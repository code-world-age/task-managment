from src.___init__ import app

@app.route("/")
def hello():
    return "Heladlo World!"
