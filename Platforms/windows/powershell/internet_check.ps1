# to test and check internet connectivity due to misleading "Connected" status in Windows

param (
    [string] $targetHost = "8.8.8.8",
    [ValidateRange(1, 10)]
    [int] $pingCount = 4
    
)

# Ensure Count is always >= 1
if ($Count -lt 1) { $Count = 1 }

Try {
   $ping = Test-Connection -ComputerName $TargetHost -Count $Count -Quiet 
   if ($ping) {
        Write-Output "Internet Connectivity Status: Connected"
        $logfile = "$env:USERPROFILE\Desktop\internet_check_log.txt"
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path $LogFile -Value "$timestamp - $TargetHost - Available"
   }
}
Catch {
    Write-Error "Ping test failed: $_"
}

if ($ping) {
    exit 0
} else {
    exit 1
}