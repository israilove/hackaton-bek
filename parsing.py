# import csv 

# import requests

# from bs4 import BeautifulSoup as BS


# url = 'https://www.mashina.kg/'
# response = requests.get(url)



# soup = BS(response.text, 'html.parser')
# cars_ul = soup.find_all('div', class_="col-sm-6 col-md-3 col-lg-3 mb-4")
# car_data = []
# for car in cars_ul:        
#     name = car.find("h4", class_="text-bold text-truncate mb-1").text.strip()
#     price = car.find("div", class_="h6 text-bold mb-2").text.strip()
#     img_url = car.find("img", class_="img-fluid rounded").get("src")
#     description = car.find("div", class_="mb-2 text-multed small text-truncate").text.strip()
#     car_data.append([name, sena, img_url, description_models])
    


# with open("car_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price", "Image URL", "Description"])
#     writer.writerows(car_data)



# def main():
#     all_models_url = 'https://www.mashina.kg/'
#     types = '?types'
    

# main()
    


import csv 
import requests
from bs4 import BeautifulSoup as BS 

data = []
for i in range(1,11):
    URL = f'https://www.mashina.kg/motosearch/all/?page={i}'

    response = requests.get(URL)
    soup = BS(response.text, 'html.parser')
    motos = soup.find_all('div', class_ = 'list-item')

    for moto in motos:
        title = moto.find('h2', class_="name").text
        price = moto.find('p', class_="price").text
        image = moto.find('img').get('data-src')
        description = moto.find('p', class_ = "body-type").text
        motos_info = [title, price, image, description]
        data.append(motos_info)

def sohr_scv(ms):
    with open('motos_kg.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'price', 'image_link', 'description'])
        for row in ms:
            writer.writerow(row)
sohr_scv(data)


