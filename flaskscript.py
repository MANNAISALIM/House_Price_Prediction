from flask import Flask, render_template, request
import pickle
import numpy as np

with open('models/LinearRegression.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def home():
    longitude = float(request.form['input-1'])
    latitude =  float(request.form['input-2'])
    housing_median_age =  float(request.form['input-3'])
    total_room =  float(request.form['input-4'])
    total_bedrooms =  float(request.form['input-5'])
    population =  float(request.form['input-6'])
    households =  float(request.form['input-7'])
    median_income =  float(request.form['input-8'])
    bedrooms_per_room = float(request.form['input-9'])
    population_per_household =  float(request.form['input-10'])
    if ( (request.form['input-11']) == 1 ):
        ocean_proximity1 =  1.0
        ocean_proximity2 =  0.0
        ocean_proximity3 =  0.0
        ocean_proximity4 =  0.0
        ocean_proximity5 =  0.0
    elif ((request.form['input-11']) == 2):
        ocean_proximity1 =  0.0
        ocean_proximity2 =  1.0
        ocean_proximity3 =  0.0
        ocean_proximity4 =  0.0
        ocean_proximity5 =  0.0
    elif ((request.form['input-11']) == 3):
        ocean_proximity1 =  0.0
        ocean_proximity2 =  0.0
        ocean_proximity3 =  1.0
        ocean_proximity4 =  0.0
        ocean_proximity5 =  0.0
    elif ((request.form['input-11']) == 4):
        ocean_proximity1 =  0.0
        ocean_proximity2 =  0.0
        ocean_proximity3 =  0.0
        ocean_proximity4 =  1.0
        ocean_proximity5 =  0.0
    else:
        ocean_proximity1 =  0.0
        ocean_proximity2 =  0.0
        ocean_proximity3 =  0.0
        ocean_proximity4 =  0.0
        ocean_proximity5 =  1.0
    
        
        
    
    arr = np.array([[longitude,latitude,housing_median_age,total_room,total_bedrooms,population,households,median_income,bedrooms_per_room,population_per_household,ocean_proximity1,ocean_proximity2,ocean_proximity3,ocean_proximity4,ocean_proximity5]])
    pred = model.predict(arr)

    data = round(pred[0], 2)
    return render_template('after.html', prediction_text='$ {}'.format(data))
if __name__ == "__main__":
    app.run()
