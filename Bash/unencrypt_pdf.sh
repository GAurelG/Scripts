#! /bin/bash

# we use the qpdf tool to unencrypt the files and return an 
# unencrypted file in the parent folder.
# to use, /script [PASSWORD] $(ls) in the folder with the encryptded pdfs
# the first argument *must* be the password!

PASSWORD="${1}"

shift 1

for FN in $*
do
	echo "Processing file: "${FN}""
	echo "..."
	qpdf --password="${PASSWORD}" --decrypt "${FN}" "../${FN%.pdf}_unencrypt.pdf"
done
