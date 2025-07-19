import random
from collections import Counter
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement.get(base, '?') for base in reversed(dna)])

def read_fasta(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])
            return sequence
    except FileNotFoundError:
        print("❌ File not found.")
        return None

def is_valid_dna(dna):
    return set(dna.upper()).issubset({'A', 'T', 'C', 'G'})

def get_codons(dna):
    rna = dna.replace("T", "U")
    return [rna[i:i+3] for i in range(0, len(rna), 3) if len(rna[i:i+3]) == 3]

def codon_frequency(dna):
    codons = get_codons(dna)
    codon_counts = Counter(codons)

    print("📊 Codon Frequency:")
    for codon, count in codon_counts.most_common():
        print(f"{codon}: {count}")

    most_common = codon_counts.most_common(1)[0]
    least_common = codon_counts.most_common()[-1]

    print(f"\n🔥 Most used codon: {most_common[0]} → {most_common[1]} times")
    print(f"❄️ Least used codon: {least_common[0]} → {least_common[1]} times")

def mutate_dna(dna, mutation_type):
    bases = ['A', 'T', 'C', 'G']
    pos = random.randint(0, len(dna) - 1)

    if mutation_type == "point":
        original = dna[pos]
        new_base = random.choice([b for b in bases if b != original])
        mutated = dna[:pos] + new_base + dna[pos+1:]

    elif mutation_type == "insertion":
        new_base = random.choice(bases)
        mutated = dna[:pos] + new_base + dna[pos:]

    elif mutation_type == "deletion":
        mutated = dna[:pos] + dna[pos+1:]

    else:
        print("❌ Invalid mutation type")
        return dna

    print(f"🧬 Mutation: {mutation_type.upper()} at position {pos}")
    return mutated

def write_fasta(sequence, header, filename):
    with open(filename, "w") as f:
        f.write(f">{header}\n")
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i+70] + "\n")

filename = input("Enter FASTA file name:   ").strip()
original_dna = read_fasta(filename)

if original_dna and is_valid_dna(original_dna):
    print("✅ DNA sequence loaded.")
    for mut_type in ["point", "insertion", "deletion"]:
        mutated = mutate_dna(original_dna, mut_type)
        out_file = f"{mut_type}_mutation.fasta"
        write_fasta(mutated, f"{mut_type.upper()}_MUTATION", out_file)
        print(f"📄 Saved: {out_file}")

    rev_comp = reverse_complement(original_dna)
    print("🔁 Reverse Complement:", rev_comp)


    print("\n📊 Running codon frequency analysis on original DNA:")
    codon_frequency(original_dna)


else:
    print("❌ Invalid DNA sequence.")




    
