to_sort = [30,20,10,9,8,7,6,4,2,1]

def merge(x, y):

    i = 0
    j = 0
    result = []
    while i < len(x) and j < len(y):

        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1

    if i == len(x):
        result += y[j:]
    else:
        result += x[i:]


    return result




def merge_sort(x):

    if len(x) == 1:
        return x

    mid = len(x)//2
    return merge(merge_sort(x[:mid]), merge_sort(x[mid:]))

print(merge_sort(to_sort))
