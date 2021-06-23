import flask
import datetime
import platform
import os
# import requests

import sys
import logging

_log_level = logging.INFO
logger = logging.getLogger()
logger.setLevel(_log_level)
log_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(log_handler)

app = flask.Flask(__name__)
_port = int(os.environ.get('PORT_IN', '80'))


@app.route('/')
def hello():
    logger.info('--------GET Root---------')

    app_name = os.environ.get('APP_NAME', 'AWS ECS Flask Webpage')
    container_service = os.environ.get('CONTAINER_SERVICE', 'AWS')
    infra_version = os.environ.get('INFRA_VERSION', '0.0.0')
    python_version = platform.python_version()
    now = datetime.datetime.now()

    # url = 'http://{}.{}/'.format('EcsProjectDemo-EcsAlbStack', 'EcsProjectDemo-NS')
    # body = requests.get(url, timeout=1).text
    # print('===body', body)

    return flask.render_template('index.html',
                                 name=app_name,
                                 platform=container_service,
                                 infra_version=infra_version,
                                 flask_version=flask.__version__,
                                 python_version=python_version,
                                 time=now)


if __name__ == '__main__':
    logger.info('--------start main---------')
    app.run(
        debug=True,
        host='0.0.0.0',
        port=_port
    )