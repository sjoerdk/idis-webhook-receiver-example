"""Listens for POST requests from IDIS
Based on https://trojand.com/simple-webhook-with-flask
"""
from flask import Flask, request
app = Flask(__name__)


@app.route('/webhook', methods=["POST"])
def webhook():
        content = request.get_json(force=True)  # show all data that was received
        print('* Received' + str(content))

        job_id = content["job_id"]              # picking out specific fields
        status = content["status"]
        destination = content["destination_path"]

        print(f'* A job with id {job_id} was completed (status {status})')
        print(f'* Job data was written to "{destination}"')
        return content


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=False)
