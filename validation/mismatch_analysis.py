from Bio import AlignIO


alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)


forward = "TGAAGCTCCCAGAATGCCAG"
reverse = "AGCTGCCCTGGTAGGTTTTC"


def reverse_complement(seq):
    complement = str.maketrans(
        "ATCG",
        "TAGC"
    )
    return seq.translate(complement)[::-1]


reverse_rc = reverse_complement(reverse)


def count_mismatch(primer, target):
    mismatches = []
    
    for i, (p, t) in enumerate(zip(primer, target), start=1):
        if p != t:
            mismatches.append(i)

    return mismatches



for record in alignment:

    seq = str(record.seq)

    print("\n", record.id)

    # Forward search
    f_start = seq.replace("-", "").find(forward)

    if f_start != -1:
        print("Forward primer: found")
        print("Mismatch: 0")
    else:
        print("Forward primer: not exact")


    # Reverse search
    r_start = seq.replace("-", "").find(reverse_rc)

    if r_start != -1:
        print("Reverse primer: found")
        print("Mismatch: 0")
    else:
        print("Reverse primer: not exact")
