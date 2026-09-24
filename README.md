# Projektdokumentation: Flask To-Do Webapplikation





### 1\. Übersicht und Zielsetzung



Die Anwendung ermöglicht es Benutzern:

* Neue Aufgaben einzutragen und abzuspeichern
* Aufgaben, die bereits erledigt sind, zu löschen
* Eine Übersicht aller gespeicherten Aufgaben anzuzeigen



### 2\. Tech-Stack

|**Komponente**|**Technologie**|**Beschreibung**|
|-|-|-|
|Backend|Python 3.14|Programmiersprache|
|Framework|Flask|Mikro Web-Framework|
|Datenbank|Flask-SQLAlchemy / SQLite|Relationale Datenbank zur persistenten Speicherung|
|Frontend|HTML5 (Jinja2 Templates)|Strukturierung und dynamisches Rendering der Inhalte|
|Styling|CSS3|Optische Gestaltung|





### 3\. Projektstruktur



todo.app/

├── app.py				#Hauptanwendung

├── instance/				#Automatisch erstellt: Enthält todos.db

├── static/

│     └── style.css			#CSS-Datei für das Layout

└── templstes/

&#x20;     └──index.html			#HTML-Template für das Frontend



### 4\. Installation und Inbetriebnahme



**Voraussetzungen:** Installiertes Python 3.8+ auf Ihrem System




##### **Schritt-für-Schritt-Anleitung**


**1. Virtuelle Umgebung erstellen und aktivieren:**
```Bash

\# macOS / Linux

python3 -m venv venv

source venv/bin/activate



\# Windows

python -m venv venv

venv\\Scripts\\activate

```


**2. Abhängigkeiten Installieren:**

```Bash

pip install flask flask-sqlalchemy

```


**3. Anwendung Starten:**

```Bash

python app.py

```


**4. Website aufrufen:**

Öffnen Sie einen Browser und navigieren Sie zu:

\[http://127.0.0.1:5000/](http://127.0.0.1:5000/)



### 5\. Datenbankmodell



Die Speicherung erfolgt relational über SQLAlchemy in einer lokalen SQLite-Datenbank (todos.db)



```Python

class Todo (db.Model):

&#x20;   id = db.Column(db.Integer, primary\_key = True)

&#x20;   task = db.Column(db.String, nullable = False)

```



**Feldbeschreibung:**

* id (Integer, Primary Key): Eindeutiger Identifikator für jeden Eintrag
* task (String(200), nullable = False): Der eingegebene Text der Aufgabe





### 6\. Schnittstellen und Routen



|**Route**|**HTTP-Methode**|**Funktion**|**Beschreibung**|
|-|-|-|-|
|/|GET|index()|Lädt alle Aufgaben aus der Datenbank und rendert index.html|
|/add|POST|add\_task()|Nimmt Daten entgegen und speichert neue Aufgaben in der Datenbank|
|/delete(<int:todo\_id>|POST|delete\_task()|Löscht die Aufgabe mit der passenden id aus der Datenbank|



### 7\. Frontend und Template-Engines



Das Frontend nutzt die JINJA2-Template-Engine zur Generierung des HTML-Codes:



* **Statisches Einbinden**: die CSS-Datei wird via ```url\_for("static", filename = "style.css")``` verknüpft.
* **Schleifen ({% for todo in todos %})**: Iteriert (wird Element für Element durchgegangen) über alle abgerufenen Datensätze aus der Datenbank und rendert sie als Listenelemente (<li>).
* **POST-Formulare**: Jede Aktion (Hinzufügen, Löschen) ist in ein <form method = "POST"> eingebettet, um Daten sicher an den Server zu senden.



### 8\. Sicherheit und Best Practices



* **SQL\_Injection-Schutz** durch die Verwendung des SQLAlchemy-ORMs. Werte werden parametrisiert und direkte SQL-Injections verhindert.
* **404-Fehlerbehandlung** durch Verwendung von Todo.quer.get\_or\_404(todo\_id), um ungültige Aufrufe sauber abzufangen
* **App Context**: Das Anlegen der Datenbanktabellen erfolgt sicher innerhalb des Flask-App-Kontexts (with app.app\_context():)

---------------------------------------------------------------------------------------------------------------

# Project Documentation: Flask To-Do Web Application





### 1\. Overview and Objectives



The application allows users to:

* Enter and save new tasks
* Delete tasks that have already been completed
* View an overview of all saved tasks



### 2. Tech Stack

|**Component**|**Technology**|**Description**|
|-|-|-|
|Backend|Python 3.14|Programming language|
|Framework|Flask|Micro web framework|
|Database|Flask-SQLAlchemy / SQLite|Relational database for persistent storage|
|Frontend|HTML5 (Jinja2 Templates)|Structuring and dynamic rendering of content|
|Styling|CSS3|Visual design|





### 3\. Project Structure



todo.app/
├── app.py				#Main application

├── instance/                #Created automatically: Contains todos.db

├── static/

│   └── style.css            #CSS file for the layout

└── templates/

&#x20;   └── index.html			#HTML template for the front end



### 4. Installation and Setup



**Prerequisites:** Python 3.8+ installed on your system




##### **Step-by-Step Instructions**


**1. Create and activate a virtual environment:**
```Bash

\# macOS / Linux

python3 -m venv venv

source venv/bin/activate



\# Windows

python -m venv venv

venv\\Scripts\\activate

```


**2. Install dependencies:**

```Bash

pip install flask flask-sqlalchemy

```


**3. Run the application:**

```Bash

python app.py

```


**4. Access the website:**

Open a browser and navigate to:

\[http://127.0.0.1:5000/](http://127.0.0.1:5000/)



### 5. Database Model



Data is stored relationally using SQLAlchemy in a local SQLite database (todos.db)



```Python

class Todo (db.Model):

&#x20;   id = db.Column(db.Integer, primary_key = True)

&#x20;   task = db.Column(db.String, nullable = False)

```



**Field Description:**

* id (Integer, Primary Key): Unique identifier for each entry
* task (String(200), nullable = False): The text entered for the task





### 6. Interfaces and Routes



|**Route**|**HTTP Method**|**Function**|**Description**|
|-|-|-|-|
|/|GET|index()|Loads all tasks from the database and renders index.html|
|/add|POST|add_task()|Accepts data and saves new tasks to the database|
|/delete(<int:todo_id>)|POST|delete_task()|Deletes the task with the specified id from the database|



### 7. Frontend and Template Engines



The frontend uses the JINJA2 template engine to generate the HTML code:



* **Static inclusion**: The CSS file is linked via ```url_for(“static”, filename = “style.css”)```.
* **Loops ({% for todo in todos %})**: Iterates (goes through element by element) over all records retrieved from the database and renders them as list items (<li>).
* **POST forms**: Each action (add, delete) is embedded in a <form method="POST"> to securely send data to the server.



### 8. Security and Best Practices



* **SQL Injection Protection** through the use of the SQLAlchemy ORM. Values are parameterized, preventing direct SQL injections.
* **404 Error Handling** by using `Todo.quer.get_or_404(todo_id)` to cleanly handle invalid requests
* **App Context**: Database tables are created securely within the Flask app context (`with app.app_context():`)
