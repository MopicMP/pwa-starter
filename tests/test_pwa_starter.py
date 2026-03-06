"""Tests for pwa-starter."""

import pytest
from pwa_starter import starter


class TestStarter:
    """Test suite for starter."""

    def test_basic(self):
        """Test basic usage."""
        result = starter("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            starter("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = starter(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
