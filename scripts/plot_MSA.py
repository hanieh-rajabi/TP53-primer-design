from Bio import AlignIO
import matplotlib.pyplot as plt
import numpy as np

alignment_file = "../alignment/TP53_MSA.fasta"
output_file = "../figures/TP53_MSA_visualization.png"


alignment = AlignIO.read(alignment_file, "fasta")

sequences = [str(record.seq) for record in alignment]
names = [record.id for record in alignment]

n_sequences = len(sequences)
alignment_length = alignment.get_alignment_length()

print("Number of sequences:", n_sequences)
print("Alignment length:", alignment_length)



base_to_number = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3,
    "-": 4
}

matrix = np.array([
    [base_to_number.get(base.upper(), 4) for base in seq]
    for seq in sequences
])




fig, ax = plt.subplots(figsize=(18, 4))

image = ax.imshow(
    matrix,
    aspect="auto",
    interpolation="nearest"
)

ax.set_yticks(range(n_sequences))
ax.set_yticklabels(names)

ax.set_xlabel("Alignment position")
ax.set_ylabel("TP53 transcript variant")

ax.set_title(
    "Multiple Sequence Alignment of TP53 Transcript Variants"
)


tick_step = 250

ax.set_xticks(
    np.arange(0, alignment_length, tick_step)
)

ax.set_xticklabels(
    np.arange(1, alignment_length + 1, tick_step)
)


cbar = plt.colorbar(image, ax=ax)

cbar.set_ticks([0, 1, 2, 3, 4])
cbar.set_ticklabels(["A", "C", "G", "T", "-"])

plt.tight_layout()

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
