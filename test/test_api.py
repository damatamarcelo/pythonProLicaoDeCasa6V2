from requests import get, post
from json import loads


class TestAPI:
    def setup(self):
        self.url = "http://localhost:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIResponse(self):
        resp = get(self.url)
        mensagem = loads(resp.text)
        assert mensagem[
                   "mensagem"] == "Bem vindo a api de operações básicas, cheque a documentação e o método POST: math!"

    def test_SOMA(self):
        resp = post(self.url + "/math", json={"valor1": 15, "valor2": 10, "oper": "+"})
        mensagem = loads(resp.text)
        esperada = {"Soma": 5}
        assert mensagem == esperada

    def test_SUB(self):
        resp = post(self.url + "/math", json={"valor1": 25, "valor2": 15, "oper": "-"})
        mensagem = loads(resp.text)
        esperada = {"Subtração": 0}
        assert mensagem == esperada

    def test_MULT(self):
        resp = post(self.url + "/math", json={"valor1": 20, "valor2": 25, "oper": "x"})
        mensagem = loads(resp.text)
        esperada = {"Multiplicação": 400}
        assert mensagem == esperada

    def test_DIV(self):
        resp = post(self.url + "/math", json={"valor1": 500, "valor2": 20, "oper": ":"})
        mensagem = loads(resp.text)
        esperada = {"Divisão": 125}
        assert mensagem == esperada
