from flask import Flask, request, jsonify,Response,send_from_directory
import mysec
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = mysec.API_AUTH_APPLICATION_KEY
acc_id = mysec.API_AUTH_ACCOUNT_ID
headers = {
    'api-auth-accountid': acc_id,
    'api-auth-applicationkey': api_key,
    'Content-Type': 'application/json'
}

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


@app.route("/app/1/get_top_sale_order_by_email", methods=['GET'])
def get_top_sale_order_by_email():
    try:
        email = request.args.get('email')
        name = request.args.get('name')
        if not email:
            return jsonify({"error": "Email is required"}), 400

        customer_list_url = f"https://inventory.dearsystems.com/ExternalApi/v2/customer?Name={name}"
        customer_response = requests.get(customer_list_url, headers=headers)
        if customer_response.status_code != 200:
            return jsonify({"error": "Failed to fetch customer data"}), 500

        customers = customer_response.json().get('CustomerList', [])
        
        customer_id = next((customer['ID'] for customer in customers 
                            for contact in customer.get('Contacts', []) 
                            if contact['Email'] == email), None)

        if not customer_id:
            return jsonify({"error": "Customer not found"}), 404

        sale_list_url = f"https://inventory.dearsystems.com/ExternalApi/v2/saleList?CustomerID={customer_id}"
        sale_response = requests.get(sale_list_url, headers=headers)
        if sale_response.status_code != 200:
            return jsonify({"error": "Failed to fetch sale orders"}), 500

        sales = sale_response.json().get('SaleList', [])
        if not sales:
            return jsonify({"error": "No sale orders found for this customer"}), 404

        top_sale_order = sales[0]
        return jsonify(top_sale_order)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)