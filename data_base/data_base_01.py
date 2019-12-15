from pymysql import *

class JD(object):

    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root",
                       password="zt6691zt", database="jd", charset="utf8")
        self.cs1 = self.conn.cursor()  # 返回对象
    @staticmethod
    def print_menu():
        print("----------")
        print("1 所有商品")
        print("2 所有商品分类")
        print("3 所有商品品牌分类")
        print("4 添加新的商品品牌名称")
        print("5 根据名字查询商品")
        return input("请输入对应的选择")
    def run(self):
        while True:
            op = JD.print_menu()
            if op == "1":
                # 查询所有商品
                self.show_all_items()
            elif op == "2":
                # 查询所有商品分类
                self.show_cates()
            elif op == "3":
                # 查询所有商品品牌分类
                self.show_brands()
            elif op == "4":
                self.add_brands()
            elif op == "5":
                self.get_info_by_name()
            else:
                print("输入有误")
                break
    def execute_sql(self,sql):
        self.cs1.execute(sql)
        print(self.cs1.fetchall())
    def show_all_items(self):
        sql = "SELECT * FROM goods;"
        self.execute_sql(sql)
    def show_cates(self):
        sql = "SELECT name FROM goods_cates;"
        self.execute_sql(sql)
    def show_brands(self):
        sql = "SELECT name FROM goods_brands;"
        self.execute_sql(sql)
    def add_brands(self):
        items = input("输入新的商品分类的名称：")
        sql = """INSERT INTO GOODS_BRANDS (NAME) VALUES ("%s");""" % items
        self.cs1.execute(sql,)
        self.conn.commit()
    def get_info_by_name(self):
        items = input("输入商品名字查询商品：")
        sql = "SELECT * FROM GOODS WHERE NAME = %s;"
        self.cs1.execute(sql,[items])
        print(self.cs1.fetchone())
    def __del__(self):
        self.cs1.close()
        self.conn.close()

def mian():
    # 创建对象
    jd = JD()
    jd.run()

if __name__ == '__main__':
    mian()