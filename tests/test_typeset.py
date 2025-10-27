import pandas as pd
import pytest
from zarque_profiling.config import Settings
from zarque_profiling.model.typeset import ProfilingTypeSet


def test_profiling_typeset():
    """Test profiling typeset initialization."""
    config = Settings()
    typeset = ProfilingTypeSet(config)
    assert typeset.config == config
