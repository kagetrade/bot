# DEAR Systems Sale Order API

## Overview

This API provides an endpoint to retrieve sales order information from DEAR Systems. It allows users to query for sales order details either by order ID or by customer email and name.

## API Endpoint

### Get Sale Order Details

- **Endpoint**: `/app/1/salelist`
- **Method**: `GET`
- **Description**: Retrieves details of a sale order. Users can either provide an order ID to fetch a specific order or provide a customer's email and name to fetch the top sale order associated with that customer.
- **Parameters**:
  - `order_id`: Unique identifier of the sale order. (Optional if email and name are provided)
  - `email`: Email address of the customer. (Required if order_id is not provided)
  - `name`: Name of the customer. (Required if order_id is not provided)
- **Response**: JSON object containing sale order details.
- **Usage**:
  - To fetch sale order by `order_id`: `GET /app/1/salelist?order_id=<order_id>`
  - To fetch sale order by `email` and `name`: `GET /app/1/salelist?order_id=<email>&name=<name>`
- **Example Responses**:
  ```json
  {
    "data": {
      "OrderID": "12345",
      "CustomerName": "John Doe",
      "TotalAmount": 100.00,
      "OrderDate": "2024-01-29"
    },
    "status": True
  }
- **Hosting**: Follow the link https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04