def solve(l1,l2):
    n = len(l1)
    if n == 0:
        return(0)
    ans = [0 for i in range(n+1)]
    ans[n-1] = max(l1[n-1],l2[n-1]) - min(l1[n-1],l2[n-1])
    for i in range(n-2,-1,-1):
        vert = max(l1[i],l2[i]) - min(l1[i],l2[i]) + ans[i+1]
        horz = (max(l1[i],l1[i+1]) - min(l1[i],l1[i+1]) +
        max(l2[i],l2[i+1]) - min(l2[i],l2[i+1])) + ans[i+2]
        ans[i] = max(vert,horz)
    return(ans[0])




n = int(input())
l1 = [int(i) for i in input().strip().split()]
l2 = [int(i) for i in input().strip().split()]
print(solve(l1, l2))