import sqlite3
from flask import Flask, render_template, g
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)

@app.before_request
def before_request():
    # Create a database
    g.conn = sqlite3.connect("gitusers.db")
    g.conn.row_factory = sqlite3.Row
    g.cur = g.conn.cursor()


@app.teardown_request
def teardown(error):
    if hasattr(g, "conn"):
        g.conn.close()    
    
def get_git_users(offset=0, per_page=10):
    sql = "select * from users limit {}, {}".format(
            offset, per_page)
    g.cur.execute(sql)
    users = g.cur.fetchall()
    return users

##############################
# Flask routes with pagination
##############################
@app.route('/')
def index():
    g.cur.execute("select count(*) from users")
    total = g.cur.fetchone()[0]
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_users = get_git_users(offset=offset, per_page=per_page)  
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('sqldatabase.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


# Debug Mode
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

# Production Mode
# if __name__ == '__main__':
#  app.run(host='0.0.0.0')