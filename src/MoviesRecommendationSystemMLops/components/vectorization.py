import pandas as pd
import os 
from MoviesRecommendationSystemMLops import logger 
import joblib 
from sklearn.feature_extraction.text import CountVectorizer
import nltk 
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from MoviesRecommendationSystemMLops.entity.config_entity import ModelTrainerConfig

class Vectorization:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config 
    
    def train(self):
        data = pd.read_csv(self.config.data_path)
        cv = CountVectorizer(max_features=self.config.max_features,stop_words='english')     
        vectors = cv.fit_transform(data['tag']).toarray()
        ps = PorterStemmer()
        def stem(text):
            y = []
            for i in text.split():
                y.append(ps.stem(i))
    
            return " ".join(y) 
        data['tag'] = data['tag'].apply(stem)

        similarity = cosine_similarity(vectors)
        sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]

        def recommend(movie):
            movie_index = data[data['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
            for i in movies_list:
              print(i)

       

     
        model_path = os.path.join(self.config.root_dir, self.config.movies_model_name)
        joblib.dump(data.to_dict(), open(model_path, 'wb'))

        similarity_path = os.path.join(self.config.root_dir, self.config.similarity_model_name)
        joblib.dump(similarity, open(similarity_path, 'wb'))
