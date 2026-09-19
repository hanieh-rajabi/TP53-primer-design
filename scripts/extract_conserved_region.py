from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


alignment = AlignIO.read(
    "../alignment/TP53_MSA.fasta",
    "fasta"
)


start = 400   # Python index (401 in alignment)
end = 700     # Python index (700 in alignment)


records = []


for record in alignment:

    region = record.seq[start:end]

    # حذف gap ها
    region = region.replace("-", "")

    records.append(
        SeqRecord(
            region,
            id=record.id,
            description="TP53 conserved region 401-700"
        )
    )


with open(
    "../data/TP53_conserved_401_700.fasta",
    "w"
) as output:

    for r in records:
        output.write(r.format("fasta"))


print("Extracted conserved region:")
print("Length:", len(records[0].seq))
