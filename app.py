from flask import Flask
from apis import api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
api.init_app(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    global_limits=["2000 per day", "100 per hour", "2 per second"]
)

app.run(debug=True)