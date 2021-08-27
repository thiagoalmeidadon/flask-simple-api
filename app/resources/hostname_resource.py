from flask_restful import Resource
from app.models.hostname_models import get_hostname

class HostnameResource(Resource):
    def get(self):
        hostname = get_hostname()
        return { "Message ": f'A api executando no {hostname}'}