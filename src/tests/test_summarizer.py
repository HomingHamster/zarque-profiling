import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.model.summarizer import (
    BaseSummarizer,
    PandasProfilingSummarizer,
    format_summary,
)


def test_format_summary():
    """Test summary formatting."""
    summary = {
        "n": 100,
        "p_missing": 0.1,
    }
    result = format_summary(summary)
    assert "n" in result
    assert result["n"] == 100


def test_base_summarizer():
    """Test base summarizer."""
    from visions import VisionsTypeset
    
    typeset = VisionsTypeset([])
    summarizer = BaseSummarizer(typeset)
    # Test that summarize method exists
    assert hasattr(summarizer, "summarize")


def test_pandas_profiling_summarizer():
    """Test pandas profiling summarizer."""
    from visions import VisionsTypeset
    
    typeset = VisionsTypeset([])
    summarizer = PandasProfilingSummarizer(typeset)
    assert isinstance(summarizer.mapping, dict)
