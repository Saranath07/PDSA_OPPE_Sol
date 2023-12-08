def minmax(a,b):
    for i in range(len(a)):
        if a[i]<b[i]:
            (a[i],b[i]) = (b[i],a[i])
    return(max(a)*max(b))

a = eval(input())
b = eval(input())
print(minmax(a,b))