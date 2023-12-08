def peak_unimodal(A):
    low = 0
    high = len(A)-1
    while True:
        mid = (low+high)//2
        if A[mid-1]<A[mid] and A[mid]<A[mid+1]:
            low = mid
        elif A[mid-1]>A[mid] and A[mid]>A[mid+1]:
            high = mid
        else:
            return mid