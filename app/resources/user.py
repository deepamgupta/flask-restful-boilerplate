from app import *
from app.resources import *
from app.models.user import User

class CrudAPI(Resource):

    def post(self):
        query = db.session.query(User)
        try:
            json_data = request.get_json(force=True)

            name = json_data.get('name')
            if not name:
                err_msg = 'name not found in request'
                logging.error(err_msg)
                return response_body(None, err_msg), 400

            mobile = json_data.get('mobile')
            if not mobile:
                err_msg = 'mobile not found in request'
                logging.error(err_msg)
                return response_body(None, err_msg), 400


            user = query.filter(User.mobile == mobile).first()
            if user:
                err_msg = 'user with that mobile already exists'
                logging.error(err_msg)
                return response_body(None, err_msg), 400


            email = json_data.get('email')
            if not email:
                err_msg = 'email not found in request'
                logging.error(err_msg)
                return response_body(None, err_msg), 400

            user = query.filter(User.email == email).first()
            if user:
                err_msg = 'user with that email already exists'
                logging.error(err_msg)
                return response_body(None, err_msg), 400

            new_user = User()
            new_user.name = name
            new_user.mobile = mobile
            new_user.email = email
            db.session.add(new_user)
            db.session.commit()

            return response_body({'user':{'id': new_user.id,
                                          'name': new_user.name,
                                          'mobile':new_user.mobile,
                                          'email':new_user.email}},
                                 'user created'), 201

        except Exception as e:
            logging.error(e)
            return response_body(None, 'Something went wrong!'), 500

    def delete(self, id=None):
        query = db.session.query(User)
        global message, response_status
        try:
            if not id:
                num_rows_deleted = db.session.query(User).delete()
                message = 'deleted all users'
                response_status = 200
            else:
                num_rows_deleted = query.filter(User.id == id).delete()
                message = 'User deleted successfully!'
                response_status = 200
                if not num_rows_deleted:
                    message = 'User with that id not found'
                    response_status = 400
                    logging.error(message)

            db.session.commit()

            return response_body({"num_rows_deleted":num_rows_deleted}, message), response_status

        except Exception as e:
            logging.error(e)
            return response_body(None, 'Something went wrong!'), 500

    def get(self, id=None):
        query = db.session.query(User)
        try:
            if not id:
                users = query.all()
            else:
                users = query.filter(User.id == id)

                if not users:
                    err_msg = "User with the id not found."
                    logging.error(err_msg)
                    #return response_body(None, err_msg), 400
                    abort(400, err_msg)


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

    def patch(self, id=None):
        query = db.session.query(User)
        try:

            if not id:
                err_msg = 'Please provide valid id of the user to update.'
                return response_body(None, err_msg), 400

            json_data = request.get_json(force=True)
            name = json_data.get('name')
            mobile = json_data.get('mobile')
            email = json_data.get('email')

            user = query.filter(User.id == id).first()

            if name:
                user.name = name
            if mobile:
                user.mobile = mobile
            if email:
                user.email = email

            if not any([name, mobile, email]):
                err_msg = 'Provide at least one of name, mobile or email to update user.'
                logging.error(err_msg)
                return response_body(None, err_msg), 400

            db.session.commit()

            return response_body({"updated_user":{'id': user.id,
                                                  'name': user.name,
                                                  'mobile':user.mobile,
                                                  'email':user.email}},
                                 'updated'), 200

        except Exception as e:
            logging.error(e)
            return response_body(None, 'Something went wrong!'), 500



