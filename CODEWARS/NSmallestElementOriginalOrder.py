#Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not 
#getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number n of smallest elements to return.
#Also:
#the number of elements to be returned cannot be higher than the array/list/vector length;
#elements can be duplicated;
#in case of duplicates, just return them according to the original order (see third example for more clarity).
def first_n_smallest(arr, n):
    list = sorted(arr)[:n]
    counter = 0
    answer = []
    for i in arr:
        if i in list and counter < n:
            answer.append(i)
            list.remove(i)
            counter += 1
    return answer