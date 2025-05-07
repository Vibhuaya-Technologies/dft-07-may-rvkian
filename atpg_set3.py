# ATPG Question Set 3
questions = [
    "Explain adaptive test flows: how does conditional ATPG extend failing patterns for higher coverage?",
    "Describe techniques to reduce ATPG runtime on 100M-gate designs, such as parallel fault dropping.",
    "How do you incorporate on-chip test-data recall (ROM) for BIST while minimizing area and routing overhead?",
    "Discuss the challenges and strategies for DFT in 3D-stacked ICs with through-silicon vias.",
    "How do you design secure DFT to prevent scan-chain misuse in cryptographic hardware?",
    "Outline an at-speed diagnosis flow using transition-fault captures and signature analysis.",
    "Explain how test compression fault models distinguish resolvable vs. unresolvable alias groups.",
    "Describe a method for in-field BIST to detect aging-induced delay faults over device lifetime.",
    "How do you integrate power-domain test strategies with IEEE-1801 UPF intent in hierarchical ATPG?",
    "Discuss mixed-mode (scan + functional) test scheduling to optimize for both coverage and speed.",
    "Explain how time-domain scan (using delay-measurement BIST) measures path delays without external testers.",
    "Outline a statistical yield analysis using per-fault failure counts from ATPG logs.",
    "Describe neighbor-highlighting and selective decompression techniques for pinpoint fault isolation.",
    "Explain low-cost vector compression hardware primitives and their trade-offs in modern DFT flows.",
    "Discuss emerging DFT challenges for quantum-dot cellular automata or neuromorphic hardware.",
]

def main():
    for idx, q in enumerate(questions, 1):
        print(f"{idx}. {q}")

if __name__ == '__main__':
    main()
