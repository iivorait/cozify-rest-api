# Cozify REST API

A HTTP REST wrapper for the very good unofficial Cozify Python library https://pypi.org/project/cozify/ / https://github.com/Artanicus/python-cozify .

The idea is that you run this Python Django application on your local server as a proxy/integration for Cozify. You can interact with it using HTTP calls that are sent to Cozify's unpublished API. You can use the HTTP connector of OpenHAB or Home Assistant etc. to interact with this application to control Cozify from your other home automation system.

## Status

Work in progress.

The following methods are implemented:

- Fetch device data including temperature, humidity, motion etc. measurement/status info (device, devices)
- Check if device is reachable (device_reachable)
- Control device power (device_toggle, device_on, device_off)
- Control light color (light_temperature, light_color, light_brightness)

## Usage

### Installation

You need a recent Python3 version

```
pip install virtualenv
python -m venv djangoenv #run in cloned repository

Linux: source djangoenv/bin/activate
Windows: djangoenv\Scripts\activate

pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000 #or "python manage.py runserver" for localhost access only
```

### Calling the API

#### Authenticating

When using the API for the first time, login by calling the following URL, then input email and one time passcode to the console

```
GET /api/authenticate
```

Authentication data is stored on the server in ~/.config/python-cozify/python-cozify.cfg (configurable using the environment variable XDG_CONFIG_HOME)

#### Fetch data

List all devices (includes states such as temperature):

```
GET /api/devices
```

Fetch data from a single device (get the id parameter from the device list):

```
GET /api/device?id=XXX
```

Check if a device is reachable, can react slowly (get the id parameter from the device list):

```
GET /api/device_reachable?id=XXX
```

#### Control devices (such as lights)

Toggle a device on/off (get the id parameter from the device list):

```
POST /api/device_toggle?id=XXX
```

Turn a device on (get the id parameter from the device list):

```
POST /api/device_on?id=XXX
```

Turn a device off (get the id parameter from the device list):

```
POST /api/device_off?id=XXX
```

Adjust light temperature in Kelvins (default 2700), transition length in milliseconds (default 0):

```
POST /api/light_temperature?id=XXX&temperature=YYY&transition=ZZZ
```

Adjust light color, hue in range from 0 to Pi*2, saturation in range from 0.0 to 1.0 (default 1.0):

```
POST /api/light_color?id=XXX&hue=YYY&saturation=ZZZ&transition=AAA
```

Adjust light brightness in range from 0.0 to 1.0:

```
POST /api/light_brightness?id=XXX&brightness=YYY&transition=ZZZ
```

### OpenHAB example configuration

You'll need the HTTP Binding and the JSONPath Transformation addon (https://www.openhab.org/addons/transformations/jsonpath/).

1. Create a new HTTP Binding Thing (HTTP URL Thing)
2. Name the thing as something generic like "Cozify". Set "Base URL" to "http://localhost:8000/api/" (adjust "localhost" to be your server address if not running on the same computer). Under "Show advanced" set the "Command Method" to "POST"
3. Create a new Channel in the HTTP URL thing
4. Name the channel as something descriptive like "LivingroomLight". For a simple on/off device or light select "Channel type" to be "Switch Channel". Set the "State Transformation" to "JSONPATH:$.state.isOn". Under "Show advanced" set "State URL Extension" to "device?id=3e906414-ba28-11e5-a124-68c90bba87d1" (adjust the id for your device) and "Command URL Extension" to "device_toggle?id=3e906414-ba28-11e5-a124-68c90bba87d1" (adjust the id for your device). Set "On Value" to be "true" and "Off Value" to "false"
5. Create a new Item for the channel

You may wish to tweak the HTTP URL Thing's "Refresh Time" setting (defaults to 30 seconds) to be a smaller value if you are using motion sensors for example. That is the rate how often Cozify is being polled for changes - a too small value can also be a bad thing.