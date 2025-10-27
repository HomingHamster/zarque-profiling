import pandas as pd
import pytest
from zarque_profiling.profile_report import ProfileReport


def test_profile_report_creation():
    """Test basic profile report creation."""
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": ["x", "y", "z", "x", "y"]
    })
    
    # Test with pandas DataFrame
    report = ProfileReport(df)
    assert report.df is not None
    assert report.config is not None


def test_profile_report_to_html():
    """Test HTML report generation."""
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": ["x", "y", "z", "x", "y"]
    })
    
    report = ProfileReport(df)
    html = report.to_html()
    assert isinstance(html, str)
    assert len(html) > 0


def test_profile_report_to_json():
    """Test JSON report generation."""
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": ["x", "y", "z", "x", "y"]
    })
    
    report = ProfileReport(df)
    json_str = report.to_json()
    assert isinstance(json_str, str)
    assert len(json_str) > 0


def test_profile_report_compare():
    """Test report comparison."""
    df1 = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": ["x", "y", "z", "x", "y"]
    })
    
    report1 = ProfileReport(df1)
    report2 = ProfileReport(df1)  # Same data for simplicity
    comparison = report1.compare(report2)
    assert comparison is not None
