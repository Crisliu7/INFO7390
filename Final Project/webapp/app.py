from flask import Flask, request, render_template

import pickle
import re
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.models import load_model
from keras import backend as K

rr = pickle.load(open('/mnt/disks/~/rr.sav','wb'))
item_name_le = pickle.load('/mnt/disks/~/item_name_le.sav','wb')
word_vectors = pickle.load(open('/mnt/disks/~/wordvector.sav','wb'))

def rmsle_cust(y_true, y_pred):
    first_log = K.log(K.clip(y_pred, K.epsilon(), None) + 1.)
    second_log = K.log(K.clip(y_true, K.epsilon(), None) + 1.)
    return K.sqrt(K.mean(K.square(first_log - second_log), axis=-1))
nn = load_model('/mnt/disks/~/model2.h5', custom_objects={'rmsle_cust': rmsle_cust})

items = ['missing', 'shirt', 't-shirt', 't shirt', 'pants', \
         'jeans', 'trousers', 'jacket', 'coat', \
         'sweater', 'hat', 'cap', 'dress', 'shorts', \
         'underwear', 'socks', 'blouse', 'shoes', 'boots']
def getItem(text):
    item = 'missing'
    for w in items:
        if re.search(w, text):
            item = w
    return item

colors = ['missing', 'white', 'black', 'pink', 'red', 'green', \
          'blue', 'yellow', 'brown', 'purple', 'violet', 'dark']
def getColor(text):
    color = 'missing'
    for w in colors:
        if re.search(w, text):
            color = w
    return color
def isNew(text):
    match1 = re.search('new', text)
    match2 = re.search('never worn', text)
    if match1:
        flag = 1
    elif match2:
        flag = 1
    else: flag = 0
    return flag
styles = ['missing', 'active','adjustable','affordable','asymmetrical',\
          'beautiful','casual','classic','comfortable',\
          'contemporary','cool','custom','cute','discount',\
          'easy to maintain','eco friendly','elegant','engineered',\
          'environmentally friendly','exciting','exposed','flexible',\
          'formal','half priced','high-waisted','knee length',\
          'knit','layered','lightweight','metallic','modern',\
          'moisture-wicking','old-fashioned','on trend','organic',\
          'oversized','patchwork','patterned','peasant','polished',\
          'pretty','professional','protective','retro',\
          'rocky','romantic','scooped-neck','semi-formal','sexy',\
          'simple','soft','solid','sport','standard','superior',\
          'supersoft','sweetheart','symmetrical','tailored',\
          'textured','trend','unique','vintage','voluminous',
          'water-resistant','waterproof','wear-anywhere','whimsical']

def getStyle(text):
    style = 'missing'
    for w in styles:
        if re.search(w, text):
            style = w
    return style
qualities = ['missing', 'poor','premium','high-quality','low-quality','medium-quality','normal-quality']
def getQuality(text):
    quality = 'missing'
    for w in qualities:
        if re.search(w, text):
            quality = w
    return quality
fabrics = ['missing', 'canvas','chambray','cotton','leather','flax',\
           'full-grain leather','jacquard','jean','jersey',\
           'lace','mesh','moleskin','nylon','organza','oxford',\
           'polyester','silk','top-grain leather']
def getFabric(text):
    fabric = 'missing'
    for w in fabrics:
        if re.search(w, text):
            fabric = w
    return fabric

sizes = ['missing', 'xs','s','m','l','xl','xxl','extra small','small','medium','large','extra large']

def getSize(text):
    size = 0
    for w in sizes:
        if re.search(w, text):
            size = w
    if (size == 'xs') | (size == 'extra small'):
        size = 1
    elif (size == 's') | (size == 'small'):
        size = 2
    elif (size == 'm') | (size == 'medium'):
        size = 3
    elif (size == 'l') | (size == 'large'):
        size = 4
    elif (size == 'xl') | (size == 'extra large'):
        size = 5
    elif size == 'xxl':
        size = 6
    else: size = 0
    return size

