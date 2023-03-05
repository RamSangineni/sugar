import numpy as np
import  pickle
import streamlit as st
import sklearn 

#loading the model
loaded_model = pickle.load(open('https://github.com/RamSangineni/sugar/blob/main/trained_model.sav','rb' ))

#creating a function for web app

def predict_diabeties(input_data):

    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
      return 'The woman is Not Diabetic'
    else:
      return 'The woman is Diabetic'



def main():
   st.title('Diabeties Predictor in Women')
   st.markdown('Diabetes is a chronic condition in which the body is unable to produce or use insulin effectively, resulting in high blood sugar levels. Diabetes affects women differently than men, particularly during pregnancy and menopause.')
   pregnancies=st.sidebar.number_input('Enter no of Pregnancies ')
   glucose=st.sidebar.number_input('Enter Glucose level')
   bp=st.sidebar.number_input('Enter BloodPressure')
   insulin=st.sidebar.number_input('Enter Insulin level')
   bmi=st.sidebar.number_input('Enter BMI')
   dpf=st.sidebar.number_input('Enter Diabetes Pedigree Function')
   age=st.sidebar.number_input('Enter Age')
   input_data=([pregnancies,glucose,bp,insulin,bmi,dpf,age])
    
    
    import joblib
def predict(input_data):
    clf = joblib.load("trained_model.sav")
    return clf.predict(input_data)
   

   #code for prediction
   diagnosis=' '

   if st.sidebar.button('submit'):
      diagnosis= predict_diabeties(input_data)
      st.success(diagnosis)
    
      st.markdown("Here are some precautions that women with diabetes should take:")

      st.text("1.  Monitor blood sugar levels: It's essential to monitor blood sugar levels regularly to ensure they are within the target range")
      st.text("High or low blood sugar levels can cause several health complications.")
      st.text("2.  Maintain a healthy diet: A healthy diet can help regulate blood sugar levels and prevent complications related to diabetes.")
      st.text(" Women with diabetes should aim to eat a balanced diet that includes whole grains, fruits, vegetables, lean proteins, and healthy fats.")
      st.text("3.  Stay physically active: Regular physical activity can help control blood sugar levels, improve heart health, and reduce stress levels.")
      st.text(" Women with diabetes should aim to engage in moderate-intensity aerobic activity for at least 150 minutes per week.")
      st.text("4. Take medications as prescribed: Medications like insulin and oral hypoglycemic agents can help manage blood sugar levels.")
      st.text("Women with diabetes should take their medications as prescribed by their healthcare provider.")
      st.text("5.  Check feet regularly: Women with diabetes are at higher risk of developing foot problems.")
      st.text("They should check their feet daily for any cuts, blisters, or sores, and report any concerns to their healthcare provider.")
      st.text("6.   Manage stress levels: Stress can affect blood sugar levels and overall health.")
      st.text("Women with diabetes should practice stress management techniques such as deep breathing, yoga, meditation, or mindfulness.")
      st.text("7.  Get regular check-ups: Women with diabetes should have regular check-ups with their healthcare provider to monitor blood sugar levels,")
      st.text("assess any complications, and adjust treatment as necessary.")
      st.text("It's important for women with diabetes to work closely with their healthcare provider to develop a personalized diabetes management plan")
      st.text("that takes into account their unique medical history and lifestyle.")




   

if __name__=='__main__':
   main()

