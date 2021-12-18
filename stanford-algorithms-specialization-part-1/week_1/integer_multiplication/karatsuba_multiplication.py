def get_product_karatsuba_style(x, y):
    if x == 0 and y == 0:
        return 0
    if x < 10 and y < 10:
        return x * y

    x_size = len(str(x))
    y_size = len(str(y))

    max_n = max(x_size, y_size)
    if max_n % 2 == 0:
        n = max_n
    else:
        n = max_n + 1

    a, b = divmod(x, 10 ** (n // 2))
    c, d = divmod(y, 10 ** (n // 2))

    ac = get_product_karatsuba_style(a, c)
    bd = get_product_karatsuba_style(b, d)
    a_plus_b_times_c_plus_d = get_product_karatsuba_style(a + b, c + d)
    gauss_trick = a_plus_b_times_c_plus_d - bd - ac

    print("ac", ac)
    print("bd", bd)
    print("a_plus_b_times_c_plus_d: ", a_plus_b_times_c_plus_d)
    print("gauss_trick: ", gauss_trick)
    print("(10**max_n) * ac : ", (10 ** max_n) * ac)
    print("(10 ** (max_n // 2)) * gauss_trick: ", (10 ** (max_n // 2)) * gauss_trick)
    print("bd: ", bd)

    return (10 ** n) * ac + ((10 ** (n // 2)) * gauss_trick) + bd


# Test inputs:
# 3141592653589793238462643383279502884197169399375105820974944592
# 2718281828459045235360287471352662497757247093699959574966967627

def main():
    print(get_product_karatsuba_style(3141592653589793238462643383279502884197169399375105820974944592,
                                      2718281828459045235360287471352662497757247093699959574966967627))


if __name__ == "__main__":
    main()
