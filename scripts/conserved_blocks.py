from Bio import AlignIO


alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)


window_size = 100


scores = []


# Calculate conservation per position

for i in range(alignment.get_alignment_length()):

    column = alignment[:, i]

    bases = [
        b for b in column
        if b != "-"
    ]

    if len(bases) == 0:
        scores.append(0)
        continue

    most_common = max(
        set(bases),
        key=bases.count
    )

    score = bases.count(most_common) / len(bases)

    scores.append(score)



print("Region\tMean conservation")


for start in range(
    0,
    len(scores)-window_size,
    window_size
):

    window = scores[start:start+window_size]

    mean_score = sum(window)/len(window)

    print(
        f"{start+1}-{start+window_size}\t{mean_score:.3f}"
    )
