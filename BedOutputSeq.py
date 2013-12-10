from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='Get sequences associated with peaks')
parser.add_argument('-p',help = 'Name of the peaks file',default = None)
parser.add_argument('-l',help = 'Total length of the sequence',default = 200)
parser.add_argument('-o',help = 'Name of the output fasta file',default = None)
parser.add_argument('-f',help = 'The reference fasta file',default = None)
args = parser.parse_args()

if args.p is None or args.o is None or args.f is None:
	print 'Tell me what file I need idiot'
	raise SystemExit

	