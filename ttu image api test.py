import requests
import json
import os

# searches for sunflower artwork from the museum database -> returns IDs for the art
receive = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers/')
# should print Response 200
print(receive.content)

# iterates through the list of art work and downloads images from the internet
for i in range(40):
    example_img = json.loads(receive.content)['objectIDs'][i]
    img_string = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(example_img)
    image = requests.get(img_string)
    stuff = json.loads(image.content)
    if stuff['primaryImage']:
        image_actual = requests.get(stuff['primaryImage'])
        print(image.content)

        # filepath is currently hard coded but will have to fix that later

        with open(r'C:\Users\choju\Desktop\sunflower.png','wb') as f:
          f.write(image_actual.content)
        os.system(r'C:\Users\choju\Desktop\sunflower.png')
