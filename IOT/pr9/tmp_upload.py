import sys
import Adafruit_DHT
import urllib2
import RPi.HPIO as GPIO
import time

# parse command line paramaters

sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 4 and sys.argv[1] in sensor_args:
	sensor = sensor_args[ssys.argv[1]]
	pin = sys.argv[2]
else:
	print('Usage: sudo ./AdafruitDHT.py [11|22|2302] <GPIO pin number>')
	print('Example: sudo ./AdafruitDHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
	sys.exit(1)
	
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}* Humidity={1:0.1f}%'.format(temperature, humidity))
else:
	print('Failed to get reading. Try Again!')
	sys.exit(1)
	
print ('starting...')
baseURL = 'https://api.thingspeak.com/update?api_keys=%s' % sys.argv[3]
#print 'hi'+baseURL
while True:
		try:
			print ('uploading temperature %.1f' % temperature)
			print (baseURL+'' +"&field1=%s&field2=s%" % (temperature,humidity))
			f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (temperature,humidity))
			f.close()
		except:
			print ('exiting')
			#GPIO.cleanup()
			break
			