from app import *
from app.resources import *
from app.models.user import User

class GetUserAPI(Resource):
    query = db.session.query(User)
    def get(self, id=None):

        try:
            if not id:
                users = query.all()
            else:
                users = query.filter(User.id == id)

                if not users:
                    err_msg = "User with the id not found."
                    logging.error(err_msg)
                    return response_body(None, err_msg), 400


            users_json = []

            for user in users:
                id = user.id
                name = user.name
                mobile = user.mobile
                email = user.email
                users_json.append({'id': id,
                                   'name': name,
                                   'mobile': mobile,
                                   'email': email})

            return response_body({'users_fetched': len(users_json),'users':users_json},
                                 'get success'), 200

        except Exception as e:
            logging.error(e)
            return response_body(None, 'Something went wrong!'), 500