from fastapi.testclient import TestClient
import main
from models import User
import pytest
from pytest import mark


client = TestClient(main.app)



@mark.post
def test_register_user():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "age": 32,
    "cpf": "090.163.990-70"
}   
    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 200
    assert response.json() == expected_user
    assert expected_user in main.users
    main.users.remove(expected_user)
    
@mark.post
def test_register_cpf_invalido():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "age": 32,
    "cpf": "090.163.990-72"
    }
    
    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 409
    assert response.json() == {"detail":"Cpf inválido."}


@mark.post
def test_user_ja_cadastrado():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "age": 32,
    "cpf": "090.163.990-70"
    }
    test_user = User(first_name="Marcos", last_name="Vinicius", age=32, cpf="090.163.990-70")
    main.users.append(test_user)

    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 409
    assert response.json() == {"detail":"Usuário já cadastrado."}
    assert expected_user in main.users
    main.users.remove(test_user)
    