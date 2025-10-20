def allowed_fields(scope):
    return {"cadastro":["nome","email"], "login":["email"]}

def test_minimize_login_scope():
    assert "cpf" not in allowed_fields("login")
