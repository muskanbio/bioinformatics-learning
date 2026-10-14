
# DNA Sequence Analyzer
# My first bioinformatics Python project

dna = input("Enter a DNA sequence: ").upper()

# Check whether the sequence contains only valid DNA bases
valid_bases = "ATGC"

if not dna:
    print("Error: DNA sequence cannot be empty.")

elif any(base not in valid_bases for base in dna):
    print("Error: Invalid DNA sequence!")
    print("DNA can contain only A, T, G, and C.")

else:
    length = len(dna)

    count_a = dna.count("A")
    count_t = dna.count("T")
    count_g = dna.count("G")
    count_c = dna.count("C")

    gc_content = ((count_g + count_c) / length) * 100

    print("\n--- DNA Sequence Analysis ---")
    print("DNA Sequence:", dna)
    print("Sequence Length:", length)
    print("Adenine (A):", count_a)
    print("Thymine (T):", count_t)
    print("Guanine (G):", count_g)
    print("Cytosine (C):", count_c)
    print("GC Content: {:.2f}%".format(gc_content))
