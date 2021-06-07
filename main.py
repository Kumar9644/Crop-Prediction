import streamlit as st
from joblib import *
model=load('crop1.ml')

def main():
    st.title('Crop Prediction')
    st.image('cr.jpg',width=600)
    N=st.number_input('Enter Niterogen Number of the soil',step=1)
    st.write(N)
    P=st.number_input('Enter Phosporus Number soil',step=1)
    st.write(P)
    K=st.number_input('Enter Potasium Number soil',step=1)
    st.write(K)
    temp=st.number_input('Enter Temperature',step=1)
    st.write(temp)
    hu=st.number_input('Enter humidity',step=1)
    st.write(hu)
    ph=st.number_input('Enter pH of the soil',step=1)
    st.write(ph)
    rain=st.number_input('Enter rainfall(mm)',step=1)
    st.write(rain)
    b=st.button('Predict Crop')
    if b:
        array=[N,P,K,temp,hu,ph,rain]
        y_pred=model.predict([array])[0]
        st.success(y_pred)










if __name__ == '__main__':
    main()