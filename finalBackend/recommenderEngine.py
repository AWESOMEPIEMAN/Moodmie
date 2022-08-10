import pandas as pd
import numpy as np
# Now we make the reommendation using Cosine Similarity between the features of the movies 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import os 
from config.definitions import MOVIE_DIR
from config.definitions import REC_DIR





def createRecommender():
                 #recommenderDataFrame = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/recommenderDataset.csv')
                 recommenderDataFrame = pd.read_csv(MOVIE_DIR)
                 termVector = TfidfVectorizer(stop_words='english')
                 matrix = termVector.fit_transform(recommenderDataFrame['comb'])

                 sim = cosine_similarity(matrix)
                 return sim


def getTopRatedMovies():
                 #Movies = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/noDup.csv')
                 Movies = pd.read_csv(REC_DIR)
                 Movies = Movies.sort_values(by='Rating', ascending=False)
                 return Movies.to_json(orient='records')


def getMoviesByEmotion(recommendations,current_emotion):
                #Movies = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/noDup.csv')
                Movies = recommendations
                if(current_emotion == 'Happy'):
                   # if user is happy we filter movies containing: Action,Adventure,Crime
                   # Movies =  Movies.loc[(Movies['Genre1']) == ( ('Action') | (Movies['Genre1']) == ('Adventure') | (Movies['Genre1']) == ('Crime') ) ] 
                   #|  (Movies['Genre2'] == (('Action') |  ('Adventure') |  ('Crime')) ) |  (Movies['Genre3'] == (('Action') |  ('Adventure') |  ('Crime')) ) ]
                   
                   Movies = Movies.loc[((Movies['Genre1'] == 'Action') | (Movies['Genre1'] == 'Adventure')| (Movies['Genre1'] == 'Crime'))] 
                   
                   
                   return Movies.to_json(orient='records')
                
                elif (current_emotion == 'Sad'):
               #     # if user is sad we filter movies containing: Comedy,Romance,Animation
               #     Movies =  Movies.loc[(Movies['Genre1'] == (('Comedy') or ('Romance') or ('Animation')) ) or (Movies['Genre2'] == (('Comedy') or ('Romance') or ('Animation')) ) or (Movies['Genre3'] == (('Comedy') or ('Romance') or ('Animation')) ) ]
                   Movies = Movies.loc[((Movies['Genre1'] == 'Comedy') | (Movies['Genre1'] == 'Romance')| (Movies['Genre1'] == 'Animation'))] 
                   return Movies.to_json(orient='records')

               #    # if user is neurtal we filter movies containing: we dont do any filtering
                elif (current_emotion == 'Neutral'):
                    #Movies =  Movies.loc[(Movies['Genre1'] == (('Action') or ('Adventure') or ('Crime')) ) or (Movies['Genre2'] == (('Action') or ('Adventure') or ('Crime')) ) or (Movies['Genre3'] == (('Action') or ('Adventure') or ('Crime')) ) ]
                    return Movies.to_json(orient='records')
               
               #    # if user is suprised we filter movies containing: Adventure,Fantasy,Horror
                elif (current_emotion == 'Surprise'):
               #     Movies =  Movies.loc[(Movies['Genre1'] == (('Adventure') or ('Fantasy') or ('Horror')) ) or (Movies['Genre2'] == (('Adventure') or ('Fantasy') or ('Horror')) ) or (Movies['Genre3'] == (('Adventure') or ('Fantasy') or ('Horror')) ) ]
                    Movies = Movies.loc[((Movies['Genre1'] == 'Adventure') | (Movies['Genre1'] == 'Fantasy')| (Movies['Genre1'] == 'Horror'))]   
                    return Movies.to_json(orient='records')

               #    # if user is fearful we filter movies containing: Horror,Thriller,Action 
                elif (current_emotion == 'Fear'):
               #     Movies =  Movies.loc[(Movies['Genre1'] == (('Horror') or ('Thriller') or ('Action')) ) or (Movies['Genre2'] == (('Horror') or ('Thriller') or ('Action')) ) or (Movies['Genre3'] == (('Horror') or ('Thriller') or ('Action')) ) ]
                    Movies = Movies.loc[((Movies['Genre1'] == 'Horror') | (Movies['Genre1'] == 'Thriller')| (Movies['Genre1'] == 'Action'))]   
                    return Movies.to_json(orient='records')

               #    # if user is angry we filter movies containing: Comedy,Romance,Thriller
                else:
               #     Movies =  Movies.loc[(Movies['Genre1'] == (('Comedy') or ('Romance') or ('Thriller')) ) or (Movies['Genre2'] == (('Comedy') or ('Romance') or ('Thriller')) ) or (Movies['Genre3'] == (('Comedy') or ('Romance') or ('Thriller')) ) ]
                    Movies = Movies.loc[((Movies['Genre1'] == 'Comedy') | (Movies['Genre1'] == 'Romance')| (Movies['Genre1'] == 'Thriller'))]
                    return Movies.to_json(orient='records')
                   