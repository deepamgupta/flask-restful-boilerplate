from app import *
from app.resources import *
from app.models.user import User

class DeleteUserAPI(Resource):

    def delete(self, id=None):
        global message, response_status
        try:
            if not id:
                num_rows_deleted = db.session.query(User).delete()
                message = 'deleted all users'
                response_status = 200
            else:
                num_rows_deleted = db.session.query(User).filter(User.id == id).delete()
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

