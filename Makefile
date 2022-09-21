build:
	poetry run pex \
	--requirement=requirements.txt \
	--sources-directory=. \
	--output-file=dist/chkmail \
	-m chkmail

install:
	sudo cp ./dist/chkmail /usr/local/bin
