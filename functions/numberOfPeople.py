from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import json

subscription_key = "your subscription_key"
endpoint = "your endpoint"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def numberOfPeople(url) :
    remote_image_url_objects = url
    detect_objects_results_remote = computervision_client.detect_objects(remote_image_url_objects)
    
    print("Detecting objects in remote image:")
    if len(detect_objects_results_remote.objects) == 0:
        return(1)
    else:
        n=0
        for object in detect_objects_results_remote.objects:
            print(object.object_property+" / confidence :"+str(object.confidence))
            if object.object_property == "person" :
                n+=1
        with open("config.json") as json_data:
            data_dict = json.load(json_data)
            maximum = data_dict['maximum']
        if n>maximum :
            return(0)
        else :
            return(1)
            
