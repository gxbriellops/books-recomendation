import pickle
import numpy as np
import streamlit as st
import pandas as pd
from math import floor

def star_print(star):
    no_star = ' '
    star_moji = '⭐'
    star = star / 2
    star = floor(star)
    if star == 0:
        st.text(no_star)
    else:
        st.text(star_moji * star)

st.set_page_config(
    page_title='ReadNear'
)

st.header('ReadNear - Recomendação de Livros usando Machine Learning 🤖')
model = pickle.load(open('artefatos/model.pkl', 'rb'))
book_name = pickle.load(open('artefatos/book_name.pkl', 'rb'))
book_pivot = pickle.load(open('artefatos/book_pivot.pkl', 'rb'))
final_data = pickle.load(open('artefatos/final_data.pkl', 'rb'))
df = pd.read_csv('archive/final_data.csv')
st.write(' ')

st.header('Recomendações de Livros 📚')

# classicos mais vendidos
five_classics = df[(df['year'] <= 1990) & (df['num_rating'] >= 100) & (df['image_url'].notna()) & (df['image_url'] != ' ')].sort_values(by=['rating', 'num_rating'], ascending=[False, False]).drop_duplicates(subset='title')
five_classics = five_classics.head()

# autores com livros mais publicados
# autores com livros mais publicados
five_most_populars_authors = df.drop_duplicates(subset='title')
five_most_populars_authors = five_most_populars_authors.groupby('author').agg({'title': 'count', 'num_rating': 'sum'}).reset_index()
five_most_populars_authors.rename(columns={'title': 'book_count', 'num_rating': 'total_ratings'}, inplace=True)
five_most_populars_authors = five_most_populars_authors.sort_values(by=['book_count', 'total_ratings'], ascending=[False, False]).head(5)

st.subheader('Os mais vendidos 🏆')

cinco_mais_vendidos = df.sort_values(by=['num_rating', 'rating'], ascending=[False, False]).drop_duplicates(subset='title')

# pega as informações e guardas nas listas
titles = []
urls = []
stars = []
num_ratings = []

for index, row in cinco_mais_vendidos.iterrows():
    book_names = row['title']
    titles.append(book_names)
    url = row['image_url']
    urls.append(url)
    star = row['rating']
    stars.append(star)
    num_rating = row['num_rating']
    num_ratings.append(num_rating)

books_cols = st.columns(5)

# aqui exibe os livros mais vendidos
for i in range(5):
    with books_cols[i]:
        st.image(urls[i], width=300)
        st.text(titles[i])
        star_print(stars[i])
        st.caption(f'{num_ratings[i]} avaliações')

# exibindo os classicos mais vendidos
st.subheader('Os mais avaliados da decada de 90📅')
classicos_cols = st.columns(5)
for i, (index_c, row_c) in enumerate(five_classics.iterrows()):
    with classicos_cols[i]:  # Agora usa `i`, que sempre está dentro do intervalo de 0 a 4
        st.image(row_c['image_url'])
        st.text(row_c['title'])
        star_print(row_c['rating'])
        st.caption(f'{row_c['num_rating']} avaliações')

# exibindo os autores com mais livros
st.subheader('Os 5 autores mais lidos. ✍️')
author_cols = st.columns(5)
for i, (index_a, row_a) in enumerate(five_most_populars_authors.iterrows()):
    with author_cols[i]:
        st.text(f'{row_a['author']} com {row_a['book_count']} e um total de {row_a['total_ratings']} avaliações.')

st.divider()

st.subheader('5 livros recomendados com base em um título 📚')

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
    col_recomdation = st.columns(5)
    for book_rec in range(5):
        with col_recomdation[book_rec]:
            st.image(poster_url[book_rec], width=300)
            st.text(recomendation_books[book_rec])
            book_info = final_data.loc[final_data['title'] == recomendation_books[book_rec]]
            if not book_info.empty:
                star_rec = book_info['rating'].values[0]
                n_avaliacoes_rec = book_info['num_rating'].values[0]
                star_print(star_rec)
                st.caption(f'{n_avaliacoes_rec} avaliações')