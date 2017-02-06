from flask import Flask
from apis import api
import os 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
api.init_app(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    global_limits=["2000 per day", "100 per hour"]
)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507)) 
    app.run(debug=True, host='0.0.0.0', port=port)
