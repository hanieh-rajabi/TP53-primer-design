import matplotlib.pyplot as plt


variants = [
    "Variant 1",
    "Variant 2",
    "Variant 3",
    "Variant 4",
    "Variant 8",
    "Variant 9",
    "Variant 12"
]

forward = [1]*7
reverse = [1]*7


fig, ax = plt.subplots(figsize=(7, 4))


x = range(len(variants))

ax.bar(
    x,
    forward,
    width=0.35,
    label="Forward primer"
)

ax.bar(
    [i + 0.35 for i in x],
    reverse,
    width=0.35,
    label="Reverse primer"
)


ax.set_xticks(
    [i + 0.175 for i in x]
)

ax.set_xticklabels(
    variants,
    rotation=45,
    ha="right"
)


ax.set_ylim(0, 1.2)

ax.set_ylabel(
    "Primer detection"
)

ax.set_title(
    "TP53 Primer Validation Across Transcript Variants"
)


ax.legend()


for i in x:
    ax.text(
        i,
        1.02,
        "✓",
        ha="center",
        fontsize=12
    )


plt.tight_layout()


plt.savefig(
    "figures/TP53_validation_summary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
