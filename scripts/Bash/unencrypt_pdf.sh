#! /bin/bash

# we use the qpdf tool to unencrypt the files and return an 
# unencrypted file in the parent folder.
# to use, just pipe an ls or use a file name as argument

PASSWORD=

for FN in $*
do
	echo "Processing file: "${FN}""
	echo "..."
	qpdf --password="${PASSWORD}" --decrypt "${FN}" "../${FN%.pdf}_unencrypt.pdf"
done
