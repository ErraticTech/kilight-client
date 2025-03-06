import logging
import pytest

from kilight.client import Connector, DeviceState, OutputState, OutputIdentifier

pytest_plugins = ('pytest_asyncio',)

LOGGER = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_read_state(kilight_hostname, kilight_port):
    connector = Connector(kilight_hostname, kilight_port)
    state = DeviceState()
    state = await connector.read_state(state)
    LOGGER.debug("Got state: %s", state)


@pytest.mark.asyncio
async def test_read_system_info_and_state(kilight_hostname, kilight_port):
    connector = Connector(kilight_hostname, kilight_port)
    state = DeviceState()
    state = await connector.read_system_info_and_state(state)
    LOGGER.debug("Got full state: %s", state)


@pytest.mark.asyncio
async def test_write_update(kilight_hostname, kilight_port):
    connector = Connector(kilight_hostname, kilight_port)
    state = OutputState(
        red=64,
        green=32,
        blue=16,
        cold_white=48,
        warm_white=10,
        brightness=128,
        power_on=False
    )
    await connector.write_update(OutputIdentifier.OutputA, state)


@pytest.mark.asyncio
async def test_write_update_and_read_state(kilight_hostname, kilight_port):
    connector = Connector(kilight_hostname, kilight_port)
    state = OutputState(
        red=64,
        green=32,
        blue=16,
        cold_white=48,
        warm_white=10,
        brightness=128,
        power_on=False
    )

    device_state = DeviceState()
    device_state = await connector.write_update_and_read_state(device_state, OutputIdentifier.OutputA, state)

    LOGGER.debug("Got updated state: %s", device_state)
