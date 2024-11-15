def books(n):
    npages=n*1000
    nbooks=npages//100
    return nbooks
n=int(input())
print(books(n))
