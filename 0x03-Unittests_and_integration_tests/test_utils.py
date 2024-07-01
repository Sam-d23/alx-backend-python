#!/usr/bin/env python3
"""
Module for accessing nested maps and testing the functionality.
"""


import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple, Optional


def access_nested_map(nested_map: Dict[str, Any],
                      path: Tuple[str, ...],
                      default: Optional[Any] = None) -> Any:
    """
    Safely access a nested element in a dictionary using a list of keys.

    Parameters:
    nested_map (dict): The nested dictionary to access.
    path (tuple): A tuple of keys representing the path to the target value.
    default: The default value to return if the path does not exist.

    Returns:
    The value at the specified path if it exists, otherwise the default value.
    """
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except (KeyError, TypeError):
        return default


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str, ...],
                               expected: Any) -> None:
        """
        Test the access_nested_map function with various inputs.

        Parameters:
        nested_map (dict): The nested dictionary to access.
        path (tuple): A tuple of keys representing the path to the target value.
        expected: The expected value at the specified path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """
        Test the access_nested_map function to ensure it raises KeyError
        for invalid paths.

        Parameters:
        nested_map (dict): The nested dictionary to access.
        path (tuple): A tuple of keys representing the path to the target value.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception),
                         f"Key {path[-1]} not found in path {path}")


if __name__ == '__main__':
    unittest.main()
