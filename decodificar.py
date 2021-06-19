import requests, json
subscription_key = '5dca5b52d85243cf96516a3ba7bf69aa'
endpoint = "https://centralus.api.cognitive.microsoft.com/"

def get_PhotoMessague(imaageUrl):
    vision_service_address = endpoint+'/vision/v3.2/'
    constructed_url = vision_service_address +"ocr"

    parameters={'language':"es"
    }

    imagepath=imaageUrl
    headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/json'
        
            }

    body= {
            'url':imagepath
            }




    response = requests.post(constructed_url,params=parameters,headers=headers, json=body)
    
    response.raise_for_status()
    result = response.json()
    return result
