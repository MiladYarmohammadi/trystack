import pytest

from datetime import datetime

from trystack.util import now


def test_now():
    result = now()
    assert isinstance(result, datetime) is True
    assert hasattr(result, "year") is True
    assert hasattr(result, "month") is True
    assert hasattr(result, "day") is True
    assert hasattr(result, "weekday") is True
    assert hasattr(result, "hour") is True
    assert hasattr(result, "minute") is True
    assert hasattr(result, "second") is True
    assert hasattr(result, "microsecond") is True
    assert result.timestamp() == pytest.approx(datetime.now().timestamp(), 1)
