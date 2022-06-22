

from pygnmi.client import gNMIclient
import pprint
import json


router = {
		"ip_address":"10.30.111.171",
		"port":57777, 
		"username":"cisco",
		"password":"cisco123!"
		}

if __name__ == '__main__':
	

	### capabilities function of gNMI

	with gNMIclient(target=(router["ip_address"],router["port"]),username=router["username"],password=router["password"],insecure=True) as gc:
		capability_result = gc.capabilities()
	print(json.dumps(capability_result, indent=4))

	







