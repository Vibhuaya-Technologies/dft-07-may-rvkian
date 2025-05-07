# ATPG Question Set 1
questions = [
    "Explain the differences between stuck-at and path-delay ATPG objectives and their impact on pattern count.",
    "Describe how X-bounding helps ATPG tools handle bus-contention and unknown values in logic.",
    "In a dual-clock design, outline how you configure ATPG launch-capture sequences across domains.",
    "Define fault coverage. After ATPG, you get 96% coverage. How do you identify and close the remaining 4%?",
    "Explain partial-scan insertion: what criteria (e.g., SCOAP) guide which flip-flops to include?",
    "Describe vector compaction techniques and how they affect fault coverage and test data volume.",
    "How does MISR-based response compression work, and what trade-offs exist in polynomial selection?",
    "After a small ECO, explain how incremental ATPG targets only affected faults without rerunning full ATPG.",
    "Discuss test-point insertion algorithms for improving controllability and observability under timing constraints.",
    "Outline power-aware ATPG constraints for scan-shift low-power modes to prevent IR-drop failures.",
    "Explain hierarchical ATPG on large SoCs: how do you stitch block-level tests for system-level validation?",
    "Describe aliasing in compressed signatures and how diagnostic ATPG localizes faults despite aliasing.",
    "How do you schedule multi-site parallel test patterns on ATE to minimize total test time?",
    "Explain the concept of X-cycle ATPG and how it improves coverage in deep-submicron designs.",
    "Given 10,000 raw vectors and a 5 ms time budget, how do you balance shift cycles and capture patterns?",
]

def main():
    for idx, q in enumerate(questions, 1):
        print(f"{idx}. {q}")

if __name__ == '__main__':
    main()
