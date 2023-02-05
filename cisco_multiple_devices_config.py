from netmiko import ConnectHandler

sw1 = {
    'device_type': 'cisco_ios',
    'ip': '10.40.0.1',
    'username': 'cisco',
    'password': 'cisco',
}

sw2 = {
    'device_type': 'cisco_ios',
    'ip': '10.40.0.2',
    'username': 'cisco',
    'password': 'cisco',
}

sw3 = {
    'device_type': 'cisco_ios',
    'ip': '10.40.0.3',
    'username': 'cisco',
    'password': 'cisco',
}


all_devices = [sw1, sw2, sw3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name VLAN-99 ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 