fits = ['missing', 'loose','standard-fit','fitted','tight','skinny','skinny-fit']
def getFit(text):
    fit = 'missing'
    for w in fits:
        if re.search(w, text):
            fit = w
    return fit

def getWash(text):
    flag = 'missing'
    match1 = re.search('hand wash', text)
    match2 = re.search('machine wash', text)
    if match1:
        flag = 'hand washable'
    if match2:
        flag = 'machine washable'
    return flag

ages = ['missing', '60s', '70s', '80s', '90s', 'modern']
def age(text):
    flag = 'missing'
    match60 = re.search('60s', text)
    match70 = re.search('70s', text)
    match80 = re.search('80s', text)
    match90 = re.search('90s', text)
    match00 = re.search('modern', text)
    if match60: flag = '60'
    if match70: flag = '70'
    if match80: flag = '80'
    if match90: flag = '90'
    if match00: flag = 'modern'
    return flag

classifier = SentimentIntensityAnalyzer()

def getSentiment(text):
    vs = classifier.polarity_scores(text)
    if vs['compound'] >= 0.5:
        sentiment = 'Positive'
    elif vs['compound'] <= -0.5:
        sentiment = 'Negtive'
    else:
        sentiment = 'Neutral'
    return sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET','POST'])
def signin_form():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    item_name = request.form['item_name']
    brand_name = request.form['brand_name']
    category_name_1 = request.form['category_name_1']
    category_name_2 = request.form['category_name_2']
    category_name_3 = request.form['category_name_3']
    item_condition = request.form['item_condition']
    ship = request.form['ship']
    item_des = request.form['item_des']

    item_name = getItem(item_name)
    color = getColor(item_des)
    isnew = isNew(item_des)
    quality = getQuality(item_des)
    fabric = getFabric(item_des)
    style = getStyle(item_des)
    age = getAge(item_des)
    wash = getWash(item_des)
    fit = getFit(item_des)
    size = getSize(item_des)
    sentiment = getSentiment(item_des)

    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')
    
    # Prediction
    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')

    token_item_des = text_to_word_sequence(item_des)

    vec = np.zeros((1,2))
    for w in token_item_des:
       	try:
           	vec = vec + word_vectors[word_vectors.index==w]
       	except:
           	vec = vec + [0,0]
    
    result = rr.predict(np.array(item_name_en,item_condition,0,ship,0,0,0,vec[0],vec[1]))
    
    return render_template('signin-ok.html', item_name=item_name, brand_name=brand_name, category_name_1= category_name_1, \
          item_condition=item_condition, ship=ship, item_des=item_des)
    # return render_template('form.html', message='Bad username or password', username=username)


@app.route('/example1', methods=['POST'])
def example1():
    item_name = "AVA-VIV Blouse"
    brand_name = "Target"
    category_name = "Women/Tops & Blouses/Blouse"
    item_condition = 1
    ship = 1
    item_des = "Adorable top with a hint of lace and a key hole in the back! The pale pink is a 1X."
    
    # Prediction
    item_name = getItem(item_name)
    color = getColor(item_des)
    isnew = isNew(item_des)
    quality = getQuality(item_des)
    fabric = getFabric(item_des)
    style = getStyle(item_des)
    age = getAge(item_des)
    wash = getWash(item_des)
    fit = getFit(item_des)
    size = getSize(item_des)
    sentiment = getSentiment(item_des)

    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')

    token_item_des = text_to_word_sequence(item_des)
    
    vec = np.zeros((1,2))
    for w in token_item_des:
       	try:
           	vec = vec + word_vectors[word_vectors.index==w]
       	except:
           	vec = vec + [0,0]
    
    result = rr.predict(np.array(item_name_en,item_condition,0,ship,0,0,0,vec[0],vec[1]))

    return render_template('signin-ok.html', item_name=item_name)

