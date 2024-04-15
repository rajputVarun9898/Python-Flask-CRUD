# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# # Change the database URI to use 'flask_test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     complete = db.Column(db.Boolean)

# # Create tables inside the application context
# with app.app_context():
#     db.create_all()

# @app.route('/')
# def home():
#     todo_list = Todo.query.all()  # Use Todo.query instead of db.session.query(Todo)
#     return render_template("index.html", todo_list=todo_list)

# @app.route("/add", methods=["POST"])
# def add():
#     title = request.form.get("title")
#     new_todo = Todo(title=title, complete=False)
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("home"))

# @app.route("/update/<int:todo_id>", methods=["GET", "POST"])
# def update(todo_id):
#     if request.method == "POST":
#         todo = Todo.query.get(todo_id)
#         title = request.form.get("title")
#         complete = request.form.get("complete") == "on"
#         todo.title = title
#         todo.complete = complete
#         db.session.commit()
#         return redirect(url_for("home"))
#     else:
#         # Handle GET request
#         todo = Todo.query.get(todo_id)
#         return render_template("update.html", todo=todo)

# @app.route("/delete/<int:todo_id>")
# def delete(todo_id):
#     # Return a template that includes JavaScript confirmation dialog
#     return render_template("confirm_delete.html", todo_id=todo_id)

# # Add a route to handle the delete action after confirmation
# @app.route("/confirm_delete/<int:todo_id>", methods=["POST"])
# def confirm_delete(todo_id):
#     if request.form.get("confirm") == "yes":
#         # Delete the entry
#         todo = Todo.query.get(todo_id)
#         db.session.delete(todo)
#         db.session.commit()
#     return redirect(url_for("home"))

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Change the database URI to use 'flask_test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Create tables inside the application context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    todo_list = Todo.query.all()  # Use Todo.query instead of db.session.query(Todo)
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>", methods=["GET", "POST"])
def update(todo_id):
    if request.method == "POST":
        todo = Todo.query.get(todo_id)
        title = request.form.get("title")
        complete = request.form.get("complete") == "on"
        todo.title = title
        todo.complete = complete
        db.session.commit()
        return redirect(url_for("home"))
    else:
        # Handle GET request
        todo = Todo.query.get(todo_id)
        return render_template("update.html", todo=todo)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Redirect to a confirmation page before deleting
    return redirect(url_for("confirm_delete", todo_id=todo_id))

@app.route("/confirm_delete/<int:todo_id>")
def confirm_delete(todo_id):
    # Render the confirmation page
    return render_template("confirm_delete.html", todo_id=todo_id)

@app.route("/process_delete/<int:todo_id>", methods=["POST"])
def process_delete(todo_id):
    if request.form.get("confirm") == "yes":
        # Delete the entry
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
