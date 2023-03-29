from flask import Flask, request, render_template, url_for
import random
# create the app 
app = Flask(__name__)
# configure the MySQL database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost:3306/flask"
# create the extension 
db = SQLAlchemy(app)

class User(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  name = db.Column(db.String(20), nullable=False)
  lastname = db.Column(db.String(20))
  email = db.Column(db.String(100)) 
  # Relations 
  group_id = mapped_column(ForeignKey("group_id"), nullable=True)
  group = relationship("Group", back_populates="users")

class Group(db.Model):
  id: db.Column(db.Integer, primary_key=True)
  name: db.Column(db.String(20), nullable=False)
  users: relationship("User", back_populates="group")

with app.app_context():
  db.create_all()

@app.route("/")
def index():
  users = User.query.all()
  return render_template('index.html', users=users)

@app.route('/new-user')
def new_user():
  return render_template('new-user.html', url=url_for('create_user'))

@app.route('/create-user', methods=['POST'])
def create_user():
  print(request.form)
  if request.method == 'POST':
    user = User(
      username=form_data['username'], 
      name=form_data['name'], 
      lastname=form_data['lastname'],
      email=form_data['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_user/<int:id>')
def delete_user(id):
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/update_user/<int:id>', methods=['POST', 'GET'])
def update_user(id):
  user = User.query.get(id)
  if request.method == 'POST':
    form_data = request.form
    user.username=form_data['username'], 
    user.name=form_data['name'], 
    user.lastname=form_data['lastname'],
    user.email=form_data['email'])
    db.session.commit()
  return render_template('new-user.html', user=user)