# DNA Sequence Statistics

sequence = input("Enter a DNA sequence: ")

sequence = sequence.upper()

if sequence and all(base in "ATGC" for base in sequence):
    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    print("\nDNA Sequence Statistics")
    print("-----------------------")
    print("Sequence length:", length)
    print("A count:", a_count)
    print("T count:", t_count)
    print("G count:", g_count)
    print("C count:", c_count)
    print("GC content: {:.2f}%".format(gc_content))
    print("AT content: {:.2f}%".format(at_content))

else:
    print("Invalid DNA sequence. Please use only A, T, G, and C.")