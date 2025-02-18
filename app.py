import pickle
import numpy as np
import os
import streamlit as st

st.header('Meu primeiro webapp usando Machine Learning')
model = pickle.load(open('artefatos/model.pkl', 'rb'))
book_name = pickle.load(open('artefatos/book_name.pkl', 'rb'))
book_pivot = pickle.load(open('artefatos/book_pivot.pkl', 'rb'))
final_data = pickle.load(open('artefatos/final_data.pkl', 'rb'))

selected_book = st.selectbox(
    'Escolha um livro',
    book_name
)   

def fecth_poster(sugestions):
    book_name = []
    id_book = []
    poster_url = []

    for book_id in sugestions[0]:
        book_name.append(book_pivot.index[book_id])
    
    for name in book_name:
        ids = np.where(final_data['title'] == name)[0][0]
        id_book.append(ids)
    
    for idx in id_book:
        url = final_data.iloc[idx]['image_url']
        poster_url.append(url)
    
    return poster_url

def recomendation(title):
    book_list = []
    book_id = np.where(book_pivot.index == title)[0][0]
    distance, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1, -1), n_neighbors=6)
    poster_url = fecth_poster(suggestions)
    for book_id in suggestions[0]:  # Acessar a primeira linha de sugestões
        book_list.append(book_pivot.index[book_id])
    return book_list, poster_url

if st.button('Mostrar Recomendações'):
    recomendation_books, poster_url = recomendation(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recomendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recomendation_books[2])
        st.image(poster_url[2])
        
    with col3:
        st.text(recomendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recomendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recomendation_books[5])
        st.image(poster_url[5])