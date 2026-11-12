"""
Sri-Cube 18D / GF(2) / 9V — reproducible audit reference
========================================================

Purpose
-------
A small, transparent reference implementation of the calculations discussed
in the Vuzol-19 / Flower Gate work:

- three 3-value plates U9, U6, U3;
- three synchronous cyclic alignments and all 3x3 independent alignments;
- GF(2) XOR syndromes and matrix rank;
- Gray-code cycle verification;
- explicit separation between arithmetic/geometric filters and digital
  GF(2) observability checks.

IMPORTANT PROVENANCE NOTE
-------------------------
This is a reconstructed, independently checkable reference implementation
based on the recovered discussion and reported behavior of
`sri_18d_9v_gf2_boot.py`. It is NOT represented as the verbatim original
Gemini source file. Replace/compare it with the original repository source
when that file is available.

No physical claim is established by these calculations. The words
"plate", "resonance", "shear", "9V", and "Sri" are names in the proposed
computational model unless independently connected to a validated physical
measurement model.
"""

from itertools import permutations
from typing import Iterable, Sequence

U9 = (14, 10, 12)
U6 = (11, 7, 13)
U3 = (7, 11, 5)

# Historical candidate labels used in the discussion.
CANDIDATES = {
    "A": ((14, 10, 12), (7, 13, 11), (11, 5, 7)),
    "B": ((14, 10, 12), (11, 7, 13), (7, 11, 5)),
    "C": ((14, 10, 12), (13, 11, 7), (5, 7, 11)),
}


def xor_all(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result ^= int(value)
    return result


def gf2_rank(rows: Sequence[int], width: int = 4) -> int:
    """Rank over GF(2), treating each integer as a width-bit row."""
    basis = [0] * width
    rank = 0
    for value in rows:
        x = int(value)
        for bit in range(width - 1, -1, -1):
            if not ((x >> bit) & 1):
                continue
            if basis[bit]:
                x ^= basis[bit]
            else:
                basis[bit] = x
                rank += 1
                break
    return rank


def column_syndromes(u9, u6, u3):
    """S_m = U9_m XOR U6_m XOR U3_m for m=0,1,2."""
    return tuple(u9[i] ^ u6[i] ^ u3[i] for i in range(3))


def summarize(label, u9, u6, u3):
    syndromes = column_syndromes(u9, u6, u3)
    return {
        "label": label,
        "sums": tuple(u9[i] + u6[i] + u3[i] for i in range(3)),
        "syndromes": syndromes,
        "syndrome_rank": gf2_rank(syndromes, width=4),
        "closed_parity": xor_all(syndromes) == 0,
    }


def cyclic_rotate(values, k):
    k %= len(values)
    return tuple(values[k:] + values[:k])


def audit_nine_cyclic_alignments():
    rows = []
    for r6 in range(3):
        for r3 in range(3):
            rows.append(
                summarize(
                    f"rot6={r6},rot3={r3}",
                    U9,
                    cyclic_rotate(U6, r6),
                    cyclic_rotate(U3, r3),
                )
            )
    return rows


def audit_all_independent_permutations():
    """All 3! x 3! = 36 alignments of U6 and U3; U9 fixed."""
    rows = []
    for p6 in permutations(U6):
        for p3 in permutations(U3):
            rows.append(summarize("independent", U9, p6, p3))
    return rows


def verify_gray_cycle():
    cycle = ("00", "10", "11", "01", "00")
    flips = []
    for a, b in zip(cycle, cycle[1:]):
        flips.append(sum(x != y for x, y in zip(a, b)))
    return {
        "cycle": cycle,
        "bit_flips_per_step": tuple(flips),
        "valid_one_bit_cycle": all(n == 1 for n in flips),
    }


def check_closed_parity_invariant():
    """
    XOR(S0,S1,S2) equals XOR of all nine plate entries.
    Permuting values inside a plate leaves that plate's total XOR unchanged.
    Therefore, if total XOR is zero, every alignment has closed parity.
    """
    plate_xors = (xor_all(U9), xor_all(U6), xor_all(U3))
    total = xor_all(plate_xors)
    return {
        "plate_xors": plate_xors,
        "total_xor": total,
        "closed_for_every_alignment": total == 0,
    }


def main():
    print("BASE CANDIDATES")
    for label, (u9, u6, u3) in CANDIDATES.items():
        print(summarize(label, u9, u6, u3))

    print("\nNINE CYCLIC ALIGNMENTS")
    for row in audit_nine_cyclic_alignments():
        print(row)

    all_rows = audit_all_independent_permutations()
    target_sum = (32, 28, 30)
    print("\n36 INDEPENDENT PERMUTATIONS")
    print("total:", len(all_rows))
    print("target arithmetic sum:", sum(r["sums"] == target_sum for r in all_rows))
    print("syndrome rank distribution:",
          {rank: sum(r["syndrome_rank"] == rank for r in all_rows)
           for rank in sorted({r["syndrome_rank"] for r in all_rows})})

    print("\nCLOSED PARITY INVARIANT")
    print(check_closed_parity_invariant())

    print("\nGRAY CYCLE")
    print(verify_gray_cycle())


if __name__ == "__main__":
    main()
