
from io import BytesIO
from flask import Flask, json, request, jsonify
import pandas as pd
import numpy as np
import recommenderEngine 
import os 
import cv2 as cv2
from config.definitions import MOVIE_DIR
from config.definitions import REC_DIR
import base64
import emotion

def getRecommendations(sim,data,movieName):
 
    
# check if the movie is in our dataset or not
 if movieName not in data['Movie_Name'].unique():
     print('This movie is not in our database.\nPlease check if you spelled it correct.')

 else:
   # getting the index of the movie in the dataframe
        # m = m.lower()
        i = data.loc[data['Movie_Name']==movieName].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:20]

        # making an empty list that will containg all 10 movie recommendations
        l = []
        
        column_names = ['Movie_id','Movie_Name','Budget','Language','Revenue','Image','Rating','Genre1','Genre2','Genre3','Cast1','Cast2','Cast3']
        
        df = pd.DataFrame(columns = column_names)
        
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['Movie_Name'][a])
        
         
        #Movies = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/noDup.csv')
        
        Movies = pd.read_csv(REC_DIR)
        
        for i in range(len(l)):
            a = l[i]
            newVal = Movies.loc[Movies['Movie_Name'] == a]
            df = df.append(newVal, ignore_index=True)    
        return df.to_json(orient='records') 


def getRecommendationsForEmotion(sim,data,movieName,current_emotion):
 
    
# check if the movie is in our dataset or not
 if movieName not in data['Movie_Name'].unique():
     print('This movie is not in our database.\nPlease check if you spelled it correct.')

 else:
   # getting the index of the movie in the dataframe
        # m = m.lower()
        i = data.loc[data['Movie_Name']==movieName].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:400]

        # making an empty list that will containg all 10 movie recommendations
        l = []
        
        column_names = ['Movie_id','Movie_Name','Budget','Language','Revenue','Image','Rating','Genre1','Genre2','Genre3','Cast1','Cast2','Cast3']
        
        df = pd.DataFrame(columns = column_names)
        
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['Movie_Name'][a])
        
         
        #Movies = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/noDup.csv')
        
        Movies = pd.read_csv(REC_DIR)
        
        for i in range(len(l)):
            a = l[i]
            newVal = Movies.loc[Movies['Movie_Name'] == a]
            df = df.append(newVal, ignore_index=True)    
        
        
        
        return recommenderEngine.getMoviesByEmotion(df,current_emotion)



app = Flask(__name__)

@app.route('/')
def homepage():
   
    return recommenderEngine.getTopRatedMovies()
    

# This function will just return recommendations without emotional context
@app.route('/get/similar/movies/<movie>')
def similarmovies(movie):
     sim = recommenderEngine.createRecommender()
     #moviesDataset = pd.read_csv('/mnt/c/Users/User/Documents/FYP Submission/Backend/datasets/current/recommenderDataset.csv',on_bad_lines='skip')
     moviesDataset = pd.read_csv((MOVIE_DIR),on_bad_lines='skip')
     
     
     topMovies = getRecommendations(sim,moviesDataset,movie)   
     return topMovies


# This function will filter out the recommendations for a movie based on current emotion of user
@app.route('/get/emotional/recommendations',methods=["POST"])
def getEmotionRecommendations():
    movie_name = request.form["movie_name"]
    current_emotion = request.form["current_emotion"]
    sim = recommenderEngine.createRecommender()
    moviesDataset = pd.read_csv((MOVIE_DIR),on_bad_lines='skip')
    return getRecommendationsForEmotion(sim,moviesDataset,movie_name,current_emotion)


# This creates a image file and returns Success
@app.route('/test',methods=["POST"])
def test():
    _test = request.form["imagebase"]
    print(type(_test))
    print(_test)
    base64_data = _test.split(",")
    image_data = base64.b64decode(base64_data[0])
    image_np = np.fromstring(image_data,dtype=np.uint8)
    img = cv2.imdecode(image_np,flags=cv2.IMREAD_COLOR)
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite("user_emotion.jpg",img)
    return "Success"

@app.route('/cnn')
def cnn():
    return emotion.getEmotion()


# @app.route('/genre/<id>')
# def getmoviesGenre(id):
#     return recommenderEngine.getMoviesByGenre(id)

if __name__ =="__main__":
    app.run(host = "172.20.0.240",port=39444)

