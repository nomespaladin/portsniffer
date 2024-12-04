#import necessary modules
import socket
import subprocess

#define function to check ip's connection
def check_ip(ip):
    result = subprocess.run(["ping","-c 1",ip], capture_output = True, text = True)
    try:
        if "Request timed out" in result.stdout:
            print(f"The IP '{ip}' is Disconnected|Offline.")
        else:
            print(f"The IP '{ip}' is Connected|Online.")
    except ConnectionAbortedError as cae:
        print(f"CRITICAL : {cae}")


def sniff_port(ip,port):
    net = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection = net.connect_ex((ip,port))
    
    if connection == 0:
        try:
            service = socket.getservbyport(port)
            
            print(f"Report for |{ip}|Port {port}| >>{service} | Status: Open |")
        except OSError as ose:
            print(f"CRITICAL {ose}")
            #attempt to banner grabbing
            net.send(b"")
            banner = net.recv(1024)
            print(f"{banner.decode().strip()}")
    net.close()

#main function will constantly run
def main():
    while True:
        print("""
        

█ ▄▄  ████▄ █▄▄▄▄    ▄▄▄▄▀ ▄▄▄▄▄    ▄   ▄█ ▄████  ▄████  ▄███▄   █▄▄▄▄ 
█   █ █   █ █  ▄▀ ▀▀▀ █   █     ▀▄   █  ██ █▀   ▀ █▀   ▀ █▀   ▀  █  ▄▀ 
█▀▀▀  █   █ █▀▀▌      █ ▄  ▀▀▀▀▄ ██   █ ██ █▀▀    █▀▀    ██▄▄    █▀▀▌  
█     ▀████ █  █     █   ▀▄▄▄▄▀  █ █  █ ▐█ █      █      █▄   ▄▀ █  █  
 █            █     ▀            █  █ █  ▐  █      █     ▀███▀     █   
  ▀          ▀                   █   ██      ▀      ▀             ▀    
                                                                       

  -version 1.1                                          By:NomesPaladin
        """)
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


if __name__ == '__main__':
    main()
    