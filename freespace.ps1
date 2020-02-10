#This script will tell you how much hardrive space is left on your hardrive in GB.
gwmi win32_volume -Filter 'drivetype = 3' | select driveletter, label, @{LABEL='GBfreespace';EXPRESSION={"{0:N2}" -f ($_.freespace/1GB)}}
