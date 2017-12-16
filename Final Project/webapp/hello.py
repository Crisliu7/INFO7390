from flask import Flask, url_for
from flask import render_template
from flask_wtf import Form 
from wtforms import TextField
from flask import request
from wtforms.validators import DataRequired

from werkzeug import secure_filename
from flask_wtf.file import FileField

app = Flask(__name__)





class PhotoForm(Form):
    photo = FileField('Your photo')

@app.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)

class MyForm(Form):
    name = TextField('name', validators=[DataRequired()])

    

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
      return redirect('/success')
    return render_template('submit.html', form=form)



# class MockCreate(Form):
#     # user_email = StringField("email address",[validators.Email()])
#     api = StringField("api",validators=[DataRequired()])
#     # submit = SubmitField("Submit")
#     code = IntegerField("code example: 200",validators=[DataRequired()])
#     # alias = StringField("alias for api")
#     # data = TextAreaField("json format",[Required()])

# @app.route("/mockservice",methods=['GET','POST'])
# def MockController():
#     form = MockCreate()
#     code = form['code']
#     api = form['api']
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('submit.html', form=form)


# class formCreate(Form) :
  #   item_name = request.form('item_name')
  # brand_name = request.form('brand_name')
  # category_name = request.form('category_name')
  # item_condition = request.form('item_condition')
  # ship = request.form('ship')
  # item_des = request.form('item_des')
  #     model = pickle.load("aaaa")
  # encoded = model.transform(itemname)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

# @app.route('/baselogin',methods=('POST','GET'))
# def baselogin():
#     return render_template('baselogin.html',form=form)

# @app.route('/success')
# def success():
#     return '<h1>Success</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>Item Name: <input name="item_name"></p>
              <p>Brand Name: <input name="brand_name"></p>
              
              <select name="category_name">
              <option value="none">Category Name</option>
              <option value ="Men">Men</option>
              <option value ="Women">Women</option>
              
              </select>              
              
              <select name="item_condition">
              <option value="none">Item Condition</option>
              <option value ="0">0</option>
              <option value ="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              </select>

              <select name="ship">
              <option value="none">Shipping</option>
              <option value ="0">Yes</option>
              <option value ="1">No</option>
              
              </select>              
              <p>Item Description: <input name="item_des" type="textarea"></p>
              

              <p><button type="submit">Submit</button></p>
              </form>'''

@app.route('/success', methods=['POST'])
def success():


  # return '<%item_name %>'


    
  return '<h3>Hello, admin!</h3>'
    # return '<h3>Bad username or password.</h3>'
# # from wtforms import StringField, SubmitField  
# # from wtforms.validators import DataRequired  
# # from flask import jsonify

# app = Flask(__name__)


# # class NameForm(Form):  
# #     name = StringField('What is your name?', validators=[DataRequired()])  
# #     submit = SubmitField('Submit')  


# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   return 'index'
# 	# return render_template("starter.html")
#   #   form = NameForm()  
#   # if form.validate_on_submit():  
#   #   session['name'] = form.name.data  
#   #   return redirect(url_for('index'))  
#   # return render_template('index.html', form=form, name=session.get('name'))  

# # @app.route('/user/<username>')
# # def show_user_profile(username):
# #     # show the user profile for that user
# #     return 'User %s' % username

# # @app.route('/post/<int:post_id>')
# # def show_post(post_id):
# #     # show the post with the given id, the id is an integer
# #     return 'Post %d' % post_id


# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         do_the_login()
# #     else:
# #         show_the_login_form()

# # @app.route('/hello/')
# # @app.route('/hello/<name>')
# # def hello(name=None):
# #     return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()