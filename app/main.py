
from flask import Flask, jsonify, request
import requests
import datetime

app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        data = response.json()
        return data.get('origin')
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

@app.route('/')
def get_info():
    current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = get_public_ip() or request.remote_addr
    return jsonify({"datetime": current_date_time, "ip": ip_address})

if __name__ == '__main__':
    app.run()
