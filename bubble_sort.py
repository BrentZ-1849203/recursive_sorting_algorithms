def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Recursive function to perform bubble sort on sublist `A[i…n]`
def bubbleSort(A, n):
 
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)
 
    if n - 1 > 1:
        bubbleSort(A, n - 1)
 
 
if __name__ == '__main__':
 
    A = list(map(int, input("Enter multiple values: ").split()))
 
    bubbleSort(A, len(A))
 
    # print the sorted list
    print(A)
