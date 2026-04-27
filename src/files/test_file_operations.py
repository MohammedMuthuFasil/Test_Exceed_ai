"""Additional file handling tests - manually written for read, write, and seek operations."""

import os
import tempfile


def test_write_and_read_file():
    path = os.path.join(tempfile.gettempdir(), "test_write.txt")
    with open(path, "w") as f:
        f.write("hello world")
    with open(path, "r") as f:
        assert f.read() == "hello world"
    os.remove(path)

def test_append_to_file():
    path = os.path.join(tempfile.gettempdir(), "test_append.txt")
    with open(path, "w") as f:
        f.write("first")
    with open(path, "a") as f:
        f.write(" second")
    with open(path, "r") as f:
        assert f.read() == "first second"
    os.remove(path)

def test_readline_returns_one_line():
    path = os.path.join(tempfile.gettempdir(), "test_readline.txt")
    with open(path, "w") as f:
        f.write("line1\nline2\nline3")
    with open(path, "r") as f:
        assert f.readline() == "line1\n"
        assert f.readline() == "line2\n"
        assert f.readline() == "line3"
    os.remove(path)

def test_readlines_returns_list():
    path = os.path.join(tempfile.gettempdir(), "test_readlines.txt")
    with open(path, "w") as f:
        f.write("a\nb\nc")
    with open(path, "r") as f:
        lines = f.readlines()
    assert lines == ["a\n", "b\n", "c"]
    os.remove(path)

def test_seek_to_beginning():
    path = os.path.join(tempfile.gettempdir(), "test_seek.txt")
    with open(path, "w") as f:
        f.write("abcdef")
    with open(path, "r") as f:
        f.read(3)
        f.seek(0)
        assert f.read() == "abcdef"
    os.remove(path)

def test_writelines():
    path = os.path.join(tempfile.gettempdir(), "test_writelines.txt")
    with open(path, "w") as f:
        f.writelines(["one\n", "two\n", "three"])
    with open(path, "r") as f:
        assert f.read() == "one\ntwo\nthree"
    os.remove(path)

def test_file_context_manager_closes():
    path = os.path.join(tempfile.gettempdir(), "test_close.txt")
    with open(path, "w") as f:
        f.write("test")
    assert f.closed

def test_tell_position():
    path = os.path.join(tempfile.gettempdir(), "test_tell.txt")
    with open(path, "w") as f:
        f.write("hello")
    with open(path, "r") as f:
        f.read(3)
        assert f.tell() == 3
    os.remove(path)
