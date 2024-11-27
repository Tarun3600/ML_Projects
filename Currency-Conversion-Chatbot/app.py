from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    # print(source_currency)
    # print(amount)
    # print(target_currency)
    cf = fetch_conversion_factor(source_currency,target_currency)
    final_amt = cf * amount;
    final_amt = round(final_amt,2)
    # print(final_amt)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amt,target_currency)
    }
    return jsonify(response)

def fetch_conversion_factor(source,target):
    url = "https://v6.exchangerate-api.com/v6/211b291410c66abc88ec0099/pair/{}/{}".format(source,target)

    response = requests.get(url)
    response_json = response.json()
    return response_json['conversion_rate']



if __name__ == "__main__":
    app.run(debug=True)
    
