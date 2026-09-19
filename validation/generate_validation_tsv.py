from Bio import AlignIO


alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)


forward = "TGAAGCTCCCAGAATGCCAG"
reverse = "AGCTGCCCTGGTAGGTTTTC"


def reverse_complement(seq):
    comp = str.maketrans("ATCG", "TAGC")
    return seq.translate(comp)[::-1]


reverse_rc = reverse_complement(reverse)


def count_mismatch(primer, target):
    mismatches = []

    for i, (p, t) in enumerate(zip(primer, target), start=1):
        if p != t:
            mismatches.append(i)

    return mismatches


out = open(
    "TP53_primer_validation.tsv",
    "w"
)


out.write(
    "Variant\tForward_match\tReverse_match\t"
    "Forward_mismatch\tReverse_mismatch\t"
    "Forward_3prime_mismatch\tReverse_3prime_mismatch\n"
)


for record in alignment:

    seq = str(record.seq).replace("-", "")

    f_pos = seq.find(forward)
    r_pos = seq.find(reverse_rc)


    if f_pos != -1:
        f_target = seq[f_pos:f_pos+len(forward)]
        f_mismatch = count_mismatch(forward, f_target)
    else:
        f_mismatch = ["NA"]


    if r_pos != -1:
        r_target = seq[r_pos:r_pos+len(reverse_rc)]
        r_mismatch = count_mismatch(reverse_rc, r_target)
    else:
        r_mismatch = ["NA"]


    f_3prime = any(
        x >= len(forward)-4 for x in f_mismatch
    )

    r_3prime = any(
        x >= len(reverse_rc)-4 for x in r_mismatch
    )


    out.write(
        f"{record.id}\t"
        f"{f_pos!=-1}\t"
        f"{r_pos!=-1}\t"
        f"{len(f_mismatch) if f_mismatch!=['NA'] else 'NA'}\t"
        f"{len(r_mismatch) if r_mismatch!=['NA'] else 'NA'}\t"
        f"{f_3prime}\t"
        f"{r_3prime}\n"
    )


out.close()

print("TP53 primer validation table created.")
