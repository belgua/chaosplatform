from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app=app)
model = api.model("simple_model", {'some_bool': fields.Boolean(required=False, default=False),
                                   'some_int': fields.Integer(required=False, default=99)})


@api.route('/foo')
class SomeClass(Resource):

    @api.expect(model)
    def post(self):
        return request.json


if __name__ == '__main__':
    app.run(host='localhost', port=8000, threaded=False, debug=True)