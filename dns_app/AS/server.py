from socket import * 
server_port = 53533

# Create a UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind to port 
server_socket.bind(('', server_port))
mappings = {}

# Now listen
print("The server is ready to receive the message...")
while True:
    # Receive Message
    message, client_address = server_socket.recvfrom(2048)
    msg_decoded = message.decode()
    print("Got the message:" + msg_decoded)

    if 'VALUE' in msg_decoded: #REGISTRATION
        print("Registration request is taken")
        # Registration
        splitted = msg_decoded.split("\n")
        name = splitted[1].split('=')[1]
        value  = splitted[2].split('=')[1]
        mappings[name] = value
        print("Name: {}, Value: {}".format(name, value))
        server_socket.sendto("Success".encode(), client_address)
    else: #QUERY
        print("Query is taken")
        splitted = msg_decoded.split('\n')
        name = splitted[1].split('=')[1]
        print("Name: {}".format(name))
        if name in mappings:
            response = "TYPE=A\nNAME={}\nValue={}\nTTL=10".format(name, mappings[name])
            server_socket.sendto(response.encode(), client_address)







