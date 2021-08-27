from flask_restful import Resource
from flask_restful import reqparse

class HelloResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade', type=str, required=True, help="Idade é obrigatório")

    def get(self, nome):
        message = f'Olá {nome}'
        return {"message": message}

    def post(self, name):
        data = HelloResource.parser.parse_args()
        idade = data['idade']
        return {"message": f'olaa {name} vc informou sua idade {idade}'}