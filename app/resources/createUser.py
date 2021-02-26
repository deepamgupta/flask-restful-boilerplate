from app import *
from app.resources import *
from app.models.user import User

class CreateUserAPI(Resource):
    def post(self):

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
            else:
                user = db.session.query(User).filter(User.mobile == mobile).first()
                if user:
                    err_msg = 'user with that mobile already exists'
                    logging.error(err_msg)
                    return response_body(None, err_msg), 400

            email = json_data.get('email')
            if not email:
                err_msg = 'email not found in request'
                logging.error(err_msg)
                return response_body(None, err_msg), 400
            else:
                user = db.session.query(User).filter(User.email == email).first()
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



