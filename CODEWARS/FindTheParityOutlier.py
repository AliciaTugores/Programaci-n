#You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
#Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(integers):
    impar = []
    par = []
    for num in integers:
        if num % 2 == 0:
            par.append(num)
        elif num % 2 != 0:
            impar.append(num)
    if len(par) > len(impar):
        return impar[0]
    else:
        return par[0]