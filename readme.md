# PortSniffer
# Open Ports Discovery Tool

This Python script is a Port/Service Discovery tool given an IP address by user. It retrieves the availability of host,open port and the service running on that specific port.

- If Service 'name' is NOT found, displays the IP, Open port and ' - ' as output for service.

## Features

- Open ports discovery
- Service identification

## Prerequisites

- Python 3.x
- Required Python packages:
  - `scoket`
  - `subprocess`


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nomespaladin/portsniffer.git
    cd portsniffer
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script and enter an IP address when prompted(in the format: Eg. 127.0.0.1/10.0.0.1):
```sh
python portsniffer.py
```

## Consider
- The program will NOT display any information until finds it, so expect the code to look like 'it's not wokrking'.
- It will and can take a while to start finding open ports.



## Example Overview
```
█ ▄▄  ████▄ █▄▄▄▄    ▄▄▄▄▀ ▄▄▄▄▄    ▄   ▄█ ▄████  ▄████  ▄███▄   █▄▄▄▄ 
█   █ █   █ █  ▄▀ ▀▀▀ █   █     ▀▄   █  ██ █▀   ▀ █▀   ▀ █▀   ▀  █  ▄▀ 
█▀▀▀  █   █ █▀▀▌      █ ▄  ▀▀▀▀▄ ██   █ ██ █▀▀    █▀▀    ██▄▄    █▀▀▌  
█     ▀████ █  █     █   ▀▄▄▄▄▀  █ █  █ ▐█ █      █      █▄   ▄▀ █  █  
 █            █     ▀            █  █ █  ▐  █      █     ▀███▀     █   
  ▀          ▀                   █   ██      ▀      ▀             ▀    
                                                                       

  -version 1.1                                          By:NomesPaladin
        
Enter IP:127.0.0.1

The IP '127.0.0.1' is Connected|Online.
This can take a while...(ctrl+C to exit program)

Report|127.0.0.1|135 >> epmap | Status: Open |
Report|127.0.0.1|139 >> netbios-ssn | Status: Open |
Report|127.0.0.1|23 >> telnet | Status: Open |
Report|127.0.0.1|22 >> ssh | Status: Open |
Report|127.0.0.1|80 >> http| Status: Open |
Report|127.0.0.1|443 >> https | Status: Open |


```
