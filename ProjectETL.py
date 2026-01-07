import pandas as pd
df = pd.read_csv('UserID.csv')
users_id = df['UserID'].tolist()
print(users_id)
#


import requests
import json

# def get_user(id):
# 	sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'
# 	response = requests.get(f'{sdw2023_api_url}/users/{id}')
# 	return response.json() if response.status_code == 200 else None

# users = [user for id in users_id if (user := get_user(id)) is not None]

users = [
  {
    "id": 4,
    "name": "Pyterson",
    "account": {
      "id": 7,
      "number": "00001-1",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4,
      "number": "**** **** **** 1111",
      "limit": 1000.0
    },
    "features": [],
    "news": [
      {
        "id": 9,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Pyterson, invista hoje para garantir um futuro seguro e pr\u00f3spero. Seu futuro agradece!"
      }
    ]
  },
  {
    "id": 5,
    "name": "Pip",
    "account": {
      "id": 8,
      "number": "00002-2",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 5,
      "number": "**** **** **** 2222",
      "limit": 1000.0
    },
    "features": [],
    "news": [
      {
        "id": 10,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Invista hoje para um futuro seguro e est\u00e1vel, Pip. O seu futuro financeiro depende disso!"
      }
    ]
  },
  {
    "id": 6,
    "name": "Pep",
    "account": {
      "id": 9,
      "number": "00003-3",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 6,
      "number": "**** **** **** 3333",
      "limit": 1000.0
    },
    "features": [],
    "news": [
      {
        "id": 11,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Oi Pep, investir \u00e9 a chave para multiplicar seu dinheiro. N\u00e3o deixe sua grana parada!"
      }
    ]
  }
]


print(json.dumps(users, indent=2))


import openai

openai.api_key = 'openai-token'

def generate_ai_news(user):
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role": "system",
				"content": "Você é um especialista em marketing bancário."
			},
			{
				"role": "system",
				"contente": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)."
			}

	]

)
	return completion.choices[0].message.content.strip('\"')
	

for user in users:
	news = generate_ai_news(user)
	print(News)
	user['news'].append({
		"description": News
		})
	


#

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

def update_user(user):
	response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
	return True if response.status_code == 200 else False 

for user in users:
	success = update_user(user)
	print(f"User {user['name']} updated? {success}!")