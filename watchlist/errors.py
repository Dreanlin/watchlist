from watchlist import app
from flask import render_template

#搜索错误网页地址的响应
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码    

#handle bad request
@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400

#handle internal error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500