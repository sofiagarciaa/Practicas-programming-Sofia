def seq_ping():
    print("ok")

def get_file():
    exit = False
    while not exit:
        FOLDER = "./sequences/"
        gene = input("Enter a filename:")
        try:
            filename = open(FOLDER + gene + ".txt", "r")
            exit = True
            return filename, gene
        except FileNotFoundError:
            if gene.lower() == "exit":
                print("The program has finished")
                filename = "nothing"
                exit = True
                return filename, gene
            else:
                print("File was not found.Try again")

def seq_read_fasta(filename):
    full_seq = filename.read()
    full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
    return full_seq

def seq_count_base(full_seq):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in full_seq:
            if i == "A":
                count_a += 1
            elif i == "C":
                count_c += 1
            elif i == "G":
                count_g += 1
            elif i == "T":
                count_t += 1

    return count_a, count_c, count_g, count_t


def seq_count(full_seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in full_seq:
        d[b] += 1
    return d

def seq_reverse(full_seq):
    fragment = full_seq[0:20]
    reverse = full_seq[::-1]
    return reverse

def seq_complement(full_seq):
    fragment = full_seq[0:20]
    complement = ""
    for i in fragment:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "G":
            complement += "C"
        elif i == "C":
            complement += "G"

    return complement

def frequent_value(d):
    highest_value = 0
    for k, v in d.items():
        if int(v) > highest_value:
            highest_value = int(v)
            base = k
    return base