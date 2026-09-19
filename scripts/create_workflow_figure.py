import matplotlib.pyplot as plt


steps = [
    "TP53 transcript variants",
    "Multiple Sequence Alignment",
    "Conservation analysis",
    "Conserved region identification\n(401–700 bp)",
    "Consensus sequence extraction",
    "Primer3 primer design",
    "Variant validation\n(7/7 TP53 transcripts)",
    "Primer-BLAST specificity analysis",
    "Final TP53 primer pair"
]


fig, ax = plt.subplots(figsize=(6, 10))

ax.axis("off")


y_positions = list(range(len(steps), 0, -1))


for i, (step, y) in enumerate(zip(steps, y_positions)):

    ax.text(
        0.5,
        y,
        step,
        ha="center",
        va="center",
        fontsize=10,
        bbox=dict(
            boxstyle="round,pad=0.5"
        )
    )

    if i < len(steps)-1:
        ax.annotate(
            "",
            xy=(0.5, y-0.45),
            xytext=(0.5, y-0.15),
            arrowprops=dict(
                arrowstyle="->"
            )
        )


plt.title(
    "TP53 Primer Design Workflow",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    "figures/TP53_workflow.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
