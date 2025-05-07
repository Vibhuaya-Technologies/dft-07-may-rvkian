# ATPG Question Set 2
questions = [
    "Compare test-per-clock (TPC) and non-TPC LBIST modes in terms of speed and hardware overhead.",
    "Outline the launch-off-capture mechanism for at-speed testing, and how you validate timing post-SDF back-annotation.",
    "Describe how boundary-scan complements internal scan for mixed-signal IP blocks with analog interfaces.",
    "Explain how seed rotation in pseudorandom BIST improves coverage and supports drift diagnosis.",
    "What metrics drive selection of control vs. observation test points when compression reduces coverage?",
    "Discuss fault simulation vs. ATPG: how does vector order affect early-detect time for critical faults?",
    "How do you manage scan-chain reordering or partitioning to optimize ATPG runtime and scan shift balance?",
    "Explain low-power scan techniques, including vector reordering and gated clocks during shift and capture.",
    "Describe a methodology for diagnosing faults from failing MISR signatures using neighbor-highlighting.",
    "In mixed-clock domains, how do you insert capture paths for multi-cycle timing constraints in ATPG?",
    "How do you estimate the aliasing probability for a 32-bit MISR compressing 200-bit responses?",
    "Outline the impact of test-point insertion on clock skew and timing closure, and how to mitigate it.",
    "Describe the process of compression-driven ATPG, including justification hints to avoid misdetection.",
    "Explain how hierarchical MISR signature merging is performed for block-based compression.",
    "Given hold violations during scan, what SDF or flops changes can ensure clean shift timing?",
]

def main():
    for idx, q in enumerate(questions, 1):
        print(f"{idx}. {q}")

if __name__ == '__main__':
    main()
