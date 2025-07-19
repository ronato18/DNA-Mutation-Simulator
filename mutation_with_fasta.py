import random

# 🧬 Reverse Complement Function
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement.get(base, '?') for base in reversed(dna)])

# 📄 FASTA Reader
def read_fasta(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])
            return sequence
    except FileNotFoundError:
        print("❌ File not found.")
        return None

# ✅ Validator
def is_valid_dna(dna):
    return set(dna.upper()).issubset({'A', 'T', 'C', 'G'})

# 🧪 Mutation Function
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

# 💾 FASTA Writer
def write_fasta(sequence, header, filename):
    with open(filename, "w") as f:
        f.write(f">{header}\n")
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i+70] + "\n")

# 🚀 Main Flow
filename = input("Enter FASTA file name (e.g. sample_dna.fasta): ").strip()
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

else:
    print("❌ Invalid DNA sequence.")
