


    
import socketpool
import ssl
import wifi
import adafruit_requests as requests

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

print ("Connecting...")
wifi.radio.connect ("Panaderia Rokypan 2G", "Roskypan0854")
print ("Connected to wifi...")

URL = "https://ideaboard-proyecto-2.azurewebsites.net/api/IDEA/ getData"

data = https.get(URL).json()

print ("Resultado del GET", data)

URL_POST= "https://ideaboard-proyecto-2.azurewebsites.net/api/IDEA/ postData"

data = {'captura': '7'}
    
result= https.post(URL_POST, json= data)
print("RESULTADO_POST", result.json())

    

