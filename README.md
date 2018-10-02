IBM-Call-for-Code-Hackaton-

# Home-PI

![Screenshot](https://github.com/genesisrrios/IBM-Call-for-Code-Hackaton-/blob/master/other/Screen%20Shot%202018-09-28%20at%208.54.57%20PM.png)

The raspberry pi that will be in the houses will run the server.py which is in charge of sending the Data of the sensors to the PI-Drone. For this to work as a hotspot we must make the following configurations in our pi link: https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/

Run server.py

# Home-Arduino

The Arduino will also be placed in the houses and it will be running "Arduino Code.ino" which will be compiled using the Arduino IDE. This code is used to store the data that the sensors attached collect, these sensors are a Fire Detector, Temperature, Gas Sensor. We plan on adding more sensors to this project and storing the data on a csv which will be sent to the ibm cloud to be analyzed. 
The DHT 11 Sensor is connected to the Digital Pin 11, the fire detecting sensor is connected to the Analog Pin 0.


# Drone-PI

![Screenshot](https://github.com/genesisrrios/IBM-Call-for-Code-Hackaton-/blob/master/other/Zoe1.jpg)

This raspberry pi is responsible for running the script datahunter.py which will be waiting to connect to a server to receive the data in a csv file. Once we have all the collected data, we process it to send it to the cloud with the Proces.py script.

For search Data run datahunter.py

to process the data run Proces.py

