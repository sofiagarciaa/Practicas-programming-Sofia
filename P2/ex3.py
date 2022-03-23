from client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 6123
IP = "127.0.0.1"

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()

# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")