@app.route('/example2', methods=['POST'])
def example2():
    item_name = "Black Skater dress"
    brand_name = "Mini rue"
    category_name = "Women/Dresses/Above Knee"
    item_condition = 2
    ship = 0
    item_des = "Xl, great condition."
    
    # Prediction
    item_name = getItem(item_name)
    color = getColor(item_des)
    isnew = isNew(item_des)
    quality = getQuality(item_des)
    fabric = getFabric(item_des)
    style = getStyle(item_des)
    age = getAge(item_des)
    wash = getWash(item_des)
    fit = getFit(item_des)
    size = getSize(item_des)
    sentiment = getSentiment(item_des)

    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')
    
        
    token_item_des = text_to_word_sequence(item_des)
    
    vec = np.zeros((1,2))
    for w in token_item_des:
       	try:
           	vec = vec + word_vectors[word_vectors.index==w]
       	except:
           	vec = vec + [0,0]
    
    result = rr.predict(np.array(item_name_en,item_condition,0,ship,0,0,0,vec[0],vec[1]))
  
    return render_template('signin-ok.html', item_name=item_name, brand_name=brand_name, category_name= category_name, \
          item_condition=item_condition, ship=ship, item_des=item_des)

@app.route('/example3', methods=['POST'])
def example3():
    item_name = "HOLD for Dogs2016 Minnetonka boots"
    brand_name = "UGG Australia"
    category_name = "Women/Shoes/Boots"
    item_condition = 3
    ship = 0
    item_des = "Authentic. Suede fringe boots. Great condition! Size 7. If you are between the sizes 5.5-7 and love wearing thick socks during the winter they'd be perfect for you as well (I did last winter)"

    # Prediction
    item_name = getItem(item_name)
    color = getColor(item_des)
    isnew = isNew(item_des)
    quality = getQuality(item_des)
    fabric = getFabric(item_des)
    style = getStyle(item_des)
    age = getAge(item_des)
    wash = getWash(item_des)
    fit = getFit(item_des)
    size = getSize(item_des)
    sentiment = getSentiment(item_des)

    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')
    
        
    token_item_des = text_to_word_sequence(item_des)
    
    vec = np.zeros((1,2))
    for w in token_item_des:
       	try:
           	vec = vec + word_vectors[word_vectors.index==w]
       	except:
           	vec = vec + [0,0]
    
    result = rr.predict(np.array(item_name_en,item_condition,0,ship,0,0,0,vec[0],vec[1]))
    
    return render_template('signin-ok.html', item_name=item_name, brand_name=brand_name, category_name= category_name, \
          item_condition=item_condition, ship=ship, item_des=item_des)

@app.route('/example4', methods=['POST'])
def example4():
    item_name = "Air Jordan carmine 6s"
    brand_name = "Air Jordan"
    category_name = "Men/Shoes/Athletic"
    item_condition = 3
    ship = 0
    item_des = "They are 100 percent authentic. They are beaters but they still have a lot of life in them. No original box."

    # Prediction
    item_name = getItem(item_name)
    color = getColor(item_des)
    isnew = isNew(item_des)
    quality = getQuality(item_des)
    fabric = getFabric(item_des)
    style = getStyle(item_des)
    age = getAge(item_des)
    wash = getWash(item_des)
    fit = getFit(item_des)
    size = getSize(item_des)
    sentiment = getSentiment(item_des)

    try:
        item_name_en = item_name_le.transform(item_name)
    except:
        item_name_en = item_name_le.transform('missing')
    
        
    token_item_des = text_to_word_sequence(item_des)
    
    vec = np.zeros((1,2))
    for w in token_item_des:
       	try:
           	vec = vec + word_vectors[word_vectors.index==w]
       	except:
           	vec = vec + [0,0]
    
    result = rr.predict(np.array(item_name_en,item_condition,0,ship,0,0,0,vec[0],vec[1]))
  
    return render_template('signin-ok.html', item_name=item_name, brand_name=brand_name, category_name= category_name, \
          item_condition=item_condition, ship=ship, item_des=item_des)

if __name__ == '__main__':
    app.run()