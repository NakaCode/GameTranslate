; PolyQuest — Inno Setup Script
; Gera: PolyQuest_Setup.exe

#define AppName      "PolyQuest"
#define AppVersion   "1.4"
#define AppPublisher "PolyQuest"
#define AppExeName   "PolyQuest.exe"
#define AppURL       ""

[Setup]
AppId={{C3F85216-229B-40E3-9F20-F54B59853029}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={localappdata}\{#AppName}
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
OutputDir=.
OutputBaseFilename=PolyQuest_Setup
SetupIconFile=icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=
WizardStyle=modern
WizardSizePercent=120
ShowLanguageDialog=no
LanguageDetectionMethod=none
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\{#AppExeName}
CloseApplications=yes
CloseApplicationsFilter={#AppExeName}
RestartApplications=no
VersionInfoDescription=PolyQuest - Overlay de traducao para jogadores
VersionInfoProductName=PolyQuest
VersionInfoProductVersion={#AppVersion}
MinVersion=10.0

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na &Area de Trabalho"; GroupDescription: "Atalhos adicionais:"
Name: "startupicon"; Description: "Iniciar com o &Windows automaticamente"; GroupDescription: "Atalhos adicionais:"; Flags: unchecked

[Files]
Source: "dist\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.json"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon_settings.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "install_ocr.ps1"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\{#AppExeName}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon
Name: "{userstartup}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: startupicon

[Run]
; Instala pacotes de idioma OCR automaticamente (en-US, pt-BR, es-ES)
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{tmp}\install_ocr.ps1"""; Flags: runhidden waituntilterminated; StatusMsg: "Instalando pacotes de idioma OCR do Windows..."
Filename: "{app}\{#AppExeName}"; Description: "Iniciar {#AppName} agora"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\crash.log"

[Code]
procedure InitializeWizard();
begin
  WizardForm.WelcomeLabel2.Caption :=
    'Este assistente vai instalar o ' + '{#AppName}' + ' no seu computador.' + #13#10 + #13#10 +
    'O PolyQuest e uma ferramenta de overlay que captura o texto na tela e exibe a traducao em portugues por cima, sem interferir no jogo.' + #13#10 + #13#10 +
    'Os pacotes de idioma OCR necessarios serao instalados automaticamente.';
end;
