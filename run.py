from dotenv import load_dotenv

from app import create_app
from config.development import DevelopmentConfig

# Load environment variables from .env file
load_dotenv()

app = create_app(DevelopmentConfig)


if __name__ == "__main__":
    app.run()
