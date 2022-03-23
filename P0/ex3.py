import seq0

FOLDER = "./sequences/"

gene = input("Choose a gene: ")
f = open(FOLDER + gene + ".txt")
print(f.read())
