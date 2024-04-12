import pymysql

connection = pymysql.connect(host='172.17.0.3', user='root', password='password', db='db')

print(connection)

# execute() có tác dụng thức thi các truy vấn MySQL
try:
  with connection.cursor() as cursor:
    query = "CREATE DATABASE pymysql"
    print(cursor.execute(query))
finally:
  connection.close()


# executemany() tương tự như phương thức execute(), có khả năng làm ảnh hưởng nhiều dòng dữ liệu trên 1 câu query
connection = pymysql.connect(host='172.17.0.3', user='root', password='password', db='db')
try:
  with connection.cursor() as cursor:
    query = """
        CREATE TABLE `users` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `email` varchar(255) NOT NULL,
            `password` varchar(255) NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        AUTO_INCREMENT=1
    """
    cursor.execute(query)
finally:
  connection.close()


# commit() : mặc định thì connection không tự động commit thay đổi nên bạn cần phải sử dụng phương thức commit() để thực hiện commit data khi có thay đổi.
connection = pymysql.connect(host='172.17.0.3', user='root', password='password', db='db')
with connection.cursor() as cursor:
  # insert a user
  sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
  cursor.execute(sql, ('admin@toidicode.com', '123456'))
  # commit
  connection.commit()

#  autocommit() để enable disable chế độ auto commit
connection = pymysql.connect(host='172.17.0.3', user='root', password='password', db='db')
connection.autocommit(True)
with connection.cursor() as cursor:
  # insert a user
  sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
  print(cursor.execute(sql, ('thanhtaivtt@toidicode.com', '123456')))

# fetchone() : lấy ra duy nhất một bản ghi đầu tiên của dữ liệu trả về, trả về dữ liệu kiểu tuple.
# fetchmany() : có tác dụng fetch dữ liệu trả về của câu query với số lượng bản ghi lấy ra tùy chỉnh.
# fetchall() :fetch ra tất cả data mà câu truy vấn trả về. Phương thức này trả về một list các tuple.
with connection.cursor() as cursor:
  sql = "SELECT * FROM users"
  result_count = cursor.execute(sql)
  print('Data Count:', result_count)
  print(cursor.fetchone())
  print(cursor.fetchmany(2))

# update 
with connection.cursor() as cursor:
    sql = "UPDATE users SET password = '1111'"
    result_count = cursor.execute(sql)
    #commit change
    connection.commit()

# delete
with connection.cursor() as cursor:
  sql = "DELETE FROM users"
  result_count = cursor.execute(sql)
  #commit change
  connection.commit()

# exec to python container and run 'pip install PyMySQL' after that 'pip install cryptography'
# docker cp python_mysql/connnection.py python_container_name:/home/
# python home/connnection.py
# run 'docker inspect name-mysql | grep IPAddress' to get host