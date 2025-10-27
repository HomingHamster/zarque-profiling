import pandas as pd
import pytest


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        "numeric": [1, 2, 3, 4, 5],
    })
