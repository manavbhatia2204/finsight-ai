def test_fastapi_app_imports_and_boots():
    """
    Verify the FastAPI app itself can be imported without error.
    This directly guards against missing dependencies in main.py
    (e.g. the slowapi import that broke the Hugging Face deployment
    without CI catching it, since no other test imported main.py).
    """
    from api.main import app

    assert app is not None
    assert app.title == "FinSight AI API"


def test_fastapi_app_has_expected_routes():
    """Verify the core routes are registered on the app."""
    from api.main import app

    route_paths = [route.path for route in app.routes]

    assert "/health" in route_paths
    assert "/ready" in route_paths
    assert "/ask" in route_paths
    assert "/predict/{ticker}" in route_paths
    assert "/stocks/{ticker}/history" in route_paths
    assert "/stocks/{ticker}/live" in route_paths
    assert "/metrics" in route_paths