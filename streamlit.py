# -*- coding: utf-8 -*-
"""Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12FmAartar0KjygMJd7AJZonXiHD4XHTE
"""

#pip install streamlit

import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('CN Detection')

# A simple text
st.write('Creating a Better CN Through Data')

# Input from user
st.markdown('Similar Importir')
no_ident = st.number_input ('NO_IDENTITAS')
nm_penerima = st.text_input('NAMA')
al_penerima = st.text_input('ALAMAT PENERIMA')
uraian_barang = st.text_input('URAIAN BARANG')

#Predict button
if st.button('Predict'):
    model = joblib.load('importir_model.pkl')
    X = np.array([no_ident, nm_penerima, al_penerima, uraian_barang])
    if any(len(x.strip()) == 0 for x in X):
      st.markdown('### All inputs must be non-empty and non-whitespace')
    else:
      try:
          # Ensure the input is in the right shape for the model
          input_data = [X]

          # Call the find_similar function
          similar_id = find_similar(no_ident, nm_penerima, al_penerima, df, model_ident, vectorizer_ident, model_name, vectorizer_name, model_address, vectorizer_address)

          # Filter the DataFrame
          filtered_df = similar_id[similar_id['Similarity (%)'] > 60].head(10)

          # Display the filtered DataFrame
          st.markdown(f'### Filtered Similarity Results:')
          st.write(filtered_df)
      except Exception as e:
          st.markdown('### An error occurred during model prediction')
          st.write(str(e))

#Price Range
st.markdown('Price Range by Description')
uraian_barang = st.text_input('Uraian Barang')

