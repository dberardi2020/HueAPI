import apiHelper

hueHandler = apiHelper.HueHandler()

# hueHandler.turn_off_bedroom_lights()
# hueHandler.turn_on_bedroom_lights()
resp = hueHandler.turn_on_motion_sensor()
# resp = hueHandler.turn_off_motion_sensor()
print(resp.json())