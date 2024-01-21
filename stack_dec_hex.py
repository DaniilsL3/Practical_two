from queue import LifoQueue


def dec_hex_converter(dec: int) -> str:
    """
    Converts a decimal number to hexadecimal using Python's queue module.

    Args:
        dec (int): The decimal number to be converted.

    Returns:
        str: The string representation of the hexadecimal number.
    """


    stack = LifoQueue(maxsize=64)

    dec_to_hex_map = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    str_to_return = ""

    if dec < 16:
        stack.put(dec)
    elif dec >= 16:
        while dec > 0:
            nb = dec / 16
            rem = dec % 16
            stack.put(rem)
            dec = dec // 16

    while not stack.empty():
        hex_val = stack.get()
        if hex_val <= 9:
            str_to_return += str(hex_val)
        elif hex_val > 9:
            str_to_return += dec_to_hex_map[hex_val]

    return str_to_return


prompt = input("Enter a decimal number -> ")
print(dec_hex_converter(int(prompt)))