#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request,redirect,url_for
import pymysql


# In[ ]:


host="database-2.contk8ieomwk.ap-south-1.rds.amazonaws.com"
port=3306
dbname="loblaw"
user="salai123"
password="RF&cloudy11"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname,cursorclass=pymysql.cursors.DictCursor)


# In[ ]:


cursor = conn.cursor()


# In[ ]:


app = Flask(__name__)


# In[ ]:


retrive = f"Select * from ITEM where NAME LIKE '%jac%' LIMIT 1;"
cursor.execute(retrive)
rows = cursor.fetchall()
len(rows)


# In[ ]:


url_dict = {}
@app.route('/')
def show_first():
    return render_template("index.html")

#@app.route('/show_index/<select_key>')
#def show_index(select_key):
#    return render_template("index.html", user_image = url_dict['URL'])



@app.route('/',methods=['POST','GET'])
def my_form_post():
    
   
    text = request.form['u']
    url_key = text.lower()
    
    retrive = f"Select * from ITEM where NAME LIKE '%{url_key}%' LIMIT 1;"
    cursor.execute(retrive)
    rows = cursor.fetchall()
    
    if len(rows) != 0:
        url_dict = rows[0]
        select_key = url_dict['NAME']
        
    else:
        retrive = "Select * from ITEM where NAME='none';"
        cursor.execute(retrive)
        rows = cursor.fetchall()
        url_dict = rows[0]
        select_key = url_dict['NAME']
    
    print(select_key)
        


    return render_template("index.html", user_image = url_dict['URL'])


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)
    conn.close()


# In[ ]:




