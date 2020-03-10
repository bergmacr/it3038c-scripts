I went with the carbon module. The carbon module adds even more automated system admin processes that the normal install of PowerShell won't have.

Here is how to install Carbon from a PS window.

Install-Module -Name 'Carbon' -AllowClobber
Import-Module 'Carbon'
---------------------------------------------------------------
Processes:
Here is how to get the permissions of a file, directory, etc. to a specified path. (To test this command yourself, replace the file path with whatever you would like, as I put in my own sample info.)

Get-Permission -Path 'C:\it3038c-scripts\Lab7\permissions.txt'
---------------------------------------------------------------
Here is how to create a directory. If a directory with the given name already exists, this command does nothing. It also creates any parent directories that may not have existed before.

Install-Directory -Path 'C:\it3038c-scripts\Lab7\NewDirectory'
---------------------------------------------------------------
Lastly, this is how to get the IPv4 address of the local machine the command is being run on.

Get-IPAddress -V4
