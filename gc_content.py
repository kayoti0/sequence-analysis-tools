def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    gc = ((g + c) / len(sequence)) * 100
    return round(gc, 2)

# Example usage:
seq = "ATGCGCGTAACCGT"
print("GC Content:", gc_content(seq), "%")
