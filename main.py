import requests
# #keepingitbasic

tokenURL = 'https://opentdb.com/api_token.php?command=request' #avoiding repeat questions
tokenData = requests.get(url=tokenURL).json() #token to keep us 'logged in'
token = tokenData['token'] #token to keep us 'logged in'

parameters = {
    'amount': 1,
    'category': 9,
    'difficulty': 'easy',
    'type': 'multiple',
    'token': token
}
basicURL = 'https://opentdb.com/api.php'

response = requests.get(url=basicURL, params=parameters) # send a get request to the API  
data = response.json()#convert answer to Json format

print('Here is a trivia question for you')
question = data['results'][0]['question']
answer = data['results'][0]['correct_answer']
incorrect_answer = data['results'][0]['incorrect_answers']

print(question)
print(answer)
