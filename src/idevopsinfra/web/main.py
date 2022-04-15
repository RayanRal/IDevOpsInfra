from src.idevopsinfra import app


@app.route('/')
def index():
    return 'Hello, World!'


def main_func() -> bool:
    return True
