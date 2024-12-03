#import necessary modules
import socket
import subprocess

def check_ip(ip):
    result = subprocess.run(["ping","-c 1",ip], capture_output = True, text = True)
    try:
        if "Request timed out" in result.stdout:
            print(f"The IP '{ip}' is offline.")
        else:
            print(f"The IP '{ip}' is online.")
    except ConnectionAbortedError as cae:
        print(f"CRITICAL : {cae}")



def sniff_port(ip,port):
    net = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection = net.connect_ex((ip,port))
    if connection == 0:
        print(f"Report for IP | {ip}")
        try:
            service = socket.getservbyport(port)
            print(f"Port|{port} >> {service}")
        except OSError as ose:
            print(f"CRITICAL {ose}")
            #attempt to banner grabbing
            net.send(b"TESTING PARAMS \r\n")
            banner = net.recv(1024)
            print(f"{banner.decode().strip()}")
    net.close()


def main():
    while True:
        try:
            ip = input("Enter IP:")
            #ping target to check and print it's availability
            check_ip(ip)
            print("This can take a while...(ctrl+C to exit program)")
            for port in range(1,65536):
                sniff_port(ip,port)
        except KeyboardInterrupt:
            print("Program Finished")
            break


main()