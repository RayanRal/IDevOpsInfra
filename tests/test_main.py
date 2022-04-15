from src.idevopsinfra.web.main import main_func


def test_main():
    result = main_func()
    assert result
