import seq0

exit = False
while not exit:
    filename, gene = seq0.get_file()
    if filename == "nothing":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        complement = seq0.seq_complement(full_seq)
        print(complement)