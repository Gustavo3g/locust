from locust import HttpUser
from rota_usuarios import UserRouteLoadTest

class WebsiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]