def repeats(arr):
    #si no se repite, hay que sumar
    sum= 0
    for i in arr:
        if arr.count(i) == 1:
            sum += int(i)
    return sum



if __name__ == "__main__":
    print("Basic tests")
    assert repeats([4,5,7,5,4,8]) == 15
    assert repeats([9, 10, 19, 13, 19, 13]) == 19
    assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
    assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) ==22
    assert repeats([5, 10, 19, 13, 10, 13]) == 24
    print("pass")