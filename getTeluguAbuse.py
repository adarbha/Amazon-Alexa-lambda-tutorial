import random

boothulu = ["Bahen-khe lowdey", "Bhaadakow","Erri pooka","Lunjhaa kodaka", "Muunda kodaka","Maa-khe lowdey"]



def lambda_handler(event, context):
    boothu = random.choice(boothulu)
    
    response = {
        'version':'1.0',
        'response':{
            'outputSpeech':{
                'type':'PlainText',
                'text': "Here you go, " + boothu
                
            }
        }
    }
    
    return response
