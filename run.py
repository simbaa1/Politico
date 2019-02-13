import os
from app import create_app

config_name = os.getenv('APP_SETTINGS')
port = int(os.environ.get('PORT', 5000))

app = create_app(config_name)

if __name__ == "__main__":
    app.run()