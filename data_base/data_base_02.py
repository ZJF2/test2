from pymysql import *
conn = connect(host="localhost", port=3306, user="root",
                       password="zt6691zt", database="jd", charset="utf8")
cs1 = conn.cursor()  # 返回对象

cs1.execute("""INSERT INTO GOODS_CATES (NAME) VALUES ("硬盘");""")
conn.rollback()
cs1.execute("""INSERT INTO GOODS_CATES (NAME) VALUES ("耳机");""")
conn.commit()
cs1.close()
conn.close()


