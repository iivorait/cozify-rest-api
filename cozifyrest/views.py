from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Cozify REST API</h2>"
                        "<p><a href='/api/authenticate'>Init authentication</a> (check console after init)</p>"
                        "<p><a href='/api/devices'>List devices</a> (includes states such as temperature)</p>"
                        "<p><a href='/api/device?id=XXX'>Get device data</a> (single device, get the id parameter from the device list)</p>"
                        "<p><a href='/api/device_reachable?id=XXX'>Check if device is reachable</a> (single device, get the id parameter from the device list)</p>"
                        "<p><i>POST /api/device_toggle?id=XXX</i> (toggle device on/off, get the id parameter from the device list)</p>"
                        "<p><i>POST /api/device_on?id=XXX</i> (turn a device on, get the id parameter from the device list)</p>"
                        "<p><i>POST /api/device_off?id=XXX</i> (turn a device off, get the id parameter from the device list)</p>"
                        "<p><i>POST /api/light_temperature?id=XXX&temperature=YYY&transition=ZZZ</i> (adjust light temperature in Kelvins (default 2700), transition length in milliseconds (default 0))</p>"
                        "<p><i>POST /api/light_color?id=XXX&hue=YYY&saturation=ZZZ&transition=AAA</i> (adjust light color, hue in range from 0 to Pi*2, saturation in range from 0.0 to 1.0 (default 1.0))</p>"
                        "<p><i>POST /api/light_brightness?id=XXX&brightness=YYY&transition=ZZZ</i> (adjust light brightness in range from 0.0 to 1.0)</p>"
                        "")