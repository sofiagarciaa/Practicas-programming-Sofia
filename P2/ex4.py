from client0 import Client
from Seq1 import Seq
from colorama import init,  Fore

PRACTICE = 2
EXERCISE = 4

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

s = "FRAT1.txt"
s1 = "ADA.txt"
s2 = "FXN.txt"

sequences = [s, s1, s2]
for i in sequences:
    init(autoreset=True)
    s0 = Seq()
    s0.read_fasta2(i)
    print(Fore.BLUE + " Sending " + i + " to the server...")
    response = c.talk(Fore.LIGHTYELLOW_EX + " Sending " + i + " to the server...")
    print(f"Response: {response}")
    print(" Sending " + Fore.BLUE + str(s0) + "to the server...")
    print(c.talk(s0.strbases))
    print(f"Response: {response}")
