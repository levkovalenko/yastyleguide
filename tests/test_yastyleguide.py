from yastyleguide import __version__


def test_version():
    """Test package version. Test from template.

    It checks `__version__` number.
    """
    assert __version__ == "0.0.5a"
