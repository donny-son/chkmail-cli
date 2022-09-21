build:
	pex \
	--requirement=requirements.txt \
	--sources-directory=. \
	--output-file=dist/chkmail \
	-m chkmail
