# pi_thermo
Reads the dht11 sensor on a rasp pi zero and publishes temp and humid to thingspeak.

# Hardware Setup
```
+   dht11 -> pi zero pin 2 
-   dht11 -> pi zero pin 6
out dht11 -> pi zero pin 7 (GPIO 4)
```

# My Channel 
https://thingspeak.com/channels/747083

# Notes:

## Setup thirdparty
```
sudo apt-get update
sudo apt-get install python-pip
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit_DHT
```


## Setting up a service
```
sudo cp pi_thermo.service to /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/pi_thermo.service
sudo systemctl daemon-reload
sudo systemctl enable pi_thermo.service
sudo reboot
```


