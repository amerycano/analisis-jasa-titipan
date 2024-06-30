import streamlit as st
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Import custom functions from your modules
from create_index import create_index, load_data, find_similar
from hscode_similarity import get_similarity
from price_range import get_range

# Load data
df = load_data('data/cn1.csv')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df[df['HS_CODE'].replace('', np.nan).notna()]

# Define variables for model and vectorizer
model_ident = None
vectorizer_ident = None
model_name = None
vectorizer_name = None
model_address = None
vectorizer_address = None
model_uraian = None
vectorizer_uraian = None

# def main ():
    # Title of the app
st.title('ANALISA JASA TITIPAN')

# A simple text
st.write('Creating a Better CN Through Data')

# Input from user
st.sidebar.title('Similar Importir')
no_ident = st.sidebar.text_input ('NO_IDENTITAS')
nm_penerima = st.sidebar.text_input('NAMA')
al_penerima = st.sidebar.text_input('ALAMAT PENERIMA')
uraian_barang = st.sidebar.text_input('URAIAN BARANG')

# Load data
df = load_data('./data/cn1.csv')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df[df['HS_CODE'].replace('', np.nan).notna()]

# # Function
# ## Mencari Kemiripan Importir
# model_ident, vectorizer_ident, model_name, vectorizer_name, model_address, vectorizer_address, model_uraian, vectorizer_uraian = create_index(df)
# sentence_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
# similar_id = find_similar(no_ident, nm_penerima, al_penerima, df, model_ident, vectorizer_ident, model_name, vectorizer_name, model_address, vectorizer_address)
# similarity_penerima = similar_id[similar_id['Similarity (%)'] > 60].head(10) # get similar_id that Similarity (%) > 0.6   

# ## Mencari kesesuaian HS Code dengan Nama Produk
# df_hs = pd.read_csv('./data/hs_code_not_clean_id.csv', dtype=str)
# df_hs_results = get_similarity(similar_id, sentence_model, df_hs)

# ## Mencari range harga berdasarkan uraian produk
# range_harga = get_range(uraian_barang, df, model_uraian, vectorizer_uraian, sentence_model)
# min_harga = range_harga[0]
# max_harga = range_harga[1]

# Predict button in sidebar
if st.sidebar.button('Predict'):
    model_ident, vectorizer_ident, model_name, vectorizer_name, model_address, vectorizer_address, model_uraian, vectorizer_uraian = create_index(df)
    sentence_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    try:
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

       
# Tabs for additional functionalities
tabs = st.sidebar.radio("Choose an action:", ["Price Range", "HSCode Search"])

if tabs == "Price Range":
    st.subheader("Price Range by Description")
    uraian_barang = st.text_input("Uraian Barang")

    if st.button('Predict Price Range'):
        try:
            if model_uraian is None or vectorizer_uraian is None:
                st.write("Model and vectorizer for description not initialized.")
            else:
                # Initialize model_uraian and vectorizer_uraian for price range prediction
                model_uraian, vectorizer_uraian = model_uraian, vectorizer_uraian
                range_harga = get_range(uraian_barang, df, model_uraian, vectorizer_uraian, sentence_model)
                st.write(f'Harga kisaran min: {range_harga[0]}')
                st.write(f'Harga kisaran max: {range_harga[1]}')
        except Exception as e:
            st.write(f'Error predicting price range: {str(e)}')

elif tabs == "HSCode Search":
    st.subheader("HS Code Search by Description")
    st.write("Insert HS Code search functionality here")
# if __name__ == '__main__':
#     main()


