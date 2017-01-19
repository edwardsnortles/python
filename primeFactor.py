#author=Nathan Jenkins

def is_prime(number):
    j = None
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
    if number % i == 0:
        j = False
    return j
#-------------------------------------
def factorize(number):
    list_of_factors = [1]
    if number == 1:
        list_of_factors = [1]
    else:
        for i in range(2, number+1):
    if number % i == 0:
        list_of_factors.append(i)
    return list_of_factors
#-------------------------------------
def GCF(x,y):
    common_factors = []
    for i in factors(x):
        if y % i == 0:
            common_factors.append(i)
    return common_factors[len(common_factors)-1]
#-------------------------------------
if __name__ = '__main__':
    print GCF(55,88)
    for i in range (1, 11):
        print is_this_prime(i)
    for i in range(1, 11):
        print factors(i)
