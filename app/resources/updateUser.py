from app import *
from app.resources import *
from app.models.user import User


class UpdateUserAPI(Resource):
    def patch(self, id=None):
        try:

            if not id:
                err_msg = 'Please provide valid id of the user to update.'
                return response_body(None, err_msg), 400

            json_data = request.get_json(force=True)
            name = json_data.get('name')
            mobile = json_data.get('mobile')
            email = json_data.get('email')

            user = db.session.query(User).filter(User.id == id).first()

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

