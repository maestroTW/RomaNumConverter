rom_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
ar_dict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}
rom_list = ["I", "V", "X", "L", "C", "D", "M"]


def rom_ar(x):
    li = list(x.upper())
    li.reverse()
    num = 0
    biggest = 0
    for ch in li:
        cur = rom_dict[ch]
        if cur >= biggest:
            biggest = cur
            num += cur
        else:
            num -= cur
    return num


def ar_rom(y):
    result = ""
    for not_i in ar_dict:
        while y >= not_i:
            result += ar_dict[not_i]
            y -= not_i
    return result


print("Enter an Arabic or a roman number")
while True:
    inp = input("Number: ")
    stage = False
    for i in rom_list:  # checking the input is an arabic or roman number
        for j in list(inp.upper()):
            if i == j:
                stage = True
                break

    if stage:
        print(inp, "-->", rom_ar(inp))
    else:
        print(inp, "-->", ar_rom(int(inp)))
