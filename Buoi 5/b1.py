chuoi = input("Nhập chuỗi: ")
stop = ["is", "a", "this"]

def remove_punctuation(s):
    dau = ".,!?()[]{}:;'\"-"
    ket_qua = ""
    for c in s:
        if c not in dau:
            ket_qua += c
    return ket_qua

def to_lower(s):
    return s.lower()

def remove_stopwords(s, stop):
    ket_qua = [t for t in s.split() if t not in stop]
    return " ".join(ket_qua)

def pipeline(s, steps):
    if not steps:        
        return s
    s = steps[0](s)
    return pipeline(s, steps[1:])

ket_qua = pipeline(chuoi, [
    remove_punctuation,to_lower,lambda x: remove_stopwords(x, stop)])
print(ket_qua)

def count_words(s):
    d = {}
    words = s.split()
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d
print(count_words(ket_qua))
