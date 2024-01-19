import os
from MoviesRecommendationSystemMLops import logger
import pandas as pd 
from MoviesRecommendationSystemMLops.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 

    
    def validate_all_columns(self)-> bool:
        try:
            validation_status: None

            movies = pd.read_csv(self.config.unzip_movies_dir)
            credits = pd.read_csv(self.config.unzip_credits_dir)
            movies = movies.merge(credits,on='title')
            movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
            movies.dropna(inplace=True)
            import ast #as the genres is in string it just convert it to object
            def convert(obj):
                L = []
                for i in ast.literal_eval(obj):
                    L.append(i['name'])
                return L
            movies['genres'] = movies['genres'].apply(convert)
            movies['keywords'] = movies['keywords'].apply(convert)
            def convert3(obj):
                L = []
                counter = 0
                for i in ast.literal_eval(obj):
                    if counter != 3:
                        L.append(i['name'])
                        counter+=1
                    else:
                     break
                return L
            movies['cast'] = movies['cast'].apply(convert3)
            def fetch_director(obj):
                L = []
                for i in ast.literal_eval(obj):
                    if i['job'] == 'Director':
                        L.append(i['name'])
                        break
                return L
            movies['crew'] = movies['crew'].apply(fetch_director)
            movies['overview'] = movies['overview'].apply(lambda x:x.split())
            movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
            movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
            movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
            movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
            movies['tag'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
            new_df = movies[['movie_id','title','tag']]
            new_df['tag'] = new_df['tag'].apply(lambda x:" ".join(x))
            new_df['tag'] = new_df['tag'].apply(lambda x:x.lower())

            new_df.to_csv(os.path.join(self.config.root_dir, 'data.csv'), index=False)   
            
            data = pd.read_csv('artifacts/data_validation/data.csv')

            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True 
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e 