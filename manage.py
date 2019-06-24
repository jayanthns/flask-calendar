from application import create_app

app = create_app()

app.app_context().push()


@app.cli.command()
def runserver():
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    runserver()
