import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.model.missing import (
    get_missing_active,
    get_missing_diagram,
)


def test_get_missing_active():
    """Test getting active missing diagrams."""
    config = Settings()
    result = get_missing_active(config, {"n_vars_with_missing": 5})
    assert "bar" in result
    assert "matrix" in result
    assert "heatmap" in result


def test_get_missing_diagram():
    """Test getting missing diagrams."""
    config = Settings()
    df = pd.DataFrame({
        "A": [1, 2, None, 4, 5]}
    settings = {"name": "bar", "caption": "test", "function": lambda x, y: "test"}
    # Note: This is a placeholder test since the actual implementation is not provided
    pass
