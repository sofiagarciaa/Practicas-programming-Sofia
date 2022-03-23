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

seq = "FRAT1.txt"
s = Seq()
s.read_fasta2(seq)
frag1 = str(s)[:10]
frag2 = str(s)[11:20]
frag3 = str(s)[21:30]
frag4 = str(s)[31:40]
frag5 = str(s)[41:50]

sequences = [frag1, frag2, frag3, frag4, frag5]

init(autoreset=True)

print(f"Gene FRAT1 {Fore.BLUE + str(s) } to the server in fragments of 10 bases...")
response = c.talk(f"Sending {seq} gene to server")

for i in sequences:
    print(Fore.BLUE + " Sending " + seq + " Gene to server, in fragments of 10 bases")
    response = c.talk(f"Fragment 1: {i} gene to server")
