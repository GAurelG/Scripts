#! /bin/bash

SOURCE1="/home/backaurel/mntAlbatros/var/snap/nextcloud/common"
SOURCE2="/home/backaurel/mntAlbatros/var/snap/nextcloud/current"
DESTINATION="file:///media/marmotte1/albatros02_backup"
ARCHIVE="/media/marmotte1/duplicity/cache"
LOG="/media/marmotte1/duplicity/log/$(date +"%Y%m")-nextcloud-backup.log"

echo "Starting backups for the:" $(date) >> "${LOG}"
# make a weekly full backup
duplicity --full-if-older-than 2W --no-encryption --archive-dir "${ARCHIVE}" --log-file "${LOG}" --include "${SOURCE1}" --include "${SOURCE2}" --exclude "**" /home/backaurel/mntAlbatros/ "${DESTINATION}"

echo -e "\nwe now check the integrity of the backup\n" >> "${LOG}"
duplicity verify --no-encryption --archive-dir "${ARCHIVE}" --include "${SOURCE1}" --exclude "**"  --include "${SOURCE2}" --exclude "**" "${DESTINATION}" /home/backaurel/mntAlbatros/

# remove older than 9 months old backups
duplicity remove-older-than 5M --log-file "${LOG}" --force "${DESTINATION}" 

# make a tar.gz archive for the last year during the first backup of the year
LASTLOGZIPPED="/media/marmotte1/duplicity/log/$(date +"%Y" --date='-1 year')-nextcloud-backup.tar.gz"
if [[ $(date +"%m") = "01" ]] &&  [[ ! -e "${LASTLOGZIPPED}" ]] 
then
	echo -e "\nAs it is the beginning of a new year we tar.gz \
		all the monthly log files\n" >> "${LOG}"
	tar czfv "${LASTLOGZIPPED}" /media/marmotte1/duplicity/log/*.log \
		&& rm /media/marmotte1/duplicity/log/*.log
fi

# I could encrypt the backups, I will need a GPG key

