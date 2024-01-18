from flask import Flask, request, jsonify,Response,send_from_directory
import mysec
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/app/1/salelist', methods=['GET'])
def salelist():
    try:
        order_id = request.args.get('order_id', None)
        headers = {
            'api-auth-applicationkey':mysec.API_AUTH_APPLICATION_KEY,
            'api-auth-accountid': mysec.API_AUTH_ACCOUNT_ID
        } 
        url = f'https://inventory.dearsystems.com/ExternalApi/v2/saleList?Search={order_id}'
        response = requests.request("GET", url, headers=headers).json()
        SaleList = response.get('SaleList')
        top_result = SaleList[0] if SaleList else None
        
        return jsonify({'data': top_result, 'status': True})
    except Exception as e:
        logging.info("Expection raised in salelist %s", e)
        return jsonify({'data': None, 'status': False, 'message': 'Exception'})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)