def add_resources():
    from app import api
    from app.resources import createUser, getUser, updateUser, deleteUser

    # api for creating user
    api.add_resource(createUser.CreateUserAPI, '/users/')

    # api for getting user
    api.add_resource(getUser.GetUserAPI, '/users/', '/users/<int:id>/')

    # api for updating user
    api.add_resource(updateUser.UpdateUserAPI, '/users/<int:id>/')

    # api for deleting user
    api.add_resource(deleteUser.DeleteUserAPI, '/users/', '/users/<int:id>/')
