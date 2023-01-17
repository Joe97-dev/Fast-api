#We import the various necessary libraries
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pandas as pd
import pickle


#Create the app object
app = FastAPI()
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)


#Trace/Index the route
@app.get('/')
def index():
    return {'Message':'Hello,buddy! Welcome!'}


#Route with a single parameter
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Joe Kazungu Page': f'{name}'}

#Expose the prediction functionaly
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()
    print(data)
    #print('Hey')
    variance = data['variance']
    print(variance)
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    #print(classifier.predict([[variance, skewness, curtosis, entropy]])
    print('Hello')
    prediction = classifer.predict([[variance, skewness, curtosis, entropy]])
    if (prediction [0] > 0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'It is a bank Note'
    return {
        'prediction' : prediction
    }

#Run the API with uvicorn

if __name__ =="__main__":
    uvicorn.run(app, host = '127.0.0.1', port =8000)

