"""Constants for the bosch component."""
from homeassistant.const import (
    TEMP_CELSIUS, TEMP_FAHRENHEIT)
import voluptuous as vol
# from bosch_thermostat_http.const import (HC_HEATING_STATUS,
#                                          HC_ROOMTEMPERATURE,
#                                          HC_CURRENT_ROOMSETPOINT,
#                                          OPERATION_MODE, HC_HOLIDAY_MODE,
#                                          DHW_CURRENT_WATERTEMP,
#                                          DHW_OFFTEMP_LEVEL,
#                                          DHW_HIGHTTEMP_LEVEL,
#                                          DHW_CURRENT_SETPOINT)

DOMAIN = "bosch"
ACCESS_KEY = "access_key"
UUID = 'uuid'

GATEWAY = 'gateway'
CLIMATE = 'climate'
SENSOR = 'sensor'
SOLAR = 'solar'
WATER_HEATER = 'water_heater'
VALUE = "value"

SIGNAL_BOSCH = "bosch_signal"
DEFAULT_MIN_TEMP = 0
DEFAULT_MAX_TEMP = 100

SIGNAL_CLIMATE_UPDATE_BOSCH = "bosch_climate_update"
SIGNAL_SENSOR_UPDATE_BOSCH = "bosch_sensor_update"
SIGNAL_DHW_UPDATE_BOSCH = "bosch_dhw_update"
SIGNAL_SOLAR_UPDATE_BOSCH = "bosch_solar_update"
BOSCH_STATE = "bosch_state"

SERVICE_CHARGE_SCHEMA = {vol.Optional(VALUE): vol.In(["start", "stop"])}

SERVICE_CHARGE_START = "set_dhw_charge"


SENSORS = "sensors"
SWITCHPOINT = "switchPoint"
CHARGE = "charge"

UNITS_CONVERTER = {
    'C': TEMP_CELSIUS,
    'F': TEMP_FAHRENHEIT,
    '%': '%',
    'l/min': 'l/min',
    'l/h': 'l/h',
    'kg/l': 'kg/l',
    'mins': 'mins',
    'kW': 'kW',
    'kWh': 'kWh',
    'Wh': 'Wh',
    'Pascal': 'Pascal',
    'bar': 'bar',
    'µA': 'µA',
    ' ': None
}
