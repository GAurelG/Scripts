#! /bin/bash

SOURCE_DIR="/mnt/albatros/"
SOURCE1="/mnt/albatros/var/snap/nextcloud/common"
SOURCE2="/mnt/albatros/var/snap/nextcloud/current"
DESTINATION="file:///baleine/albatros_backup/files"
ARCHIVE="/baleine/albatros_backup/duplicity/cache"
LOG="/baleine/albatros_backup/duplicity/log/$(date +"%Y%m")-nextcloud-backup.log"

echo "Starting backups for the:" $(date) >> "${LOG}"
# make a weekly full backup
duplicity --full-if-older-than 2W --no-encryption --archive-dir "${ARCHIVE}" --log-file "${LOG}" --include "${SOURCE1}" --include "${SOURCE2}" --exclude "**" "${SOURCE_DIR}" "${DESTINATION}"

echo -e "\nwe now check the integrity of the backup\n" >> "${LOG}"
duplicity verify --no-encryption --archive-dir "${ARCHIVE}" --include "${SOURCE1}" --exclude "**"  --include "${SOURCE2}" --exclude "**" "${DESTINATION}" "${SOURCE_DIR}"

# remove older than 9 months old backups
duplicity remove-older-than 5M --log-file "${LOG}" --force "${DESTINATION}" 

# make a tar.gz archive for the last year during the first backup of the year
LASTLOGZIPPED="/baleine/albatros_backup/duplicity/log/$(date +"%Y" --date='-1 year')-nextcloud-backup.tar.gz"
if [[ $(date +"%m") = "01" ]] &&  [[ ! -e "${LASTLOGZIPPED}" ]] 
then
	echo -e "\nAs it is the beginning of a new year we tar.gz \
		all the monthly log files\n" >> "${LOG}"
	tar czfv "${LASTLOGZIPPED}" /baleine/albatros_backup/duplicity/log/*.log \
		&& rm /baleine/albatros_backup/duplicity/log/*.log
fi

# I could encrypt the backups, I will need a GPG key

