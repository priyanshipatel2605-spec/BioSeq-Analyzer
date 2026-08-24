# ============================================
# BioSeq Analyzer v1.0
# Author : Priyanshi Patel
# Project : Bioinformatics Mini Project
# ============================================

def dna_analysis():
    print("\n===== DNA Analysis =====")

    dna = input("Enter DNA sequence: ").upper()

    valid = True

    for base in dna:
        if base not in "ATGC":
            valid = False
            break

    if valid:
        length = len(dna)
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        gc_content = ((g + c) / length) * 100
        at_content = ((a + t) / length) * 100

        print("\n----- DNA Analysis Result -----")
        print("Length      :", length)
        print("A Count     :", a)
        print("T Count     :", t)
        print("G Count     :", g)
        print("C Count     :", c)
        print("GC Content  : {:.2f}%".format(gc_content))
        print("AT Content  : {:.2f}%".format(at_content))

    else:
        print("Invalid DNA Sequence!")
def reverse_complement():
    print("\n===== Reverse Complement =====")

    dna = input("Enter DNA sequence: ").upper()

    valid = True

    for base in dna:
        if base not in "ATGC":
            valid = False
            break

    if valid:
        complement = ""

        for base in dna:
            if base == "A":
                complement += "T"
            elif base == "T":
                complement += "A"
            elif base == "G":
                complement += "C"
            elif base == "C":
                complement += "G"

        reverse = complement[::-1]

        print("\n----- Reverse Complement Result -----")
        print("DNA                :", dna)
        print("Complement         :", complement)
        print("Reverse Complement :", reverse)

    else:
        print("Invalid DNA Sequence!")


def dna_to_rna():
    print("\n===== DNA to RNA Converter =====")

    dna = input("Enter DNA sequence: ").upper()

    valid = True

    for base in dna:
        if base not in "ATGC":
            valid = False
            break

    if valid:
        rna = dna.replace("T", "U")

        print("\n----- RNA Result -----")
        print("DNA :", dna)
        print("RNA :", rna)

    else:
        print("Invalid DNA Sequence!")
while True:

    print("\n========== BioSeq Analyzer ==========")
    print("1. DNA Analysis")
    print("2. Reverse Complement")
    print("3. DNA to RNA Converter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        dna_analysis()

    elif choice == "2":
        reverse_complement()

    elif choice == "3":
        dna_to_rna()

    elif choice == "4":
        print("\nThank you for using BioSeq Analyzer!")
        print("Program Closed Successfully.")
        break

    else:
        print("\nInvalid Choice! Please enter a number from 1 to 4.")