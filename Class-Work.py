def count(text,ltr):
    count = 0
    for c in text:
        if c == ltr:
            count += 1
    return(count)
print(count("banana","b"))

def find2(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng(ix) == ch:
            return ix
        ix += 1
    return -1
print(find2("banana", "a", 0, 3))
test(find2("banana", "a", 2) == 3)

