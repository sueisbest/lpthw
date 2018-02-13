with open('quicksort.in','r') as fh:
    read_ins=fh.readline().split(',')

eis=[]
for each in read_ins:
    eis.append(int(each))

print(eis)

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    print(f'A[{i}] placed. A[{i}]={A[i]}')
    return i+1

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,p+1,r)

quicksort(eis,0,len(eis)-1)

print(eis)

