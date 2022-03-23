import seq0

import seq0

exit = False
while not exit:
    filename, gene = seq0.get_file()
    if filename == "nothing":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        value = seq0.frequent_value(full_seq)
        base = seq0.frequent_value(d)
        print(base)