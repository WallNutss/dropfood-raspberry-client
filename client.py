from urllib import response
import requests

#url for http request
url = "https://dropfood-backend.herokuapp.com/dropfood"
urlocal = "http://localhost:5000/dropfood"

# Data in form of Multipart/Form-Data
payload = {
    'status' : 'Halo, disini dari Python Client Server, menyajikan EVA-01',
    'file' : open('evaaa.jpg','rb')  
}

# headers = {
#     'Content-Type' : 'multipart/form-data',
#     'Connection' : 'keep-alive'
# }
response = requests.post(urlocal,files=payload)


print(response.text)