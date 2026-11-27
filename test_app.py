from app import app

def test_loan_api():
    client = app.test_client()
    response = client.get("/loan")

    assert response.status_code == 200

    data = response.get_json()
    assert data["service"] == "Loan Service"
    assert data["status"] == "running"
