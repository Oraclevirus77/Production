from app.main import db, flask_bcrypt
from sqlalchemy.sql import func


class User(db.Model):
    """
    User model for storing user related details
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    registered_on = db.Column(db.DateTime, default=func.now())
    updated_on = db.Column(
        db.DateTime, default=func.now(), onupdate=func.now())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(100))
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref(
        'users', lazy='joined'), uselist=False)

    def __repr__(self):
        return '<User %r' % self.username  # returns the username in a string format

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Role(db.Model):
    """User model for storing role related details"""
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class UserRoles(db.Model):
    """UserRoles model for storing user roles"""
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = db. Column(db.Integer, db.ForeignKey(
        'role.id', ondelete='CASCADE'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
