
import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


REC_DIR = os.path.join(ROOT_DIR, 'datasets/current', 'noDup.csv')
MOVIE_DIR = os.path.join(ROOT_DIR, 'datasets/current', 'recommenderDataset.csv')
CNN_DIR = os.path.join(ROOT_DIR,'models', 'emotion_little_vgg_3.h5')
CV_FRONT_FACE = os.path.join(ROOT_DIR, 'models','haarcascade_frontalface_default.xml')
IMG_SRC = os.path.join(ROOT_DIR, 'user_emotion.jpg')