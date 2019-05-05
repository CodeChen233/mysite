import socket, pymysql


def start_socket():
    # if ask:

        sk = socket.socket()

        # 为socket绑定IP和端口号

        address = ('172.17.46.74', 8002)  # 代指本机IP地址
        sk.bind(address)

        # 服务器socket监听端口号请求，随时准备接收客户端发来的连接，这时候服务器的socket并没有被打开

        sk.listen(1000)    # 可等待的人数
        print('waiting receive message..........')
        # MCU_list = []
        flag = True
        while flag:
            # conn ==> 客户端的socket对象 addr ==> 客户端IP地址和端口
            conn, addr = sk.accept()
            print(addr)
            while flag:
                try:
                    data = conn.recv(1024)   # sever的conn和client的sk是一个东西
                except Exception:
                    break
                MCU_data = str(data, 'utf8')
                # Get_data.objects.all()
                # Get_data.objects.create(data=MCU_data)
                print('单片机数据:', MCU_data)
                # MCU_list.append(MCU_data)
                # print(MCU_list)
                db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                                     passwd='1996chen', db='mysite_db', charset='utf8')
                cursor = db.cursor()

                try:
                    # 执行sql语句
                    # cursor.execute(sql)
                    cursor.execute('insert into website_get_data(get_data) values(%s)', MCU_data)
                    # 提交到数据库执行
                    cursor.execute('select * from website_get_data')
                    print(cursor.fetchall())
                    db.commit()
                except:
                    # 如果发生错误则回滚
                    db.rollback()

                # 关闭数据库连接
                db.close()
                if not data:
                    break
            conn.close()  # 关闭与某个client的通信
        return 1






