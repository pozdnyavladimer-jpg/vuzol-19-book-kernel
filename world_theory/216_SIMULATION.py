#!/usr/bin/env python3
"""216 toy: Fixed vs Adaptive vs Gate vs 14->10->10->8 cascade.
Toy benchmark only; it does NOT validate Sri or 14/10/10/8 as a law of nature.
"""
import numpy as np
EPS=1e-9

class Medium:
    def __init__(self,n=10,seed=0):
        self.n=n; self.rng=np.random.default_rng(seed)
        self.wh=np.clip(.45+.08*self.rng.normal(size=(n,n-1)),.05,.95)
        self.wv=np.clip(.45+.08*self.rng.normal(size=(n-1,n)),.05,.95)

    def relax(self,inp,steps=24,noise=.012):
        n=self.n; x=np.zeros((n,n)); x[:,0]=inp
        for _ in range(steps):
            z=np.zeros_like(x); q=np.full_like(x,.16)
            z[:,:-1]+=self.wh*x[:,1:]; z[:,1:]+=self.wh*x[:,:-1]
            q[:,:-1]+=self.wh; q[:,1:]+=self.wh
            z[:-1,:]+=self.wv*x[1:,:]; z[1:,:]+=self.wv*x[:-1,:]
            q[:-1,:]+=self.wv; q[1:,:]+=self.wv
            x=z/(q+EPS); x[:,0]=inp
            x+=noise*self.rng.normal(size=x.shape)
        return x

    def candidates(self,x,target):
        n=self.n; rr=np.arange(n)[:,None]
        d=np.exp(-((rr-target)/2.)**2)*np.linspace(.2,1,n)[None,:]
        h=x[:,:-1]*x[:,1:]*(.35+d[:,:-1]+d[:,1:])
        v=x[:-1,:]*x[1:,:]*(.25+d[:-1,:]+d[1:,:])
        h/=np.max(np.abs(h))+EPS; v/=np.max(np.abs(v))+EPS
        return h,v

    def apply(self,h,v,lr=.035):
        self.wh=np.clip(self.wh+lr*h,.02,1.2)
        self.wv=np.clip(self.wv+lr*v,.02,1.2)

def score(x,target):
    n=x.shape[0]; p=np.abs(x[:,-1])+EPS; p/=p.sum()
    t=np.exp(-((np.arange(n)-target)/1.25)**2); t/=t.sum()
    band=(np.abs(np.arange(n)-target)<=1)
    return .45*np.dot(p,t)+.55*p[band].sum()

def cascade(cand,seed):
    # Candidate architecture only. Fixed random projections implement 14->10->10->8.
    rng=np.random.default_rng(seed)
    R1=rng.normal(0,1/np.sqrt(14),(14,10))
    R2=rng.normal(0,1/np.sqrt(10),(10,10))
    R3=rng.normal(0,1/np.sqrt(10),(10,8))
    out=np.zeros_like(cand)
    for idx,v in np.ndenumerate(cand):
        f=np.array([v,abs(v),v*v,np.tanh(v),np.sin(v),np.cos(v)-1,v**3,
                    np.sign(v)*np.sqrt(abs(v)+EPS),np.exp(-abs(v))-1,
                    1/(1+np.exp(-3*v))-.5,np.sin(2*v),np.tanh(2*v),
                    v/(1+abs(v)),1.])
        c=np.tanh(np.tanh(np.tanh(f@R1)@R2)@R3)
        if v>.08 and np.mean(np.abs(c))>.12: out[idx]=v
    return out

def run(mode,seed,episodes=100,n=10):
    m=Medium(n,seed); rng=np.random.default_rng(seed+1000); target=n//2
    writes=0
    for ep in range(episodes):
        center=target+rng.integers(-2,3)
        inp=np.clip(np.exp(-((np.arange(n)-center)/2.3)**2)+.12*rng.normal(size=n),0,1)
        x=m.relax(inp); h,v=m.candidates(x,target)
        if mode=="fixed": continue
        if mode=="adaptive": dh,dv=h,v
        elif mode=="gate":
            dh=np.where(h>.12,h,0); dv=np.where(v>.12,v,0)
        elif mode=="cascade":
            dh=cascade(h,seed+77); dv=cascade(v,seed+77)
        writes+=np.count_nonzero(dh)+np.count_nonzero(dv)
        m.apply(dh,dv)

    vals=[]
    for _ in range(40):
        center=target+rng.integers(-3,4)
        inp=np.clip(np.exp(-((np.arange(n)-center)/2.3)**2)+.16*rng.normal(size=n),0,1)
        vals.append(score(m.relax(inp,noise=.02),target))
    return np.mean(vals),writes

def main():
    print("216 TOY SIMULATION")
    print("Local grid task: route noisy signal toward a target.\n")
    print(f"{'MODE':<10} {'TEST MEAN':>10} {'SEED SD':>10} {'WRITES':>10}")
    rows=[]
    for mode in ("fixed","adaptive","gate","cascade"):
        rs=[run(mode,s) for s in range(8)]
        mean=np.mean([x[0] for x in rs]); sd=np.std([x[0] for x in rs])
        wr=np.mean([x[1] for x in rs])
        rows.append((mode,mean,sd,wr))
        print(f"{mode:<10} {mean:10.4f} {sd:10.4f} {wr:10.1f}")
    print("\nInterpretation:")
    print("* Fixed = no persistent learning.")
    print("* Adaptive = every local candidate writes.")
    print("* Gate = only candidates above a local threshold write.")
    print("* Cascade = candidate 14->10->10->8 filter before commit.")
    print("* A cascade win here would NOT prove 14/10/10/8; widths must later be searched blindly.")
if __name__=="__main__": main()
