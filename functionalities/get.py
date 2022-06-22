

from pygnmi.client import gNMIclient
import pprint
import json


router = {
		"ip_address":"10.30.111.168",
		"port":57777,
		"username":"cisco",
		"password":"cisco123!"
		}

if __name__ == '__main__':
	
	## get function of gNMI

	# path = ['openconfig-interfaces:interfaces/interface[name=Loopback0]','Cisco-IOS-XR-rsi-agent-oper:rsi-agent/nodes/']
	
	path = ['openconfig-interfaces:interfaces/interface[name=Loopback1]']
	
	with gNMIclient(target=(router["ip_address"],router["port"]),username=router["username"],password=router["password"],insecure=True) as gc:
		get_result = gc.get(path=path,encoding='json_ietf')
		print(json.dumps(get_result, indent=4))		


	