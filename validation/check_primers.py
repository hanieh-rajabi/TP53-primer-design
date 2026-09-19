from Bio import AlignIO

alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)

forward = "TGAAGCTCCCAGAATGCCAG"
reverse = "AGCTGCCCTGGTAGGTTTTC"


for record in alignment:
    seq = str(record.seq).replace("-", "")

    f_match = forward in seq

    # reverse complement
    rev_comp = reverse.translate(
        str.maketrans("ATCG", "TAGC")
    )[::-1]

    r_match = rev_comp in seq

    print(record.id)
    print("Forward:", f_match)
    print("Reverse:", r_match)
    print()
