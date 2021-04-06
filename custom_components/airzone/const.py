DOMAIN = "airzone"
DEFAULT_DEVICE_ID = 1
DEFAULT_DEVICE_CLASS = 'innobus'

from homeassistant.components.climate.const import (
    FAN_AUTO,
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    HVAC_MODE_AUTO,
    HVAC_MODE_COOL,
    HVAC_MODE_DRY,
    HVAC_MODE_FAN_ONLY,
    HVAC_MODE_HEAT,
    HVAC_MODE_HEAT_COOL,
    HVAC_MODE_OFF,
    PRESET_NONE,
    SUPPORT_AUX_HEAT,
    SUPPORT_FAN_MODE,
    SUPPORT_PRESET_MODE,
    SUPPORT_TARGET_TEMPERATURE,
)

### Innobus Extra Attributes
ATTR_IS_ZONE_GRID_OPENED = 'is_zone_grid_opened'
ATTR_IS_GRID_MOTOR_ACTIVE = 'is_grid_motor_active'
ATTR_IS_GRID_MOTOR_REQUESTED = 'is_grid_motor_requested'
ATTR_IS_FLOOR_ACTIVE = 'is_floor_active'
ATTR_LOCAL_MODULE_FANCOIL = 'get_local_module_fancoil'
ATTR_IS_REQUESTING_AIR = 'is_requesting_air'
ATTR_IS_OCCUPIED = 'is_occupied'
ATTR_IS_WINDOWS_OPENED = 'is_window_opened'
ATTR_FANCOIL_SPEED = 'get_fancoil_speed'
ATTR_PROPORTIONAL_APERTURE = 'get_proportional_aperture'
ATTR_TACTO_CONNECTED = 'is_tacto_connected_cz'
ATTR_IS_AUTOMATIC_MODE = 'is_automatic_mode'
ATTR_IS_TACTO_ON = 'is_tacto_on'
ATTR_DIF_CURRENT_TEMP = 'get_dif_current_temp'

AVAILABLE_ATTRIBUTES_ZONE = {
    ATTR_IS_ZONE_GRID_OPENED: 'is_zone_grid_opened',
    ATTR_IS_GRID_MOTOR_ACTIVE: 'is_grid_motor_active',
    ATTR_IS_GRID_MOTOR_REQUESTED: 'is_grid_motor_requested',
    ATTR_IS_FLOOR_ACTIVE: 'is_floor_active',
    ATTR_LOCAL_MODULE_FANCOIL: 'get_local_module_fancoil',
    ATTR_IS_REQUESTING_AIR: 'is_requesting_air',
    ATTR_IS_OCCUPIED: 'is_occupied',
    ATTR_IS_WINDOWS_OPENED: 'is_window_opened',
    ATTR_FANCOIL_SPEED: 'get_fancoil_speed',
    ATTR_PROPORTIONAL_APERTURE: 'get_proportional_aperture',
    ATTR_TACTO_CONNECTED: 'is_tacto_connected_cz',
    ATTR_IS_AUTOMATIC_MODE: 'is_automatic_mode',
    ATTR_IS_TACTO_ON: 'is_tacto_on',
    ATTR_DIF_CURRENT_TEMP: 'get_dif_current_temp'
}

ZONE_HVAC_MODES = [HVAC_MODE_AUTO, HVAC_MODE_HEAT_COOL, HVAC_MODE_OFF]
PRESET_SLEEP = 'SLEEP'
ZONE_PRESET_MODES = [PRESET_NONE, PRESET_SLEEP]
ZONE_FAN_MODES = {FAN_AUTO: 'AUTOMATIC', FAN_LOW: 'SPEED_1', FAN_MEDIUM: 'SPEED_2', FAN_HIGH: 'SPEED_3'}
ZONE_FAN_MODES_R = dict(zip(ZONE_FAN_MODES.values(),ZONE_FAN_MODES.keys()))
ZONE_SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE | SUPPORT_PRESET_MODE

MACHINE_HVAC_MODES = [HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_OFF]
PRESET_AIR_MODE = 'AIRE'
PRESET_FLOOR_MODE = 'FLOOR'
MACHINE_PRESET_MODES = [PRESET_AIR_MODE, PRESET_FLOOR_MODE]
MACHINE_SUPPORT_FLAGS = SUPPORT_AUX_HEAT | SUPPORT_PRESET_MODE


AIDO_HVAC_MODES = [HVAC_MODE_AUTO, HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_OFF, HVAC_MODE_DRY]
AIDO_SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE
