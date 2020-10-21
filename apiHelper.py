import requests
import json


class HueHandler:
    # Define General Endpoints
    _httpURL = "http://"
    _bridgeIpAddress = "192.168.0.105/"
    _apiUrl = "api/"
    _uniqueID = "r7IZ3QF7VaEMgSp2P2iRaZYWhb28nbEwoOfwQueO/"
    _baseURL = _httpURL + _bridgeIpAddress + _apiUrl + _uniqueID

    # Define Lights Endpoint
    _lightsURL = _baseURL + "lights/"

    # Define Motion Sensor Endpoint
    _motionSensorURL = _baseURL + "sensors/10"

    # Define Lights
    BR1 = 2
    BR2 = 4
    LR1 = 1
    LR2 = 3

    def turn_on_light(self, light_id):
        url = self._lightsURL + str(light_id) + "/state"
        payload = json.dumps({"on": True})
        return requests.put(url, payload)

    def turn_off_light(self, light_id):
        url = self._lightsURL + str(light_id) + "/state"
        payload = json.dumps({"on": False})
        return requests.put(url, payload)

    def turn_off_bedroom_lights(self):
        self.turn_off_light(self.BR1)
        self.turn_off_light(self.BR2)

    def turn_on_bedroom_lights(self):
        self.turn_on_light(self.BR1)
        self.turn_on_light(self.BR2)

    def turn_off_motion_sensor(self):
        url = self._motionSensorURL + "/config"
        payload = json.dumps({"on": False})
        return requests.put(url, payload)

    def turn_on_motion_sensor(self):
        url = self._motionSensorURL + "/config"
        payload = json.dumps({"on": True})
        return requests.put(url, payload)
