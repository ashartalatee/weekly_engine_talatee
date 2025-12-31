from rapidfuzz import fuzz

def string_similarity(a: str, b: str) -> float:
    """
    Menghitung tingkat kemiripan dua string (0-100).
    """
    if not isinstance(a, str) or not isinstance(b, str):
        return 0.0
    
    a = a.strip().lower()
    b  = b.strip().lower()

    return float(fuzz.token_sort_ratio(a, b))

if __name__ == "__main__":
    print(string_similarity("Andi Wijaya", "Andi W."))
    print(string_similarity("PT Sumber Makmur", "Sumber Makmur PT"))
    print(string_similarity("Budi", "Citra"))
