#!/usr/bin/env python3
"""VUZOL-19 Sri-6D research reference: code, text and supplied feature records."""
from __future__ import annotations
import argparse
import ast
import json
import math
from dataclasses import dataclass
from html import escape
from pathlib import Path

AXES = (
    ("violet_future", 270, "#b366ff"),
    ("green_balance", 330, "#00e676"),
    ("yellow_struct", 30, "#ffea00"),
    ("red_mass", 90, "#ff3d00"),
    ("orange_flow", 150, "#ff9100"),
    ("blue_law", 210, "#00b0ff"),
)
KEYS = {key for key, _, _ in AXES}

@dataclass
class Result:
    domain: str
    axes: dict
    evidence: list
    gates: dict
    verdict: str
    reasons: list

    def as_dict(self):
        return {
            "schema": "vuzol19.sri6d.state.v1", "domain": self.domain,
            "axes": self.axes, "evidence": self.evidence, "gates": self.gates,
            "cascade": {name: "NOT_IMPLEMENTED" for name in
                        ("intake14", "structural10", "dynamic10", "invariants8")},
            "verdict": self.verdict, "reasons": self.reasons,
            "human_gate_required": True,
        }

def bounded_axes(raw):
    """Independent coordinates; missing values stay unknown, never zero."""
    if set(raw) - KEYS:
        raise ValueError("Unknown axis names: " + repr(sorted(set(raw) - KEYS)))
    out = {}
    for key, _, _ in AXES:
        value = raw.get(key)
        if value is not None:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{key}: expected number or null")
            if not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError(f"{key}: must be finite within [0,1]")
        out[key] = value
    return out

def from_python(source):
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return Result("code", bounded_axes({}), [f"Syntax error line {exc.lineno}"],
                      {"NORTH_INPUT": "FAIL", "EAST_RULES": "UNKNOWN",
                       "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                      "BLOCK", ["Source does not parse as Python"])
    nodes = list(ast.walk(tree))
    loops = sum(isinstance(n, (ast.For, ast.While, ast.AsyncFor)) for n in nodes)
    funcs = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in nodes)
    try_nodes = sum(isinstance(n, ast.Try) for n in nodes)
    unbounded_candidates = sum(
        isinstance(n, ast.While) and isinstance(n.test, ast.Constant)
        and n.test.value is True for n in nodes)
    # Heuristic indicators only; no security or correctness certification.
    raw = {
        "yellow_struct": min(1, 0.15 + 0.12 * funcs),
        "orange_flow": min(1, 0.10 + 0.10 * loops),
        "red_mass": min(1, 0.10 + 0.30 * unbounded_candidates),
        "green_balance": min(1, 0.10 + 0.12 * try_nodes),
    }
    reasons = ["AST-derived scores are heuristic, not correctness evidence"]
    if unbounded_candidates:
        reasons.append("while True detected: inspect cancellation, blocking and exit behavior")
    return Result("code", bounded_axes(raw),
                  [f"Parsed {len(nodes)} AST nodes; functions={funcs}, loops={loops}"],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "HOLD", reasons)

def from_text(source):
    if not source.strip():
        return Result("language", bounded_axes({}), ["Empty text"],
                      {"NORTH_INPUT": "FAIL", "EAST_RULES": "UNKNOWN",
                       "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                      "BLOCK", ["Empty input"])
    return Result("language", bounded_axes({}),
                  [f"Text length={len(source)} characters"],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "RESEARCH", ["No validated semantic encoder supplied; interpretation required"])

def from_features(obj):
    if not isinstance(obj, dict) or not isinstance(obj.get("domain"), str):
        raise ValueError("Feature input must be an object with a domain")
    axes = bounded_axes(obj.get("axes", {}))
    sources = obj.get("sources", [])
    if not isinstance(sources, list):
        raise ValueError("sources must be a list")
    return Result(obj["domain"], axes,
                  ["User-supplied axes; not independently verified"] + [str(s) for s in sources],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "RESEARCH", ["No calibrated domain-specific invariants or thresholds supplied"])

def svg(result, title="VUZOL-19 Sri-6D state"):
    cx, cy, radius = 350, 320, 190
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 680">',
         '<rect width="700" height="680" fill="#080d1b"/>',
         f'<text x="350" y="36" fill="white" font-size="20" text-anchor="middle">{escape(title)}</text>',
         f'<text x="350" y="62" fill="#ffdd66" font-size="14" text-anchor="middle">{escape(result.verdict)} · RESEARCH VISUALIZATION</text>']
    for fraction in (0.25, 0.5, 0.75, 1.0):
        pts = " ".join(f"{cx + radius*fraction*math.cos(math.radians(d)):.1f},{cy + radius*fraction*math.sin(math.radians(d)):.1f}" for _, d, _ in AXES)
        s.append(f'<polygon points="{pts}" stroke="#33435c" fill="none"/>')
    polygon = []
    for key, degrees, color in AXES:
        angle = math.radians(degrees)
        endx, endy = cx + radius*math.cos(angle), cy + radius*math.sin(angle)
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{endx:.1f}" y2="{endy:.1f}" stroke="{color}" stroke-opacity="0.5"/>')
        value = result.axes[key]
        if value is not None:
            polygon.append((cx + radius*value*math.cos(angle), cy + radius*value*math.sin(angle)))
        lx, ly = cx + 245*math.cos(angle), cy + 245*math.sin(angle)
        label = f"{key}: {value:.2f}" if value is not None else f"{key}: ?"
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" fill="{color}" font-size="11" text-anchor="middle">{escape(label)}</text>')
    if len(polygon) == 6:
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in polygon)
        s.append(f'<polygon points="{pts}" fill="#9e80ff" fill-opacity="0.18" stroke="#b69cff" stroke-width="3"/>')
    s.append('<circle cx="350" cy="320" r="7" fill="white"/>')
    s.append('<text x="350" y="620" text-anchor="middle" fill="#cbd5e1" font-size="13">Unknown axes are intentionally not interpolated.</text>')
    s.append('</svg>')
    return "\n".join(s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", choices=("code", "language", "features"), required=True)
    parser.add_argument("--input", required=True, help="Source file path")
    parser.add_argument("--out", default="sri6d_report.json")
    parser.add_argument("--svg", default="sri6d_state.svg")
    args = parser.parse_args()
    source = Path(args.input).read_text(encoding="utf-8")
    if args.domain == "code":
        result = from_python(source)
    elif args.domain == "language":
        result = from_text(source)
    else:
        result = from_features(json.loads(source))
    Path(args.out).write_text(json.dumps(result.as_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    Path(args.svg).write_text(svg(result), encoding="utf-8")
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
