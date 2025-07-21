import random
from Full_Codon_Table import codon_table
from collections import Counter

def transcribe(dna):
    return dna.replace("T", "U")

def get_codons(rna):
    return [rna[i:i+3] for i in range(0, len(rna), 3) if len(rna[i:i+3]) == 3]

def translate(codons):
    protein = []
    for codon in codons:
        aa = codon_table.get(codon, "?")
        if aa == "STOP":
            break
        protein.append(aa)
    return protein

def classify_mutation(original, mutated):
    if original == mutated:
        return "🔹 Silent"
    elif "STOP" in mutated:
        return "🛑 Nonsense"
    else:
        return "⚠️ Missense"

def apply_mutation(dna, mutation_type):
    pos = random.randint(0, len(dna) - 1)
    base = random.choice("ATCG")
    
    if mutation_type == "Point":
        new_base = random.choice([b for b in "ATCG" if b != dna[pos]])
        mutated = dna[:pos] + new_base + dna[pos+1:]
        desc = f"Point at {pos}: {dna[pos]} → {new_base}"
    
    elif mutation_type == "Insertion":
        mutated = dna[:pos] + base + dna[pos:]
        desc = f"Insertion at {pos}: +{base}"
    
    elif mutation_type == "Deletion":
        mutated = dna[:pos] + dna[pos+1:]
        desc = f"Deletion at {pos}: -{dna[pos]}"
    
    else:
        return dna, "Invalid", ""
    
    return mutated, mutation_type, desc

# 🔁 Mutation Gauntlet
def mutation_gauntlet(original_dna, rounds=10):
    print("🎯 Mutation Gauntlet Begins!")
    original_rna = transcribe(original_dna)
    original_protein = translate(get_codons(original_rna))

    for i in range(1, rounds + 1):
        mutation_type = random.choice(["Point", "Insertion", "Deletion"])
        mutated_dna, mtype, desc = apply_mutation(original_dna, mutation_type)

        mutated_rna = transcribe(mutated_dna)
        mutated_protein = translate(get_codons(mutated_rna))
        result = classify_mutation(original_protein, mutated_protein)

        print(f"\n⚔️ Mutation #{i}: {desc}")
        print(f"🧬 Mutation Type: {mtype}")
        print(f"🧪 Result: {result}")
        print(f"🔗 Protein: {''.join(mutated_protein)}")

        if "STOP" in mutated_protein:
            print("🛑 STOP codon reached. Ending Gauntlet.")
            break

import os
from collections import Counter

def is_valid_dna(sequence):
    return all(base in "ATGC" for base in sequence.upper())

def read_fasta(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            dna = ''.join(line.strip() for line in lines if not line.startswith(">"))
            if not dna:
                print("❌ Fasta file is empty")
                return None
            if not is_valid_dna(dna):
                print("❌ Fasta contains invalid characters.")
                return None
            return dna.upper()
    except FileNotFoundError:
        print(f"❌  File not found: {filename}")
    except Exception as e:
        print(f"❌ Error reading FASTA: {e}")
    return None

def save_codon_frequency(codons, filename="codon_report.txt"):
    codon_counts = Counter(codons)
    total = sum(codon_counts.values())

    with open(filename, "w", encoding="utf-8") as f:
        f.write("📊 Codon Frequency Report\n")
        f.write(f"🧬 Total Codons: {total}\n\n")
        for codon, count in sorted(codon_counts.items()):
            frequency = (count / total) * 100
            f.write(f"{codon}: {count} ({frequency:.2f}%)\n")

    print(f"✅ Codon frequency saved to '{filename}'")

def get_dna_sequence():
    while True:
        choice = input("Enter 'M' for manual DNA input or 'F' to load FASTA file: ")

        if choice == "M":
            dna = input(" Enter DNA Sequence (A, T, C, G only): ").strip().upper()
            if not dna:
                print("❌  No input provided.")
                continue
            if is_valid_dna(dna):
                return dna
            else:
                print("❌  Invalid DNA sequence. Please try again.")

        elif choice == "F":
            filename = input("Enter FASTA filename: ").strip()
            dna = read_fasta(filename)
            if dna:
                return dna
        else:
            print("❌ Invalid choice. Type 'M' or 'F'.")

if __name__ == "__main__":
    sequence = get_dna_sequence()
    print("✅ DNA Sequence loaded successfully!")
    print(sequence)
    
    codons = get_codons(sequence)
    save_codon_frequency(codons)

    mutation_gauntlet(sequence)
    


