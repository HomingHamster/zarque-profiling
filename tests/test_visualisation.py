import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.visualisation.plot import (
    histogram,
    mini_histogram,
    correlation_matrix,
    scatter_complex,
    cat_frequency_plot,
    plot_acf_pacf,
)


def test_histogram():
    """Test histogram generation."""
    config = Settings()
    series = pd.Series([1, 2, 3, 4, 5],
    )
    result = histogram(config, series.values, bins=5)
    assert isinstance(result, str)
    assert len(result) > 0


def test_correlation_matrix():
    """Test correlation matrix plot generation."""
    config = Settings()
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [2, 3, 4, 5, 6],
    })
    result = correlation_matrix(config, df, vmin=-1)
    assert isinstance(result, str)
    assert len(result) > 0


def test_cat_frequency_plot():
    """Test categorical frequency plot generation."""
    config = Settings()
    data = pd.Series([10, 20, 30], index=["cat1", "cat2", "cat3"])
    assert isinstance(result, str)
