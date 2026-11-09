from flask import Flask, jsonify
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Mi aplicacion en Render modificada</title>
        </head>
        <body>
            <h1>Mi aplicacion funciona!</h1>
            <p>Aplicacion desplegada correctamente en Render.</p>
            <p>Proyecto realizado con Python y Flask.</p>
        </body>
    </html>
    """

@app.route("/status")
def status():
    return jsonify({
        "status": "OK",
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "server_time": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
