from flask import Flask


def test_app_creation(app):
    assert isinstance(app, Flask)


def test_test_page(client):
    response = client.get("/whale")
    assert response.status_code == 200
    assert b"Whale, Hello there!" in response.data


# def test_cli_runner(runner):
#     result = runner.invoke(args=['command'])
#     assert 'Expected output' in result.output
