# 🧬 Protein Mutation Analyzer (Function-Based)
import random
import time
from Full_Codon_Table import codon_table  

time.sleep(1)

def transcribe(dna):
    return dna.replace("T", "U")

def get_codons(rna):
    return [rna[i:i+3] for i in range(0, len(rna), 3) if len(rna[i:i+3]) == 3]

def translate(codons):
    protein = []
    for codon in codons:
        amino = codon_table.get(codon, "???")
        if amino == "STOP":
            break
        protein.append(amino)
    return protein

def classify_mutation(original, mutated):
    if mutated == original:
        return "🔹 Silent Mutation"
    elif "STOP" in mutated:
        return "🛑 Nonsense Mutation"
    else:
        return "⚠️ Missense Mutation"

def analyze_mutation(original_dna, mutation_pos, new_base):
    mutated_dna = original_dna[:mutation_pos] + new_base + original_dna[mutation_pos + 1:]

    original_rna = original_dna.replace("T", "U")
    mutated_rna = mutated_dna.replace("T", "U")
    
    original_codons = [original_rna[i:i+3] for i in range(0, len(original_rna), 3)]
    mutated_codons = [mutated_rna[i:i+3] for i in range(0, len(mutated_rna), 3)]

    
    original_protein = [codon_table.get(c, "?") for c in original_codons]
    mutated_protein = [codon_table.get(c, "?") for c in mutated_codons]

    
    mutation_type = classify_mutation(original_protein, mutated_protein)

    
    print(mutation_type)
    print("Original DNA:   ", original_dna)
    print("Mutated  DNA:   ", mutated_dna)
    print("Original Codons:", original_codons)
    print("Mutated Codons:", mutated_codons)
    print("Original Protein:", original_protein)
    print("Mutated  Protein:", mutated_protein)

    return mutated_protein

original_dna = "ATGCTGCTACTGATCGTAGCTAGCTACGTAGCTGATGCTGATCTGATGCTGAC"  
MAX_MUTATIONS = 100
count = 0

while count < MAX_MUTATIONS:
    count += 1
    print(f"\n🔁 Mutation #{count}")

    mutation_pos = random.randint(0, len(original_dna) - 1)
    original_base = original_dna[mutation_pos]
    new_base = random.choice([b for b in "ATCG" if b != original_base])

    mutated_protein = analyze_mutation(original_dna, mutation_pos, new_base)

    if "STOP" in mutated_protein:
        print("🛑 STOP codon detected. Ending mutation loop.")
        break

else:
    print(f"⚠️ Reached {MAX_MUTATIONS} mutations. No STOP codon found.")

