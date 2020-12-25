from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
  __tablename__ = 'employees'

  id = db.Column(Integer, primary_key=True)
  name = db.Column(String(100), nullable=False)
  employee_number = db.Column(Integer, nullable=False, unique=True)
  hashed_password = db.Column(String(100), nullable=False)


  @property
  def password(self):
      return self.hashed_password


  @password.setter
  def password(self, password):
      self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
      return check_password_hash(self.password, password)
