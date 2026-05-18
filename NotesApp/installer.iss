; Inno Setup script for Notes app
; Compile with: iscc installer.iss
; Output:       Output\NotesApp-Setup.exe

#define AppName      "Notes"
#define AppVersion   "1.0.0"
#define AppPublisher "Notes App"
#define AppExe       "NotesApp.exe"
#define AppId        "{{B5F8A2C3-1D4E-4F6B-8A9C-2D3E4F5A6B7C}"

[Setup]
AppId={#AppId}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher={#AppPublisher}
VersionInfoVersion={#AppVersion}

; Install to Program Files (admin) or AppData\Local\Programs (non-admin)
DefaultDirName={autopf}\{#AppName}
DefaultGroupName={#AppName}
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesInstallIn64BitMode=x64

; Installer appearance
WizardStyle=modern
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\{#AppExe}
UninstallDisplayName={#AppName}

; Output
OutputDir=Output
OutputBaseFilename=NotesApp-Setup
Compression=lzma2/ultra64
SolidCompression=yes

; Control Panel entry
AppSupportURL=https://github.com/
AppUpdatesURL=https://github.com/

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
; Desktop shortcut is checked by default
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; \
  GroupDescription: "{cm:AdditionalIcons}"

[Files]
; Everything from the PyInstaller --onedir output folder
Source: "dist\NotesApp\*"; DestDir: "{app}"; \
  Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Start Menu
Name: "{group}\{#AppName}";              Filename: "{app}\{#AppExe}"
Name: "{group}\Uninstall {#AppName}";   Filename: "{uninstallexe}"
; Desktop shortcut (only if task selected above)
Name: "{autodesktop}\{#AppName}";        Filename: "{app}\{#AppExe}"; \
  Tasks: desktopicon

[Run]
; Offer to launch the app after installation
Filename: "{app}\{#AppExe}"; \
  Description: "{cm:LaunchProgram,{#StringChange(AppName, '&', '&&')}}"; \
  Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Remove user-data only if the user explicitly checks the box —
; instead, just clean up any empty install-dir artefacts.
Type: dirifempty; Name: "{app}"
