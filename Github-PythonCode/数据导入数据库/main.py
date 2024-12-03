from fine_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection

text_file = TextFileReader("c:\\2011年1月销售数据.txt")
json_file = JsonFileReader("c:\\2011年2月销售数据JSON.txt")

jan_data = text_file.read_data()
feb_data = json_file.read_data()

all_data:list[Record] = jan_data + feb_data

try:
    conn = Connection(
        host="localhost",        # 主机名或IP地址
        port=3306,               # 端口号
        user="root",             # 用户名
        password="ZXC123456",    # 密码
        autocommit=True          # 自动提交更改（对于查询操作来说，这个参数不是必需的）
    )

    cursor = conn.cursor()

    conn.select_db("py_sql")

    for record in all_data:
        sql = f"insert into orders(order_date, order_id, money, province) values('{record.date}','{record.order_id}', {record.money}, '{record.province}')"
        cursor.execute(sql)

    conn.commit()

finally:
    cursor.close()
    conn.close()
