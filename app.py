import streamlit as st
import joblib
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fb4a1c91cf5f09bf62f29d9525e63271&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_pics = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id #Poster Fetching

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_pics.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_pics

file_path = 'artifacts/model_trainer/movies.joblib'
movies_dict = joblib.load(open(file_path,'rb'))
movies = pd.DataFrame(movies_dict)

file_path2 = 'artifacts/model_trainer/similarity.joblib'
similarity = joblib.load(open(file_path2,'rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter any movie to get similar movies !',movies['title'].values)

if st.button('Recommend'):
   names,posters =  Recommend(selected_movie_name)

   col1,col2,col3,col4,col5 = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
        st.text(names[2])
        st.image(posters[2])
   with col4:
        st.text(names[3])
        st.image(posters[3])
   with col5:
        st.text(names[4])
        st.image(posters[4])

