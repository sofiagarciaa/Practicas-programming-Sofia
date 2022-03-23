from Seq1 import Seq


def get_file():
    exit = False
    while not exit:
        folder = "./sequences/"
        filename = input("Enter a filename:")
        try:
            print(folder + filename + ".txt")
            f = open(folder + filename + ".txt", "r")
            exit = True
            return folder + filename + ".txt"
        except FileNotFoundError:
            print("File was not found.Try again")


s1 = Seq()
filename = get_file()
s1.read_fasta2(filename)

print(f"\nSequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse: ", s1.reverse())
print("Complementary:", s1.complement())
base = s1.processing_genes(d)
print(f"Gene {filename} : \nmost frequent value Base: {base}")