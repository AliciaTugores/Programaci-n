def find_uniq(arr):
    a, b = set (arr) 
    if arr.count(a) == 1:
        return a
    else:
        return b



if __name__ == "__main__":
    print("Basic tests")
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10
    print("pass")