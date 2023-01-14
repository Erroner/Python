import requests
from bs4 import BeautifulSoup


morele1_url = requests.get('https://www.morele.net/karta-graficzna-asus-dual-radeon-rx-6600-gaming-oc-8gb-gddr6-dual-rx6600-8g-9603906')
morele1_content = BeautifulSoup(morele1_url.text,'lxml')
morele1_div = morele1_content.find('div', class_='product-box-main')
morele1_price = morele1_div.find('div', class_='product-price').text


morele2_url = requests.get('https://www.morele.net/karta-graficzna-msi-radeon-rx-6600-mech-2x-8gb-gddr6-rx-6600-mech-2x-8g-9295824')
morele2_content = BeautifulSoup(morele2_url.text,'lxml')
morele2_div = morele2_content.find('div', class_='product-box-main')
morele2_price = morele2_div.find('div', class_='product-price').text


morele3_url = requests.get('https://www.morele.net/karta-graficzna-power-color-radeon-rx-6600-hellhound-8gb-gddr6-axrx-6600-8gbd6-3dhl-5949665')
morele3_content = BeautifulSoup(morele3_url.text,'lxml')
morele3_div = morele3_content.find('div', class_='product-box-main')
morele3_price = morele3_div.find('div', class_='product-price').text


morele4_url = requests.get('https://www.morele.net/karta-graficzna-biostar-radeon-rx-6600-xt-8gb-gddr6-va66t6tm81-9495928')
morele4_content = BeautifulSoup(morele4_url.text,'lxml')
morele4_div = morele4_content.find('div', class_='product-box-main')
morele4_price = morele4_div.find('div', class_='product-price').text


morele5_url = requests.get('https://www.morele.net/karta-graficzna-gigabyte-radeon-rx-6600-eagle-8gb-gddr6-gv-r66eagle-8gd-5949643')
morele5_content = BeautifulSoup(morele5_url.text,'lxml')
morele5_div = morele5_content.find('div', class_='product-box-main')
morele5_price = morele5_div.find('div', class_='product-price').text


print(f'ASUS Radeon RX6600 8GB{morele1_price}')
print(f'MSI Radeon RX6600 8GB{morele2_price}')
print(f'PowerColor Radeon RX6600 8GB{morele3_price}')
print(f'Biostar Radeon RX6600 8GB{morele4_price}')
print(f'Gigabyte Radeon RX6600 8GB{morele5_price}')
