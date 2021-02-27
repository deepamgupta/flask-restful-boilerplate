def add_resources():
    from app import api
    from app.resources import user

    api.add_resource(user.CrudAPI, '/users/', '/users/<int:id>/')