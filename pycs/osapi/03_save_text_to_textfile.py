from pathlib import Path
import numpy as np
from string import ascii_letters
from itertools import batched


if __name__ == "__main__":
    fpath = Path(__file__).parent.parent / "data" / "write_to_textfile.txt"
    text = "".join(np.random.choice(list(ascii_letters), replace=True, size=10_000))
    # (1) write the text to file
    with open(fpath, "wt") as f:
        for k in range(0, len(text), 50):
            f.write(text[k:k+50])
    # (2) read the text from the file
    with open(fpath, "rt") as f:
        lines = []
        while line := f.readline():
            lines.append(line)
    # (3) do check to confirm that both original and loaded strings are equal
    print("Check result: ")
    print(text == "".join(lines))
