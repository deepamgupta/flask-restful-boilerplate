from app.models import *


class User(Base):

    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    mobile = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

    # def __repr__(self):
    #     return "User(id: {}, name: {}, mobile: {}, email: {})"\
    #         .format(self.id, self.name, self.mobile, self.email)
