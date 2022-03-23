import seq0

exit = False
while not exit:
    filename = seq0.get_file()
    if filename == "nothing":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        reverse = seq0.seq_reverse(full_seq)