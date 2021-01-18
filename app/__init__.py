# app/__init__.py

from flask_restplus import Api
from flask import Blueprint, url_for

#from werkzeug.contrib.fixers import ProxyFix

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

class Custom_API(Api):
    @property
    def specs_url(self):
        '''
        The Swagger specifications absolute url (ie. `swagger.json`)

        :rtype: str
        '''
        return url_for(self.endpoint('specs'), _external=False)



blueprint = Blueprint('api', __name__)
#blueprint.wsgi_app = ProxyFix(blueprint.wsgi_app)

api = Custom_API(blueprint,
          title='FLASK RESTPLUS API WS01 WITH JWT',
          version='1.0',
          description='flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
