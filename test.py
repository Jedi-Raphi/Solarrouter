import ShellyPy

device = ShellyPy.Shelly("192.168.68.121")

deviceMeter = device.meter(0)   #request meter information
print(deviceMeter['power'])     #print power information
print(deviceMeter['total'])     #print total information