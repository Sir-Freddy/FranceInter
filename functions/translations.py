import requests, uuid, json

subscription_key = "d329c7b7171d4f6e8013e71ad190040a"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "westeurope"

# Fonctionnelle
def translate(text) :
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'fr',
        'to': 'en'
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
