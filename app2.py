import requests

url = "https://bravenewcoin.p.rapidapi.com/ohlcv"

querystring = {"size":"10"}

headers = {
	"Authorization": "Bearer <append token here>",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)