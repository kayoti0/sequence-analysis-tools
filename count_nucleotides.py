def count_nucleotides(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

# Example usage:
seq = "ATGCGCGTAACCGT"
print(count_nucleotides(seq))
