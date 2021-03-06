import os
from flask import Flask
from flask_restful import Api
from mongoengine import connect, signals
from .resources import QueryAPI, DocumentAPI
from .documents import Quote, Character, Theme, Page

app = Flask(__name__)
api = Api(app)
connect('quoted', host=os.environ.get('MONGODB_HOST',
                                      'mongodb://127.0.0.1:27017/quoted'))

api.add_resource(QueryAPI, '/api/v1.0/quotes', endpoint='quotes',
                 resource_class_kwargs={'query': Quote, 'endpoint': 'quotes'})
api.add_resource(DocumentAPI, '/api/v1.0/quotes/<id>', endpoint='quote',
                 resource_class_kwargs={'query': Quote, 'endpoint': 'quote'})

api.add_resource(QueryAPI, '/api/v1.0/characters', endpoint='characters',
                 resource_class_kwargs={'query': Character, 'endpoint': 'characters'})
api.add_resource(DocumentAPI, '/api/v1.0/characters/<id>', endpoint='character',
                 resource_class_kwargs={'query': Character, 'endpoint': 'character'})

api.add_resource(QueryAPI, '/api/v1.0/themes', endpoint='themes',
                 resource_class_kwargs={'query': Theme, 'endpoint': 'themes'})
api.add_resource(DocumentAPI, '/api/v1.0/themes/<id>', endpoint='theme',
                 resource_class_kwargs={'query': Theme, 'endpoint': 'theme'})

api.add_resource(QueryAPI, '/api/v1.0/pages', endpoint='pages',
                 resource_class_kwargs={'query': Page, 'endpoint': 'pages'})
api.add_resource(DocumentAPI, '/api/v1.0/pages/<id>', endpoint='page',
                 resource_class_kwargs={'query': Page, 'endpoint': 'page'})

signals.pre_save.connect(Character.pre_save, sender=Character)
signals.pre_save.connect(Theme.pre_save, sender=Theme)
signals.pre_save.connect(Page.pre_save, sender=Page)
signals.post_save.connect(Quote.post_save, sender=Quote)
