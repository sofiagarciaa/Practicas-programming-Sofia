import seq0
filename = seq0.get_file()
full_seq = seq0.seq_read_fasta(filename)
print(full_seq[:20])
