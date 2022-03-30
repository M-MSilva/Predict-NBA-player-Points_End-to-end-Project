# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:45:06 2022

@author: marquinho
"""


import pickle 
import pandas as pd
import streamlit as st
from preprocessing import CreateCombinedAttributes
from pathlib import Path
import os



current_directory = Path(__file__).parent #Get current directory
file = open(os.path.join(current_directory, 'trained_model.sav'), 'rb') #rb = read bytes because we are reading the file
 
loaded_model = pickle.load(file)


# Web App Title
st.markdown('''
# **Predict Points Of NBA Players**

#### Developed by: Marcos Matheus de Paiva Silva

This is a web app created on Streamlit and hosted on Heroku, whose purpose is to predict a basketball player's points. In this project we deal with a **regression** problem.

**Links:** My [Linkedin](https://www.linkedin.com/in/marcos-matheus-silva-089699b3/) , [GitHub](https://github.com/M-MSilva) e [email](silvamarcosxd@gmail.com)

---
''')



def Predict_Points(input_data):
    
    #predict
    prediction = loaded_model.predict(input_data)

    #show the result
    st.write("%.2f PTS"% (prediction))
    
    
def code():	   

    #fill out form
    form = st.form(key='numbers')        
    MINR	= form.number_input('What is the percentage of team minutes per game used by a player while he was on the court?',key='1')
    MPG	= form.number_input('How many minutes per team game were used by a player?',key='2')
    TOPG = form.number_input('How many turnovers per game does the athlete make?',key='3')
    GP = form.number_input('What was the number of games that an athlete played in his entire career?',key='4')
    USGR = form.number_input('What percentage of team plays used by the athlete while he was on the court?',key='5')
    FTA = form.number_input('what is the number of free throws a player attempts?',key='6')
    P2A = form.number_input('What is the number of 2-point field goals a player attempts in his entire trajectory?',key='7')
    P3A = form.number_input('What is the number of 3-point field goals a player attempts in his entire career?',key='8')
    BPG = form.number_input('How many blockages does the athlete perform per Game?',key='9')
    form.form_submit_button('Add')
   
    #dataset creation
    data = [[MINR,MPG,TOPG,GP,USGR,FTA,P2A,P3A,BPG]]
    columns = ['MIN%','MPG','TOPG','GP','USG%','FTA','2PA','3PA','BPG']
    
    
    #insert
    df = pd.DataFrame(data=data, columns=columns)


    
    #creating a button for prediction
    if st.button('The Points That The Player Will Have Is'):
        Predict_Points(df)
    

if __name__ == '__main__':
    code()				
    



   


				
    
    
    
    
    