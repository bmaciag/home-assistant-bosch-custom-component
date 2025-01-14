"""Bosch sensor for Recording sensor in IVT."""

from ..const import SIGNAL_RECORDING_UPDATE_BOSCH
from .base import BoschBaseSensor


class RecordingSensor(BoschBaseSensor):
    """Representation of Recording Sensor."""

    signal = SIGNAL_RECORDING_UPDATE_BOSCH
    _domain_name = "Recording"

    @property
    def device_name(self):
        return "Recording sensors"

    def attrs_write(self, data, **kwargs):
        self._unit_of_measurement = self._bosch_object.unit_of_measurement
        self._attrs = data
        self._attr_last_reset = data.get("last_reset")
        if self._update_init:
            self._update_init = False
            self.async_schedule_update_ha_state()
