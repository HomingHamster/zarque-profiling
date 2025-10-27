import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.model.alerts import (
    Alert,
    AlertType,
    check_table_alerts,
    check_variable_alerts,
    get_alerts,
    numeric_alerts,
    categorical_alerts,
    boolean_alerts,
    generic_alerts,
    supported_alerts,
    unsupported_alerts,
    alert_value,
    skewness_alert,
)


def test_alert_creation():
    """Test creating alerts."""
    alert = Alert(AlertType.CONSTANT)
    assert alert.alert_type == AlertType.CONSTANT
    assert alert.alert_type_name == "Constant"


def test_check_table_alerts():
    """Test table-level alert checking."""
    table_stats = {"n_duplicates": 5, "n": 100}
    alerts = check_table_alerts(table_stats)
    assert len(alerts) == 1
    assert alerts[0].alert_type == AlertType.DUPLICATES
    alerts = check_table_alerts({"n": 0})
    assert any(alert.alert_type == AlertType.EMPTY for alert in alerts)


def test_numeric_alerts():
    """Test numeric variable alerts."""
    config = Settings()
    summary = {
        "skewness": 25,
        "p_infinite": 0.1,
        "p_zeros": 0.1,
        "chi_squared": {"pvalue": 0.9995},
    }
    alerts = numeric_alerts(config, summary)
    assert len(alerts) == 4  # skewness, infinite, zeros, uniform
    alert_types = {alert.alert_type for alert in alerts}
    expected_types = {AlertType.SKEWED, AlertType.INFINITE, AlertType.ZEROS, AlertType.UNIFORM}
    assert alert_types == expected_types


def test_categorical_alerts():
    """Test categorical variable alerts."""
    config = Settings()
    summary = {
        "n_distinct": 100,
        "chi_squared": {"pvalue": 0.9995},
    }
    alerts = categorical_alerts(config, summary)
    assert len(alerts) == 2  # high cardinality and uniform


def test_boolean_alerts():
    """Test boolean variable alerts."""
    config = Settings()
    summary = {"imbalance": 0.6}
    alerts = boolean_alerts(config, summary)
    assert len(alerts) == 1
    assert alerts[0].alert_type == AlertType.IMBALANCE


def test_alert_value():
    """Test alert value thresholding."""
    assert alert_value(0.02) is True
    assert alert_value(0.001) is False
    assert alert_value(float('nan')) is False


def test_skewness_alert():
    """Test skewness alert detection."""
    assert skewness_alert(25, 20) is True
    assert skewness_alert(15, 20) is False
