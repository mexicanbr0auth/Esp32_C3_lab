
import network
import time

class Wifi:
    def __init__(self):
        self.connection = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)

    def wifi(self):
        print("WIFI CENTER")
        print("ACTIVATING WIFI...")
        self.connection.active(True)
        time.sleep(1)
        print("WIFI ON")

    def scan(self):
        print("SCANNING NETWORKS...")
        rede = self.connection.scan()

        for redes in rede:
            ssid = redes[0].decode("utf-8")
            bssid = redes[1]
            canal = redes[2]
            rssi = redes[3]
            seguranca = redes[4]

            print(f"""
------------------
NOME: {ssid}
BSSID: {bssid}
CANAL: {canal}
RSSI: {rssi} dBm
SEGURANCA: {seguranca}
------------------
""")
  
    def route(self, name, passwd):

        self.ap.active(True)
        self.ap.config(
               essid=name,
               password=passwd
               )
        print(f"IP: {self.ap.ifconfig()}")
       


