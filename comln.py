#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys, os, io


def put(ch):
	sys.stdout.write(ch)


def lenrow(row):
	nlen = 0
	for ch in row:
		n = len(ch.encode('utf-8', errors='ignore'))
		if n >= 3:
			n = 2
		nlen += n
	return nlen


def putrow(row, nmaxrow, first, last):
	# Decolate front
	if first:
		put('{0} '.format(first))

	# Row
	for ch in row:
		put(ch)

	# Padding
	for _ in range(lenrow(row), nmaxrow):
		put(' ')

	# Decolate back
	if last:
		put(' {0}'.format(last))


def puthorizon(nhor, ch, first, last):
	put(first)
	for i in range(1, nhor-1):
		put(ch)
	put(last)
	put('\n')


def main():
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
	sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
	sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

	# Input from stdin or program arguments
	src = '' # Destination of input
	args = sys.argv[1:]

	if len(args):
		for i in range(0, len(args)-1):
			src += args[i] + ' '
		src += args[-1]
	else:
		src = sys.stdin.read()

 	# Parse source
	mat = [] # Destination matrix
	row = [] # Destination temporary row of matrix
	nmaxrow = 0 # Max length of row in mat
	ntmp = 0
	ntabstop = 4

	for ch in src:
		if ch in '\t':
			for _ in range(0, ntabstop):
				row.append(' ')
			ntmp += ntabstop
			continue

		if ch in '\n':
			if ntmp > nmaxrow:
				nmaxrow = ntmp
			ntmp = 0
			mat.append(list(row))
			row = []
		else:
			nlen = len(ch.encode('utf-8', errors='ignore'))
			if nlen >= 3:
				nlen = 2
			ntmp += nlen
			row.append(ch)

	if len(row):
		if ntmp > nmaxrow:
			nmaxrow = ntmp
		mat.append(list(row))
	row = None

	# Output
	star = '*'
	lefttop = '/'
	rightbottom = '/'

	puthorizon(nmaxrow + 4, star, lefttop, star)

	for i in range(0, len(mat)-1):
		row = mat[i]
		putrow(row, nmaxrow, star, star)
		put('\n')

	if len(mat):
		row = mat[-1]
		putrow(row, nmaxrow, star, star)

	put('\n')
	puthorizon(nmaxrow + 4, star, star, rightbottom)

	sys.stdout.flush()
	sys.stderr.flush()
	return 0


if __name__ == '__main__':
	sys.exit(main())
