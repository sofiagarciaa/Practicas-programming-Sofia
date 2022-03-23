import seq0

filename = seq0.get_file()
full_seq = seq0.seq_read_fasta(filename)
d = seq0.seq_count(full_seq)
print(d)
