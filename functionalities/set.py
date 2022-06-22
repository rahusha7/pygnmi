

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
	
	### set function of gNMI ##TenGigE0/0/0/20

	# ## update

	cisco_update = [
				("openconfig-interfaces:interfaces/interface[name=Loopback1]",
					{
						"config":
						{
							"name":"Loopback1",
							"enabled": False,
							"type": "iana-if-type:softwareLoopback",     ### mandatory filed as per YANG module
							"description":"testing pygnmi to create an interface"
						}

					}
				)

			] 

	
	with gNMIclient(target=(router["ip_address"],router["port"]),username=router["username"],password=router["password"],insecure=True) as gc:
		set_result = gc.set(update=cisco_update,encoding='json_ietf')
		#print(json.dumps(set_result, indent=4))
	
	## delete	
	
	cisco_delete = ['openconfig-interfaces:interfaces/interface[name=Loopback1]']
	

	with gNMIclient(target=(router["ip_address"],router["port"]),username=router["username"],password=router["password"],insecure=True) as gc:
	 	set_result = gc.set(delete=cisco_delete,encoding='json_ietf')
	 	print(set_result)

	







