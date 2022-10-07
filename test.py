from app import app


def test():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test2():
    response = app.test_client().get("/base")
    assert response.status_code == 200

def test3():
    response = app.test_client().get("/base")
    assert b'added' in response.data.lower()

def test4():
    response = app.test_client().get("/asdas")
    assert response.status_code == 404

