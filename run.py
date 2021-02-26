from app import app, resources_init

resources_init.add_resources()

if __name__ == '__main__':
    app.run(debug=True)