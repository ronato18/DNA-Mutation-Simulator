
def find_motif_positions(dna_seq, motif):
    positions = []
    for i in range(len(dna_seq) - len(motif) + 1):
        if dna_seq[i:i+len(motif)] == motif:
            positions.append(i)
    return positions

dna = input("🔡 Enter DNA sequence: ").upper().strip()
motif_input = input("🔍 Enter motifs (comma-separated): ").upper().strip()
motif_list = [m.strip() for m in motif_input.split(",") if m.strip()]

report_lines = []
report_lines.append("🧬 MOTIF REPORT")
report_lines.append(f"Sequence Length: {len(dna)} bases\n")

for motif in motif_list:
    positions = find_motif_positions(dna, motif)
    count = len(positions)
    report_lines.append(f"🔎 Motif: {motif}")
    report_lines.append(f"Count: {count}")
    report_lines.append(f"Positions: {positions}\n")

valid_bases = {"A", "T", "C", "G"}
if not set(dna).issubset(valid_bases):
    print("❌ Invalid DNA sequence. Use only A, T, C, G.")
else:
    positions = find_motif_positions(dna, motif)
    count = len(positions)

    if count > 0:
        print(f"\n✅ Motif '{motif}' found {count} time(s) at positions: {positions}")
    else:
        print(f"\n❌ Motif '{motif}' not found.")

# 🧬 MOTIF SEARCH TOOL

def read_fasta(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])
        return sequence.upper()
    except Exception as e:
        print(f"❌ Error reading FASTA file: {e}")
        return None

def find_motif_positions(dna_seq, motif):
    positions = []
    i = 0
    while i <= len(dna_seq) - len(motif):
        if dna_seq[i:i+len(motif)] == motif:
            positions.append(i)
        i += 1  # allows overlap
    return positions

# 📥 Input mode
mode = input("📥 Choose input mode — 'manual' or 'fasta': ").strip().lower()

if mode == "manual":
    dna = input("🔡 Enter DNA sequence: ").upper().strip()
elif mode == "fasta":
    file_name = input("📂 Enter FASTA file name: ").strip()
    dna = read_fasta(file_name)
else:
    print("❌ Invalid mode. Use 'manual' or 'fasta'.")
    dna = None

# 🔎 Proceed if valid
if dna:
    valid_bases = {"A", "T", "C", "G"}
    if not set(dna).issubset(valid_bases):
        print("❌ Invalid DNA sequence. Use only A, T, C, G.")
    else:
        motif_input = input("🔍 Enter motifs (comma-separated): ").upper().strip()
        motif_list = [m.strip() for m in motif_input.split(",") if m.strip()]

        report_lines = []
        report_lines.append("🧬 MOTIF REPORT")
        report_lines.append(f"Sequence Length: {len(dna)} bases\n")

        for motif in motif_list:
            positions = find_motif_positions(dna, motif)
            count = len(positions)
            report_lines.append(f"🔎 Motif: {motif}")
            report_lines.append(f"Count: {count}")
            report_lines.append(f"Positions: {positions}\n")

            if count > 0:
                print(f"\n✅ Motif '{motif}' found {count} time(s) at positions: {positions}")
            else:
                print(f"\n❌ Motif '{motif}' not found.")

        # 💾 Save to file
        with open("motif_report.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print("\n📁 Motif report saved to 'motif_report.txt'")
