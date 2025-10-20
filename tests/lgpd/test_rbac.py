def is_authorized(role, action):
    matrix = {"admin":{"export_pessoal":True},"user":{"export_pessoal":False}}
    return matrix.get(role,{}).get(action,False)

def test_rbac_export():
    assert is_authorized("admin","export_pessoal")
    assert not is_authorized("user","export_pessoal")
