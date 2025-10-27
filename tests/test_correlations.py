import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.model.correlations import (
    calculate_correlation,
    perform_check_correlation,
    get_active_correlations,
    Auto,
    Pearson,
    Spearman,
    Kendall,
    Cramers,
    PhiK,
)


def test_perform_check_correlation():
    """Test correlation checking."""
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [2, 3, 4, 5, 6],
        "C": [1, 1, 1, 1, 1],
    })
    correlation_matrix = df.corr()
    threshold = 0.9
    result = perform_check_correlation(correlation_matrix, threshold)
    assert isinstance(result, dict)


def test_get_active_correlations():
    """Test getting active correlation types."""
    config = Settings()
    active = get_active_correlations(config)
    assert "auto" in active
