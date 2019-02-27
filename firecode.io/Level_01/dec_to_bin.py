# Binary Representation

def dec_to_bin(number):
    if number < 2:
        return str(number)

    return dec_to_bin(number // 2) + str(number % 2)
    # Other method
    # return dec_to_bin(number // 2) + dec_to_bin(number % 2)


if __name__ == '__main__':
    arr = [6, 5, 10, 15, 200, 256, 257]
    for i in arr:
        print(f"bin({i}) = {bin(i)[2:]}")
        print(f"dec_to_bin({i}) = {dec_to_bin(i)}")
        print(f"dec_to_bin({i}) is {bin(i)[2:] == dec_to_bin(i)}")
        print("-----------------------------")
