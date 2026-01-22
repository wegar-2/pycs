from pathlib import Path


if __name__ == "__main__":

    fpath = Path(__file__).parent.parent / "data" / "peloponnesian_war.txt"

    # (1) read the whole text at once
    with open(fpath, "rt") as f:
        print(f.read())

    # (2) read the text line by line -- using readline()
    with open(fpath, "rt") as f:
        while line := f.readline():
            print(line)

    # (3) read the text line by line -- but load it into list of strings first
    with open(fpath, "rt") as f:
        lines: list[str] = f.readlines()
        for line in lines:
            print(line)
