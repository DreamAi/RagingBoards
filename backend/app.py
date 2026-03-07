from flask import Flask
from api.designs import design_api
from api.ecommerce import ecommerce_api
from api.payments import payment_api

app = Flask(__name__)

app.register_blueprint(design_api)
app.register_blueprint(ecommerce_api)
app.register_blueprint(payment_api)

@app.route("/")
def home():
    return {"platform":"Raging Boards AI"}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
  from api.surf_ai_api import surf_ai_api

app.register_blueprint(surf_ai_api)
