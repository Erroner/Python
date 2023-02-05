from netmiko import ConnectHandler 
import getpass

#bezpieczne przekazywanie credsów co by nie hard codować
user = getpass.getpass('Username: ')
password = getpass.getpass('Password: ')

connection = ConnectHandler(
    device_type='cisco_ios',
    host='192.168.0.120',
    username=user,
    password=password,
    secret=password)
connection.enable()

#conf t
connection.config_mode()

#hostname
connection.send_command('hostname CSR1000v')

#create int lo100
connection.send_command('interface loopback100')
connection.send_command('ip address 11.11.11.11 255.255.255.255')
connection.send_command('no shut')
connection.exit_config_mode()

output=connection.send_command('show run | i hostname')
output1 = connection.send_command('show ip interface brief | i Loopback')
output2 = connection.send_command('show ip interface brief | i Gigabit')

print(output)
print(output1)
print(output2)
connection.disconnect()
