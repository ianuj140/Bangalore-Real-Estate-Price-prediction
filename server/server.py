from flask import Flask, request, jsonify
import util
app = Flask(__name__)

# create a new file called util, and it will contain all the core routines


@app.route('/predict_home_price', methods=['POST', 'GET'])  # exposes http endpoint
def predict_home_price():
    # when you make http call from the html frontend application, we will get all the inputs in request.form
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    totalsqft = float(request.form['totalsqft'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, totalsqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_location_names', methods=['GET'])  # exposes http endpoint
def get_location_names():
    response = jsonify({'locations': util.get_location_names()
                        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
