IBM-Call-for-Code-Hackaton-

# Home-PI

![Screenshot] ()

In the PI that will be in the houses will be running the server.py which is in charge of sending the Data of the sensors to the PI-Drone. For this to work as a hotspot we must make the following configurations in our pi link: https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/

Run server.py



# Drone-PI

This is laraspberry pi which is responsible for running the script datahunter.py which will be waiting to connect to a server to receive the data in a csv file. Once we have all the collected data, we process it to send it to the cloud with the Proces.py script.
