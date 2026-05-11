"""A tiny string utilities module."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def reverse_string(s: str) -> str:
    """Return the reversed version of the given string."""
    return s[::-1]
