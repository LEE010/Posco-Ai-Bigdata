import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import WineInfo,WineWord
import random
from sklearn.externals import joblib

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

def quality(request):
    spec = ['fixed_acidity','volatile_acidity','citric_acid','residual_sugar',
             'chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density',
             'pH','sulphates','alcohol','quality_category']

    # Save to file in the current working directory
    # joblib_file = "r_joblib_model.pkl"
    # joblib.dump(r_pickle_model, joblib_file)

    # Load from file
    r_joblib_model = joblib.load("r_joblib_model.pkl")

    r_train = {"fixed_acidity": [6.3] ,"volatile_acidity":[0.39],"citric_acid":[0.16],"residual_sugar":[1.4],"chlorides":[0.08],"free_sulfur_dioxide":[11],"total_sulfur_dioxide":[23],"density":[0.9955],"pH":[3.34],"sulphates":[0.56],"alcohol":[9.3]}
    type(r_train)
    r_train = pd.DataFrame(r_train)

    # Calculate the accuracy and predictions
    # score = r_joblib_model.score(r_test_x_robust, r_test_y)
    # print("Test score: {0:.2f} %".format(100 * score))
    # Ypredict = r_joblib_model.predict(r_tr_x_robust)
    Y_predict = r_joblib_model.predict(r_train)
    Y_predict
    # Save to file in the current working directory
    # joblib_file = "w_joblib_model.pkl"
    # joblib.dump(w_pickle_model, joblib_file)

    # Load from file
    w_joblib_model = joblib.load("w_joblib_model.pkl")

    w_train = {"fixed_acidity": [7] ,"volatile_acidity":[0.27],"citric_acid":[0.36],"residual_sugar":[20.7],"chlorides":[0.045],"free_sulfur_dioxide":[45],"total_sulfur_dioxide":[170],"density":[1.001],"pH":[3],"sulphates":[0.45],"alcohol":[8.8]}
    type(w_train)
    w_train = pd.DataFrame(w_train)

    # Calculate the accuracy and predictions
    # score = w_joblib_model.score(w_test_x_robust, w_test_y)
    # print("Test score: {0:.2f} %".format(100 * score))
    # Ypredict = w_joblib_model.predict(w_test_x_robust)
    Y_predict = w_joblib_model.predict(w_train)
    Y_predict
    return render(request,'quality.html')

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
