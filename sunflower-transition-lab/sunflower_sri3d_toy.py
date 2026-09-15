from itertools import combinations

def is_sunflower(sets):
    sets = [frozenset(s) for s in sets]
    if len(sets) < 2:
        return True
    core = sets[0] & sets[1]
    return all(
        (sets[i] & sets[j]) == core
        for i in range(len(sets))
        for j in range(i + 1, len(sets))
    )

def ordinary_shadow(family):
    out = set()
    for F in family:
        for x in F:
            out.add(frozenset(F - {x}))
    return out

def oriented_tokens(family):
    out = []
    for source_id, F in enumerate(family):
        for x in F:
            out.append({
                "payload": frozenset(F - {x}),
                "removed": x,
                "source_id": source_id,
                "source": F,
            })
    return out

def has_naive_shadow_sunflower(family, r=3):
    shadow = list(ordinary_shadow(family))
    return any(is_sunflower(c) for c in combinations(shadow, r))

def has_liftable_oriented_sunflower(family, r=3):
    tokens = oriented_tokens(family)
    for comb in combinations(tokens, r):
        if len({t["source_id"] for t in comb}) != r:
            continue

        payloads = [t["payload"] for t in comb]
        if not is_sunflower(payloads):
            continue

        parents = [t["source"] for t in comb]
        if is_sunflower(parents):
            return True
    return False

def run(n=6, k=3, family_size=3, r=3):
    universe = range(1, n + 1)
    ksets = [frozenset(c) for c in combinations(universe, k)]

    stats = {
        "families": 0,
        "source_sunflower": 0,
        "naive_projection_positive": 0,
        "naive_false_green": 0,
        "oriented_lift_positive": 0,
    }

    for fam in combinations(ksets, family_size):
        fam = list(fam)
        stats["families"] += 1

        source = is_sunflower(fam)
        naive = has_naive_shadow_sunflower(fam, r)
        lifted = has_liftable_oriented_sunflower(fam, r)

        stats["source_sunflower"] += int(source)
        stats["naive_projection_positive"] += int(naive)
        stats["naive_false_green"] += int(naive and not source)
        stats["oriented_lift_positive"] += int(lifted)

    return stats

if __name__ == "__main__":
    print(run())
