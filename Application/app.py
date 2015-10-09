from flask import Flask


app = Flask(__name__)
from couchb import couchb 

app.register_blueprint(couchb, url_prefix='/couchbase')

if __name__ == "__main__":
    app.run()