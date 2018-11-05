def MA():
    NUM=int(input())
    A=[int(n) for n in input().split()]
    CA=int(input())
    R=CA-1
    
    if R == 0:
        for item in A:
            print(item, end=' ')
    else:
        B = [0] * NUM
        C = [0] * NUM
        D = list()
        for i in range(0, NUM):
            if (i % R != 0):
                B[i] = (max(A[i], B[i - 1]))
            else:
                B[i] = A[i]
        
        C[-1] = A[-1]
        for i in range(NUM-2, -1, -1):
            if ((i+1) % R != 0):
                C[i] = max(A[i], C[i + 1])
            else:
                C[i] = A[i]
        for i in range(0, NUM-R):
            D.append(max(C[i], B[i+CA-1]))
        
        for i in D:
            print(i, end=' ')
    
if __name__ == "__main__":            
    MA()	
