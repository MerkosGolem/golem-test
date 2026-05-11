"""Tests for string utilities."""

from main import greet, reverse_string


def test_greet():
    assert greet("World") == "Hello, World!"


def test_greet_empty():
    assert greet("") == "Hello, !"


def test_reverse_string_normal():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""


def test_reverse_string_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string("racecar") == "racecar"
