import sys

if len(sys.argv) != 3:
	print("usage:\npython kallisto_sam_convertor.py <psudoalignment.sam> <annotation.gtf> > <reformated.sam>")
	sys.exit()

pos_tr = {}
neg_tr = {}

with open(sys.argv[2],'r') as anotationfile:
	for entry in anotationfile:
		entry = entry.split('\t')
		key = entry[8].split('"')[1]
		if entry[6] == '+':
			pos_tr[key] = entry[3]
		else:
			neg_tr[key] = entry[3]

with open(sys.argv[1],'r') as samfile:
	for samline in samfile:
		if samline[:3] == '@HD':
			print(samline, end='')
			print("@SQ	SN:S5_genome	LN:6778833")
		if samline[:3] == '@PG':
			print(samline, end='')
			break
	for samline in samfile:
		samline = samline.split('\t')
		print('\t'.join(samline[0:2]), end="\t")
		print('S5_genome', end="\t")
		tr_pos = int(samline[3])
		try:
			gen_pos = pos_tr[samline[2]]
		except KeyError:
			try:
				gen_pos = neg_tr[samline[2]]
			except KeyError:
				print('Something is wrong here, gene ',samline[2],' is not in the list.')
				break
		genome_pos = tr_pos + int(gen_pos) - 1
		print(genome_pos, end="\t")
		print('\t'.join(samline[4:]), end='')
