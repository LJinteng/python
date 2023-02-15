import requests
from bs4 import BeautifulSoup
import csv

url = 'https://dealer.autohome.com.cn/shandong/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

provinces = soup.find('div', {'class': 'province'})
print(provinces)
# province_tags = provinces.find_all('a')
#
# with open('car_dealers.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['省份', '城市', '商家类型', '商家名称', '商家地址', '在售车源'])
#
#     for province_tag in province_tags:
#         province_name = province_tag.text  # 省份名称
#         province_url = province_tag['href']  # 省份链接
#
#         response = requests.get(province_url)
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')
#
#         cities = soup.find('div', {'class': 'city'})
#         city_tags = cities.find_all('a')
#
#         for city_tag in city_tags:
#             city_name = city_tag.text  # 城市名称
#             city_url = city_tag['href']  # 城市链接
#
#             response = requests.get(city_url)
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
#
#             dealer_types = soup.find('div', {'class': 'dealer-types'})
#             dealer_type_tags = dealer_types.find_all('a')
#
#             for dealer_type_tag in dealer_type_tags:
#                 dealer_type = dealer_type_tag.text  # 商家类型
#                 dealer_type_url = dealer_type_tag['href']  # 商家类型链接
#
#                 response = requests.get(dealer_type_url)
#                 html = response.text
#                 soup = BeautifulSoup(html, 'html.parser')
#
#                 dealers = soup.find('div', {'class': 'dealer-list'})
#                 dealer_tags = dealers.find_all('div', {'class': 'dealer-item'})
#
#                 for dealer_tag in dealer_tags:
#                     dealer_name = dealer_tag.find('h4').text  # 商家名称
#                     dealer_address = dealer_tag.find('p', {'class': 'address'}).text  # 商家地址
#                     on_sale_cars = dealer_tag.find('div', {'class': 'on-sale-car'}).text  # 在售车源
#
#                     writer.writerow([province_name, city_name, dealer_type, dealer_name, dealer_address, on_sale_cars])
