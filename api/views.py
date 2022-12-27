from django.shortcuts import render
from django.http import HttpResponse
from cozify import hub, cloud
from django.http import JsonResponse

def authenticate(request):
    cloud.authenticate()
    return HttpResponse("Authentication initiated - check console. If no output, you may already be logged in.")

def devices(request):
    cloud.authenticate()
    devices = hub.devices()
    return JsonResponse(devices)

def device(request):
    cloud.authenticate()
    try:
        device = hub.device(request.GET['id'])
        return JsonResponse(device)
    except:
        return HttpResponse("Device not found. Check the id parameter", status=404)

def device_reachable(request):
    cloud.authenticate()
    try:
        device_reachable = hub.device_reachable(request.GET['id'])
        return HttpResponse(device_reachable)
    except:
        return HttpResponse("Device not found. Check the id parameter", status=404)

def device_toggle(request):
    if request.method == "POST":
        cloud.authenticate()
        hub.device_toggle(request.GET['id'])
        return HttpResponse("OK")
    return HttpResponse("Make a POST request to this address with ?id=XXX parameter", status=400)

def device_on(request):
    if request.method == "POST":
        cloud.authenticate()
        hub.device_on(request.GET['id'])
        return HttpResponse("OK")
    return HttpResponse("Make a POST request to this address with ?id=XXX parameter", status=400)

def device_off(request):
    if request.method == "POST":
        cloud.authenticate()
        hub.device_off(request.GET['id'])
        return HttpResponse("OK")
    return HttpResponse("Make a POST request to this address with ?id=XXX parameter", status=400)

def light_temperature(request):
    if request.method == "POST":
        temperature = request.GET.get('temperature', 2700)
        transition = request.GET.get('transition', 0)
        cloud.authenticate()
        try:
            hub.light_temperature(request.GET['id'], int(temperature), int(transition))
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=400)
    return HttpResponse("Make a POST request to this address with ?id=XXX&temperature=YYY&transition=ZZZ parameters", status=400)

def light_color(request):
    if request.method == "POST":
        hue = request.GET.get('hue', 0) #range from 0 to Pi*2
        saturation = request.GET.get('saturation', 1.0)
        transition = request.GET.get('transition', 0)
        cloud.authenticate()
        try:
            hub.light_color(request.GET['id'], float(hue), float(saturation), int(transition))
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=400)
    return HttpResponse("Make a POST request to this address with ?id=XXX&hue=YYY&saturation=ZZZ&transition=AAA parameters", status=400)

def light_brightness(request):
    if request.method == "POST":
        brightness = request.GET.get('brightness', 0) #range from 0 to 1
        transition = request.GET.get('transition', 0)
        cloud.authenticate()
        try:
            hub.light_brightness(request.GET['id'], float(brightness), int(transition))
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=400)
    return HttpResponse("Make a POST request to this address with ?id=XXX&brightness=YYY&transition=ZZZ parameters", status=400)
