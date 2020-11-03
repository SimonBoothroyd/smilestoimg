from ._version import get_versions

try:
    __version__ = get_versions()["version"]
    del get_versions
except ValueError:
    pass
