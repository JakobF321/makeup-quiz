""""""
from pathlib import Path


def write_to_binary_file(filename, s):
    """Take a string and write it to a binary file"""
    filename = Path(filename)
    with open(filename, "wb") as f:
        f.write(s.encode("utf-8"))


def read_from_binary_file(filename):
    """Read a string from a binary file"""
    filename = Path(filename)
    with open(filename, "rb") as f:
        s = f.read().decode("utf-8")
    return s


if __name__ == "__main__":
    cwd = Path(__file__).parent

    # ----- generate/save a binary file -----
    S = "I am NOT done with 46120!"
    FILENAME = cwd / "file.bin"
    write_to_binary_file(filename=FILENAME, s=S)

    # ----- read a binary file -----
    s_read = read_from_binary_file(filename=FILENAME)
    print(s_read)
