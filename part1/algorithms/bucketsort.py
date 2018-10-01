## By https://gist.github.com/sarrhid/5022081

def bucketsort(arr):

    buckets = [[] for x in range(10)]
    for i, x in enumerate(arr):
        buckets[int(x*len(buckets))].append(x)
    out = []
    for buck in buckets:
        out += isort(buck)
    return out


def isort(arr):
    if len(arr) <= 1: return arr
    i = 1
    while i < len(arr):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            arr[j] = k
            j -= 1
        i += 1
    return arr
