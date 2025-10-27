import pytest
from zarque_profiling.config import Settings, PolarsSettings, Config


def test_settings_default():
    """Test that default settings are loaded correctly."""
    settings = Settings()
    assert settings.title == "ZarQUE Profiling Report"
    assert settings.vars.num.skewness_threshold == 20
    assert settings.vars.cat.cardinality_threshold == 50
    assert settings.vars.bool.imbalance_threshold == 0.5


def test_polars_settings():
    """Test Polars-specific settings."""
    settings = PolarsSettings()
    assert settings.correlations["auto"].calculate is True
    assert settings.correlations["pearson"].calculate is False


def test_settings_from_file(tmp_path):
    """Test loading settings from a YAML file."""
    config_file = tmp_path / "config.yaml"
    config_file.write_text("title: Custom Title")
    
    settings = Settings.from_file(config_file)
    assert settings.title == "Custom Title"


def test_settings_update():
    """Test updating settings."""
    settings = Settings()
    updated = settings.update({"title": "Updated Title"})
    assert updated.title == "Updated Title"


def test_config_shorthands():
    """Test config shorthand processing."""
    kwargs = {"minimal": True}
    shorthand_args, _ = Config.shorthands(kwargs, split=True)
    assert "minimal" in shorthand_args


def test_config_arg_groups():
    """Test config argument groups."""
    kwargs = Config.get_arg_groups("sensitive")
    assert "samples" in kwargs
    assert kwargs["samples"] is None
