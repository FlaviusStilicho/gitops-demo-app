def test_health(test_client):
    response = test_client.get("/health")
    assert b"Hello!" in response.data