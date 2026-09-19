import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 3))

ax.axis("off")


# Main TP53 region line
ax.plot(
    [0.1, 0.9],
    [0.5, 0.5],
    linewidth=2
)


# Forward primer marker
ax.plot(
    [0.25, 0.35],
    [0.5, 0.5],
    linewidth=6
)

ax.text(
    0.25,
    0.65,
    "Forward primer\nTGAAGCTCCCAGAATGCCAG",
    ha="center",
    fontsize=9
)


# Reverse primer marker
ax.plot(
    [0.65, 0.75],
    [0.5, 0.5],
    linewidth=6
)

ax.text(
    0.7,
    0.25,
    "Reverse primer\nAGCTGCCCTGGTAGGTTTTC",
    ha="center",
    fontsize=9
)


# Amplicon bracket
ax.annotate(
    "",
    xy=(0.75, 0.42),
    xytext=(0.35, 0.42),
    arrowprops=dict(
        arrowstyle="<->"
    )
)

ax.text(
    0.55,
    0.35,
    "137 bp amplicon",
    ha="center",
    fontsize=10
)


# Labels
ax.text(
    0.1,
    0.55,
    "5'",
    fontsize=12
)

ax.text(
    0.92,
    0.55,
    "3'",
    fontsize=12
)

ax.text(
    0.5,
    0.85,
    "TP53 conserved region (401–700 bp)",
    ha="center",
    fontsize=12
)


plt.xlim(0, 1)
plt.ylim(0, 1)

plt.savefig(
    "figures/TP53_primer_design.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
