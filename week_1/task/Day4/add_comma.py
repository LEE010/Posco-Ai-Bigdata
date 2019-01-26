def add_comma(val):
    str_val = list(str(val))

    for d in range(1, (len(str_val) -1)//3 + 1):
        str_val[-d * 3] = ',' + str_val[-d *3]

    return ''.join(str_val)

def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_1comma_added_12 = add_comma(12)

    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_1comma_added_12)

if __name__ == '__main__':
    main()
