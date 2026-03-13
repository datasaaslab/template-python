"""Shared testing helpers for repository-wide assertions."""

from collections.abc import Mapping


def assert_mapping_contains_subset(
    actual: Mapping[str, object],
    expected_subset: Mapping[str, object],
) -> None:
    """Assert that a mapping contains the expected key-value pairs."""
    for key, value in expected_subset.items():
        assert actual.get(key) == value, f"Expected {key!r} to equal {value!r}."
