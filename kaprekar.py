# Kaprekar's numbers
# cycle of length at most 7
#
# https://en.wikipedia.org/wiki/6174

def fpad(s: str) -> str:
    while len(s) < 4:
        s = "0" + s
    return s

def bpad(s: str) -> str:
    while len(s) < 4:
        s = s + "0" 
    return s

def sort_and_sub(n: int) -> int:
    smol_n = int(fpad("".join(sorted(str(n)))))
    big_n = int(bpad("".join(reversed(sorted(str(n))))))
    # print("big_n: {}, smol_n: {}".format(big_n, smol_n))
    return big_n - smol_n

def kaprekar_iter(n: int, count: int) -> tuple[int,int]:
    new_n = sort_and_sub(n)
    # print("count: {}\tgot n: {}\tnew n: {}".format(count,n,new_n))
    count += 1
    return new_n,count

def kaprekar_length(n: int) -> int:
    """get the length of the kaprekar cycle for n"""
    KAP=6174
    if sort_and_sub(n) == 0:
        print("{} is monodigital".format(n))
        return 0

    n_ = n
    count = 0
    while n_ != KAP:
        assert(sort_and_sub(n_) != 0)
        n_,count = kaprekar_iter(n_,count)

    print("final count for {}: {}".format(n,count))
    return count

if __name__ == "__main__":
    D = {}
    for i in range(1001, 10_000):
        D[i] = kaprekar_length(i)

    max_key = max(D, key=D.get)
    print(f"Key with max value: {max_key}, Value: {D[max_key]}")
