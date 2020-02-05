function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
function getUser{
    $env:USERNAME
}
function getcurrentDate{
    Get-Date
}
function getComputerName{
    $env:COMPUTERNAME
}
function getPSversion{
    $Host.Version
}

$IP = getIP
$User = getUser
$PSVersion = getPSversion
$Hostname = getComputerName
$Date = getCurrentDate


Send-MailMessage -To "bergmacr@mail.uc.edu" -From "cambergman7706@gmail.com" -Subject "IT3038C Windows SysInfo" -Body "This machine's IP is:($IP). The current user is:($User). The version of Powershell is:($PSversion). The hostname of the machine is:($Hostname). The current date is:($Date)" -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)