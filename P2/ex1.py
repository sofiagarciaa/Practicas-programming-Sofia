from client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
SERVER_IP = "localhost"
SERVER_PORT = 8081

# -- Create a client object
c = Client(SERVER_IP, SERVER_PORT)

# -- Test the ping method
c.ping()

# -- Print the IP and PORTs
print(f"Server's address: ({c.server_ip}:{c.server_port})")