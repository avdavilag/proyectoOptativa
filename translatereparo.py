import requests, json


subscription_key = '35743f81b19545ce8fff99f1ba26b5c6'
endpoint = "https://southcentralus.api.cognitive.microsoft.com/"

vision_service_address = endpoint+'/vision/v3.2/'
constructed_url = vision_service_address +"ocr"

parameters={
        'language':"es",

        }

imagepath="https://www.galaxcommerce.com.br/sistema/upload/362/editor/files/texto.JPG"


headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/json'
#        'Content-Type': 'application/json'
}

body= {
        'url':imagepath
        }

    # You can pass more than one object in body.
#    body = [{
#        'url' : text_input
#    }]
#    response = requests.post(constructed_url, headers=headers, json=body)
#    return response.json()



response = requests.post(constructed_url,headers=headers, json=body)

result = response.json()
print(result)
#print(json.dumps(result))
