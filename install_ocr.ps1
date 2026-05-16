$langs = @('en-US','pt-BR','es-ES')
foreach ($l in $langs) {
    $name = "Language.OCR~~~${l}~0.0.1.0"
    $cap = Get-WindowsCapability -Online -Name $name
    if ($cap.State -ne 'Installed') {
        Add-WindowsCapability -Online -Name $name
    }
}
