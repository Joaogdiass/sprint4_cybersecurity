import time, jwt, pytest
SECRET="change-me"

def issue_token(user_id: str) -> str:
    now = int(time.time())
    payload = {"sub": user_id, "iat": now, "exp": now + 3600, "iss":"sprint3","aud":"students"}
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=["HS256"], audience="students", issuer="sprint3")

def test_jwt_has_exp_and_validates():
    t = issue_token("u1")
    data = verify_token(t)
    assert "exp" in data and data["sub"]=="u1"

def test_expired_token_fails():
    now = int(time.time())
    t = jwt.encode({"sub":"x","iat":now-4000,"exp":now-1,"iss":"sprint3","aud":"students"}, SECRET, algorithm="HS256")
    with pytest.raises(Exception):
        verify_token(t)
