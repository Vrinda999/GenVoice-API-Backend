from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from routes import get_blueprints


app = Flask(__name__)
CORS(app)

# Configuration for MySQL Connection.
app.config.from_object('config.Config')

# Initialize MySQL
mysql = MySQL(app)

# Register all blueprints
for bp, prefix in get_blueprints():
    app.register_blueprint(bp, url_prefix=prefix)

if __name__ == '__main__':
    app.run(debug=True)