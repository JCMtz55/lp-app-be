from src import config, create_app

application=create_app()

if __name__ == "__main__":
    application.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG)