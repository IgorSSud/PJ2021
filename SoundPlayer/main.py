import socket

import playsound

if __name__ == '__main__':
    print('PyCharm')
    sock = socket.socket()
    sock.bind(('', 9091))
    sock.listen(1)


    while True:
        conn, addr = sock.accept()
        print('connected:', addr)
        data = conn.recv(1024)
        if not data:
            conn.close()
        # if len(data)>0:
        #     print(str(data))
        #     conn.send(data.upper())

        if data.decode('utf-8')=='Morning':
            print("yes")
            conn.send("Morning music play".encode("utf-8"))
            playsound.playsound("Morning.mp3")
        elif data.decode('utf-8')=='AC_DC_Shoot_still':
            print("yes")
            conn.send("AC_DC_Shoot_still music play".encode("utf-8"))
            playsound.playsound("ACDC - Shoot to Thrill.mp3")


