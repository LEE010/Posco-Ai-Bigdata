import random
from collections import Counter

def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def next_prime(prime):
    next_prime = prime + 1

    while(True):
        if check_prime(next_prime):
            return next_prime
        else:
            next_prime += 1

def prime_fact(num, primes, prime=2):
    if num % prime == 0:
        primes.append(prime)
        prime_fact(num//prime, primes)
    elif check_prime(num):
        primes.append(num)
        return
    else:
        prime_fact(num, primes, next_prime(prime))

def LCM(nums):
    lcm = 1
    proun_lst = []

    for num in nums:
        temp = []
        prime_fact(num, temp)
        proun_lst.append(temp)

    prouns = list(map(Counter, proun_lst))
    disjoint = {}

    for proun in prouns:
        for k,v in proun.items():
            try:
                if disjoint[k] < v:
                    disjoint[k] = v
            except KeyError:
                disjoint[k] = v

    for n in disjoint:
        lcm *= n

    return lcm


def GCD(nums):
    proun_lst = [[ i for i in range(1,num + 1) if num % i == 0] for num in nums]
    prouns = []
    result = []

    for lst in proun_lst:
        prouns += lst

    count_prouns = Counter(prouns)

    for k in count_prouns:
        if count_prouns[k] == len(nums):
            result.append(k)

    return max(result)

def main():
    a = []

    for i in range(10):
        a.append(random.randint(1, 100))

    print(a)

    lcm_value = LCM(a)
    gcd_value = GCD(a)
    print('최소공배수:', lcm_value, ', 최대공약수:', gcd_value)

if __name__ == '__main__':
    main()
