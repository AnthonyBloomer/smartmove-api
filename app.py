from flask import Flask
from apis import blueprint as api
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "/api/v1"
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

limiter = Limiter(
    app,
    key_func=get_remote_address,
    global_limits=["2000 per day", "100 per hour"]
)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.register_blueprint(api, url_prefix='/api/v1')
    app.run(debug=True, host='0.0.0.0', port=port)
