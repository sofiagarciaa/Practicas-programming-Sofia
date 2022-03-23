import seq0

exit = False
while not exit:
    filename, gene = seq0.get_file()
    if filename == "nothing":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        count_a, count_c, count_g, count_t = seq0.seq_count_base(full_seq)
        print(count_a, count_c, count_g, count_t)