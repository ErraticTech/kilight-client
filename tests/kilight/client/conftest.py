import pytest

from kilight.client import DEFAULT_PORT


@pytest.fixture
def kilight_hostname():
    return 'KiLightMono'

@pytest.fixture
def kilight_port():
    return DEFAULT_PORT