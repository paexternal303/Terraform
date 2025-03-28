A =[1,78,46,4,34,10,50,2]
N = len(A)
def Algorithm(A,N):
    #B <- Array[N]
    B = A[N]
    B=[0]*N
    for i in range(1,N):
        B[A[i]]+=1
        i=1
    #for i <-- 1 to N
    for j in range(1,N):
    #for k <-- to B[j]
        for k in range(0,B[j]):
            A[i]=j
            i+=1
    return

Algorithm(A,N)
print(A)
