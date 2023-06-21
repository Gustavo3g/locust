from locust import HttpUser, TaskSet, task


class UserRouteLoadTest(TaskSet):

    @task()
    def test_list_users(self):
        self.client.get("/usuarios", name="Listar usuarios")


    @task()
    def test_create_user(self):
        self.client.post(
            "/usuarios",
            name="Criar usuario",
            json={
                "nome": "Gustavo Locust",
                "email": "gustavolocust@test.com",
                "password": "teste",
                "administrador": "false"
            }
        )