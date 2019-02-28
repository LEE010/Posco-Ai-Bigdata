import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import WineInfo,WineWord
import random
from sklearn.externals import joblib
import pandas as pd

WINE_AGE = {'20':'E','30':'A','40':'D','50':'F'}
WINE_GENDER = {'male':'F','female':'B'}
WINE_JOB = {'student':'E','professional':'E','self-employment':'B',
            'temporary':'D','salary':'E'}
TASTE_DATA = {'A':[2,3,2,3,3,3],'B':[3,1,3,2,1,3],'C':[3,1,3,2,2,2],
              'D':[3,3,3,2,1,1],'E':[3,3,2,1,2,1],'F':[2,3,2,2,2,2],
              'G':[1,3,3,3,2,2],'H':[2,3,2,2,3,3]}

def index(request):
    return render(request,'index.html')

def input_info(request):
    return render(request,'input_info.html')

def recommend(request):
    age = WINE_AGE[request.GET['ageSelect']]
    gender = WINE_GENDER[request.GET['genderSelect']]
    job = WINE_JOB[request.GET['jobSelect']]

    wine_cats = set([age,gender,job])

    wine_list = []

    for type in wine_cats:
        wine_list += list(WineInfo.objects.filter(cat=type))

    res_list = random.sample(wine_list, 5)
    wine_taste = [TASTE_DATA[wine.cat] for wine in res_list]
    wine_words = [random.sample(list(WineWord.objects.filter(type=wine.cat)), 10) for wine in res_list]

    if len(wine_cats) == 0:
        return render(request,'recommend.html')
    else:
        # return render(request,'recommend.html',{'wine_list': res_list,'wine_types':wine_types})
        return render(request,'recommend.html',{'result':zip(res_list,wine_taste,wine_words) })

def input_quality(request):
    return render(request,'input_quality.html')

def result_quality(request):
    spec = ['fixed_acidity','volatile_acidity','citric_acid','residual_sugar',
             'chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density',
             'pH','sulphates','alcohol','quality_category']

    if request.GET['winetype'] == 'red':
        joblib_file = "static/r_joblib_model.pkl"
    else:
        joblib_file = "static/w_joblib_model.pkl"

    joblib_model = joblib.load(joblib_file)
    # print(request.GET)
    # for i in spec:
    #     print(request.GET[i])

    X = {"fixed_acidity": float(request.GET['fixed_acidity']) ,"volatile_acidity":float(request.GET['volatile_acidity']),
         "citric_acid":float(request.GET['citric_acid']),"residual_sugar":float(request.GET['residual_sugar']),
         "chlorides":float(request.GET['chlorides']),"free_sulfur_dioxide":float(request.GET['free_sulfur_dioxide']),
         "total_sulfur_dioxide":float(request.GET['total_sulfur_dioxide']),"density":float(request.GET['density']),
         "pH":float(request.GET['pH']),"sulphates":float(request.GET['sulphates']),"alcohol":float(request.GET['alcohol'])}

    df_X = pd.DataFrame.from_dict([X])

    Y_predict = joblib_model.predict(df_X)

    result = {0:'LOW',1:'MID',2:"HIGH"}

    return render(request,'result_quality.html',{'Y':result[Y_predict[0]],'X':X})

@permission_required('admin.can_add_log_entry')
def wine_upload(request):
    template = "wine_upload.html"

    prompt = {
        'order': "Order of the CSV should name, score, price, cat"
    }

    if request.method == "GET":
        return render(request,template,prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = WineInfo.objects.update_or_create(
            name=column[-4],
            score=round(float(column[-3]),3),
            price=round(float(column[-2]),3),
            cat=column[-1]
        )
    wine = {}
    return render(request, template, wine)

def word_upload(request):
    template = "wine_upload.html"

    prompt = {
        'order': "Order of the CSV should word, time, type"
    }

    if request.method == "GET":
        return render(request,template,prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = WineWord.objects.update_or_create(
            word=column[1],
            time=column[2],
            type=column[3]
        )
    word = {}
    return render(request, template, word)
