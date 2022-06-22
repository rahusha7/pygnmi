

from pygnmi.client import gNMIclient,telemetryParser
import pprint
import json


router = {
		"ip_address":"10.30.111.171",
		"port":57777,
		"username":"cisco",
		"password":"cisco123!"
		}

if __name__ == '__main__':
	

	### subscription function in gNMI

	subscribe_request = {

		'subscription':[
			{
				'path':'openconfig-interfaces:interfaces/interface[name=Loopback0]',
				'mode':'sample',
				'sample_interval':10000000000
			},
			{
				'path':'Cisco-IOS-XR-rsi-agent-oper:rsi-agent/nodes/',
				'mode':'sample',
				'sample_interval':10000000000
			}
		],
		'mode':'stream',
		'encoding':'proto'

	}

	with gNMIclient(target=(router["ip_address"],router["port"]),username=router["username"],password=router["password"],insecure=True) as gc:
		telemetry_stream = gc.subscribe(subscribe=subscribe_request)

		for data in telemetry_stream:
			print(json.dumps((telemetryParser(data)), indent=4))

	

	

	


