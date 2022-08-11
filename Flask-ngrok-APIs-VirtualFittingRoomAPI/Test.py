import requests
import base64
url = 'http://e88a-35-198-244-100.ngrok.io'

def dress_person(person, cloth):
    imgs = {
        'person_image' : open(f"Input\\{person}", 'rb'),
        'clothing_image' : open(f"Input\\{cloth}", 'rb')
    }
    r = requests.post(url + '/apply', files = imgs)
    with open(f"Output\\{person[:-4] + ' + ' + cloth[:-4]}.png", "wb") as img_file:
        img_file.write(base64.b64decode(bytes(r.json()['result'], 'ascii')))
    print(f"{person} wore {cloth}")
        

persons = ('person.jpg', 'person2.png')
clothes = ('cloth.jpg', 'cloth2.jpg')
for person in persons:
    for cloth in clothes:
        dress_person(person, cloth)
