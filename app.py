from flask import Flask

from api.views import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8001", debug=False)
