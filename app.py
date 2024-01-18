from flask import Flask, render_template,jsonify,request
from backend import (
    get_suggested_funds,
)
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# @app.route("/",methods=['POST'])
# def index():
#     fund_codes_to_search = request.get_json()
#     # fund_codes_to_search =["BMO97334", "HMUS.U", "BMO97325", "PFC6611"]

#     suggested_funds_result = get_suggested_funds(
#         "api/static/Funds.xlsx", fund_codes_to_search
#     )
#     return jsonify(suggested_funds_result)
    # return render_template("index.html", suggested_funds=suggested_funds_result)

@app.route("/")
def index():
    # fund_codes_to_search = request.get_json()
    # fund_codes_to_search =["BMO97334", "HMUS.U", "BMO97325", "PFC6611"]

    # suggested_funds_result = get_suggested_funds(
    #     "static/Funds.xlsx", fund_codes_to_search
    # )
    # return jsonify(suggested_funds_result)
    return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)
