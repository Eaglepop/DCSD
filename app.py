import flask
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import io 
import xgboost
import os




# Use pickle to load in the pre-trained model
model_path = '/Users/isadmin/Desktop/研究所課程/包皮/foreskin_app/model/XGB_infect_1.6.2.pickle'
# model_path = '/Users/isadmin/Desktop/研究所課程/包皮/foreskin_app/model/XGB_infect_1.7.3.pickle'


if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        # Your code to load the model
        model = pickle.load(f)
else:
    print(f"Model file not found at: {model_path}")





# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')




# Set up the main route
@app.route('/', methods=['GET'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
@app.route('/predict', methods=['POST'])
def predict():
    if flask.request.method == 'POST':
        # Extract the input
        Age = flask.request.form['Age']
        Height = flask.request.form['Height']
        Weight = flask.request.form['Weight']
        Penis_length = flask.request.form['Penis_length']
        Phimosis_Grading = flask.request.form['Phimosis_Grading']
        Pain_level_D0 = flask.request.form['Pain_level_D0']
        Pain_level_D1 = flask.request.form['Pain_level_D1']
        
        # Make DataFrame for model
        input_variables = pd.DataFrame([[Age, Height, Weight, 
                                         Penis_length, Phimosis_Grading,
                                         Pain_level_D0, Pain_level_D1]],
                                       columns=['Age', 'Height', 'Weight', 
                                                'Penis_length', 'Phimosis_Grading', 
                                                'Pain_level_D0', 'Pain_level_D1'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        classification = model.predict(input_variables)[0]
        probability = model.predict_proba(input_variables)[0]
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        
        probability=np.array(probability)
        print(probability[1])
        print(classification)
        
        if classification==0:
            return render_template('main.html', 
                                   classification='Not Infected',
                                   probability=probability[1]
                                   )
        else:
            return render_template('main.html', classification='Infected',
                                   probability=probability[1]
                                   )

        
        # return render_template('main.html', 
                            #    if classification==0:
                            #         return render_template('main.html', classification='Not Infected')
                            #    else:
                            #         return render_template('main.html', classification='Infected')

                            
                            # classification=classification,
                            # probability=probability,
                            #   )
                                 
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
                           
                                
                                # probability='{0:.{1}f}'.format(probability[0][1], 2)
                                
                                
                            
                                
                                
                                