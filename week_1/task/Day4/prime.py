def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def main():
    a = 12
    b = 15

    if check_prime(a):
        print(str(a) + '는 소수입니다.')
    else:
        print(str(a) + '는 소수가 아닙니다.')

    if check_prime(b):
        print(str(a) + '는 소수입니다.')
    else:
        print(str(a) + '는 소수가 아닙니다.')
    print('최소공배수: ', lcm_value, ', 최대공약수: ', gcd_value)

if __name__ == '__main__':
    main()
