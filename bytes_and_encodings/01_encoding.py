

if __name__ == "__main__":

    # ----- (1) bin(.) getting binary representation of a given positive integer -----
    x: int = 123123
    print(f"{x=}")
    print(f"{bin(x)=}")

    # ----- (2) encoding a string in UTF-8 -----
    str_ = "Hello World; Polish letters ąęćż"
    encoded_str: bytes = str_.encode(encoding="utf-8")
    print(f"{encoded_str=}")
    print(f"{type(encoded_str)=}")

    for i, x in enumerate(encoded_str):
        print(f"{i}: {x}")

    encoded_str_list = list(encoded_str)
    print(f"{encoded_str_list=}")

    bytes(encoded_str_list).decode("utf-8")
    