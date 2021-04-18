'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from modules.ignition import *
from modules.dataFetcher import *
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
ledRed = 19

#initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   

# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)

hx = 4

@app.route("/")
def index():
	# Read GPIO Status
	ledRedSts = GPIO.input(ledRed)

	templateData = {
      'ledRed'  : ledRedSts,
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
   
	if action == "on":
		t1 = Ignition(actuator)
		t1.start()
		data = FetchData(hx)
		data.start()
		t1.stop()

	if deviceName == 'stopData':
		data.stop()
		
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
   
	templateData = {
      'ledRed'  : ledRedSts,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
