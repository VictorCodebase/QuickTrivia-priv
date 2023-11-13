import requests
# #keepingitbasic


token = ""
url = ""
def init():
    global tokenData, token, url
    tokenURL = 'https://opentdb.com/api_token.php?command=request' #avoiding repeat questions
    tokenData = requests.get(url=tokenURL).json() #token to keep us 'logged in'
    token = tokenData['token'] #token to keep us 'logged in'
    url = 'https://opentdb.com/api.php'
    print("conn init")

def fetchQuestions(quantity=1, category=1, difficulty='easy', type='multiple'):
    global tokenData, token
    parameters = {
        'amount': quantity,
        'category': category,
        'difficulty': difficulty,
        'type': type,
        'token': token
    }
    
    response = requests.get(url=url, params=parameters) # send a get request to the API  
    data = response.json()#convert answer to Json format
    print("Questions fetched and returned")
    return data