from boltiot import Bolt
import json
import time
import os

api_key = os.environ['api_key']
device_id = os.environ['device_id']
mybolt = Bolt(api_key, device_id)

i = 0
while i == 0:
    response = mybolt.analogRead("A0")
    data_dict = json.loads(response)
    extracted_value = int(data_dict["value"])
    print("LDR Value=",extracted_value, end='\n')
    time.sleep(10)
    
    if extracted_value < 50:
        mybolt.digitalWrite("0", "HIGH")
        print("LDR Value less than 50,Switchiching on LED ")
    else:
        mybolt.digitalWrite("0", "LOW")
        print("LDR Value greater than 50, Switching off LED ")
        
    print(end='\n')
    time.sleep(10)
