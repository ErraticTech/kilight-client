import logging
import pytest

from kilight.client import OutputIdentifier, Device

pytest_plugins = ('pytest_asyncio',)

LOGGER = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_update_state(kilight_hostname, kilight_port):
    device = Device(kilight_hostname, kilight_port)
    await device.update_state()
    LOGGER.debug("Got state: %s", device.state)


@pytest.mark.asyncio
async def test_multiple_actions(kilight_hostname, kilight_port):
    device = Device(kilight_hostname, kilight_port)
    await device.update_state()
    LOGGER.debug("Got state: %s", device.state)

    await device.update_output_from_parts(OutputIdentifier.OutputA, power=True)
    LOGGER.debug("Wrote output, got state: %s", device.state)

    await device.update_state()

    await device.update_output_from_parts(OutputIdentifier.OutputA, power=False)
    LOGGER.debug("Wrote output, got state: %s", device.state)

    await device.update_state()

    await device.update_output_from_parts(OutputIdentifier.OutputA, power=True)
    LOGGER.debug("Wrote output, got state: %s", device.state)

    await device.update_output_from_parts(OutputIdentifier.OutputA, power=False)
    LOGGER.debug("Wrote output, got state: %s", device.state)

    await device.disconnect()
