from watchlist import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#设置数据库的表对应的模型类
class User(db.Model, UserMixin):#表名为user全小写
    __tablename__ = 'user_table' #规定在flask shell中db.create_all()后，这个模型类生成的数据表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
