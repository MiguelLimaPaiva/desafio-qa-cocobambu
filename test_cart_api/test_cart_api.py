import requests

BASE_URL = "https://dummyjson.com/carts"

# Adicionando item ao carrinho
def test_add_to_cart():
    res = requests.post(f"{BASE_URL}/add", json={
        "userId": 1,
        "products": [{"id": 1, "quantity": 2}]
    })
    assert res.status_code == 200
    assert "id" in res.json()

# Atualizando item
def test_update_cart():
    res = requests.put(f"{BASE_URL}/1", json={
        "merge": True,
        "products": [{"id": 1, "quantity": 3}]
    })
    assert res.status_code == 200
    data = res.json()
    assert any(p["quantity"] == 3 for p in data["products"])

# Deletando item
def test_delete_cart():
    res = requests.delete(f"{BASE_URL}/1")
    assert res.status_code == 200

