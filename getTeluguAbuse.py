# Source code for responses - Teach Telugu App
import random
def lambda_handler(event, context):
    
    # Event in args is basically the request json object from request generated
    
    abuseIntent = 'AbuseIntent'
    introIntent = 'introduceInTelugu'

    boothulu = ["Bahen-khe lowdey", "Bhaadakow","Erri pooka","Lunjhaa kodaka", "Muunda kodaka","Maa-khe lowdey"]

            
    def getAbuseIntent(boothulu):
        boothu = random.choice(boothulu)
        things_to_say = "Here you go, " + boothu
        return buildresponse(things_to_say)
        
    
    def getIntroIntent():
        things_to_say = '''Naa peru Alexa, Maa mummy peru Sándhyaa Raani. Maa mummy ki iddharu daddys, So I don't know who my daddy is'''
        return buildresponse(things_to_say)
    
        
    def buildresponse(things_to_say):
        response = {
        'version':'1.0',
        'response':{
            'outputSpeech':{
                'type':'PlainText',
                'text': things_to_say
                }
            }
        }
        return response
        
        
    if(event['request']['type'] == 'IntentRequest'):
        
        if event['request']['intent']['name'] == abuseIntent:
            # code abuse intent
            return getAbuseIntent(boothulu)
            
        if event['request']['intent']['name'] == introIntent:
            # code introIntent
            return getIntroIntent()
        
