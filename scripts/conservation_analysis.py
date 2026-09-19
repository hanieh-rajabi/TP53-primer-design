from Bio import AlignIO

alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)

num_sequences = len(alignment)

print("Number of sequences:", num_sequences)
print("Alignment length:", alignment.get_alignment_length())


# calculate conservation for each position

conservation = []

for i in range(alignment.get_alignment_length()):
    column = alignment[:, i]

    # remove gaps
    bases = [b for b in column if b != "-"]

    if len(bases) == 0:
        conservation.append(0)
        continue

    most_common = max(
        set(bases),
        key=bases.count
    )

    score = bases.count(most_common) / len(bases)

    conservation.append(score)


# find highly conserved regions

threshold = 0.90

regions = []
start = None

for i, score in enumerate(conservation):

    if score >= threshold:
        if start is None:
            start = i

    else:
        if start is not None:
            if i - start >= 20:
                regions.append(
                    (start+1, i)
                )
            start = None


print("\nConserved regions (>90%):")

