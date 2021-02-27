def add_resources():
    from app import api
    from app.resources import crud

    api.add_resource(crud.CrudAPI, '/users/', '/users/<int:id>/')