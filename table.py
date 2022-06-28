n=int(input("enter the number"))
a={}
i=1
a[i]=n
while i<=n:
    m=[]
    j=1
    while j<=10:
        pro=i*j
        m.append(pro)
        j=j+1
    a[i]=m
    i=i+1
print(a)