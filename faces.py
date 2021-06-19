import requests, json


subscription_key = '5dca5b52d85243cf96516a3ba7bf69aa'
endpoint = "https://centralus.api.cognitive.microsoft.com/"

vision_service_address = endpoint+'face/v1.0/'
constructed_url = vision_service_address +"detect"
def reconocimiento(url):
    parameters={
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,smile,glasses,emotion,hair',
            'recognitionModel': 'recognition_04',
            'returnRecognitionModel': 'true',
            'returnFaceLandmarks': 'true',
            'detectionModel': 'detection_01',
            'faceIdTimeToLive': '86400'
            }

    imagepath="http://gritaradio.com/wp-content/uploads/2019/06/Santana.png"


    headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/json'         
           }

    body= {
            'url':url
            }

    response = requests.post(constructed_url,params=parameters, headers=headers, json=body)

    respuestas = response.json()
    return respuestas

