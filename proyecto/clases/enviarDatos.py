from time import*
import requests

#puerto_ser=serial.Serial("/dev/ttyACM0",9600)
TOKEN="BBFF-qzcdywLap8XxqMVMKdqrDXb7nlrnzM"
DEVICE_LABEL="PROYECTO"
mojito=0
cubaLibre=0
ronPuro=0
coca=0
sprite=0
naranja=0

payload={
            "mojitos": mojito,
            "cubaLibre": cubaLibre,
            "ron": ronPuro,
            "coca": coca,
            "sprite": sprite,
            "naranja": naranja,
        }
def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def enviar(numero):
    if(numero=='1'):
        global mojito
        mojito+=10
        
        #puerto_ser.write([49])
    if(numero=='2'):
        global cubaLibre
        cubaLibre+=10
        #puerto_ser.write([50])
    if(numero=='3'):
        global ronPuro
        ronPuro+=10
        #puerto_ser.write([51])
    if(numero=='4'):
        global coca
        coca+=10
        #puerto_ser.write([52])
    if(numero=='5'):
        global sprite
        sprite+=10
        
    if(numero=='6'):
        global naranja
        naranja+=10
        
    payload={
            "mojitos": mojito,
            "cubaLibre": cubaLibre,
            "ron": ronPuro,
            "coca": coca,
            "sprite": sprite,
            "naranja": naranja,
        }
    
    post_request(payload)
    
