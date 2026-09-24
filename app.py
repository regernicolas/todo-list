from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Deaktiviert die Nachverfolgung von Änderungen
db = SQLAlchemy(app)

#Klasse
class Todo (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all() #Erstellt Tabelle, wenn keine existiert

#Decorator, der eine URL mit einer bestimmten Funktion verknüpft
@app.route("/") #("/") == Homepage
def index():
    todos = Todo.query.all()  #Ruft alle Todo-Einträge aus db ab
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_task():
    todo_text = request.form.get("todo")
    if todo_text:
        new_todo = Todo(task = todo_text)
        db.session.add(new_todo) #fügt neuen Task der db hinzu und speichert ihn ab
        db.session.commit()
    return redirect (url_for("index"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_task(todo_id):
    todo = Todo.query.get_or_404(todo_id) #ruft jedes Klassenobjekt auf und gibt Objekt zurück bzw. 
    db.session.delete(todo)               #erzeugt Fehler 404, wenn nicht gefunden
    db.session.commit() 
    return redirect (url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)