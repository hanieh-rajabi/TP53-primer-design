from Bio import AlignIO
import matplotlib.pyplot as plt


# read alignment
alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)


scores = []


# calculate conservation score
for i in range(alignment.get_alignment_length()):

    column = alignment[:, i]

    # remove gaps
    bases = [b for b in column if b != "-"]

    if len(bases) == 0:
        scores.append(0)
        continue

    most_common = max(
        set(bases),
        key=bases.count
    )

    score = bases.count(most_common) / len(bases)

    scores.append(score)



plt.figure(figsize=(12,4))

plt.plot(
    range(1, len(scores)+1),
    scores
)

plt.xlabel("TP53 transcript alignment position")
plt.ylabel("Conservation score")

plt.title(
    "TP53 transcript variant conservation profile"
)

plt.ylim(0,1.05)

plt.grid(True)

plt.savefig(
    "../results/TP53_conservation_profile.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
