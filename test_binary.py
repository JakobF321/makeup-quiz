"""An optional test to see if your binary file contents are correct"""
from pathlib import Path

from main import read_from_binary_file


def test_binary():
    """Check the binary file has the correct contents"""
    # given
    cwd = Path(__file__).parent
    filename = cwd / "file.bin"
    s_expect = "I AM done with 46120!"
    # when
    s_read = read_from_binary_file(filename=filename)
    # then
    assert s_expect.lower() == s_read.lower()
