@echo off
setlocal enabledelayedexpansion

set quality=80

set source_folder=C:\Users\Usuario\Desktop\face\muestra

set destination_folder=C:\Users\Usuario\Desktop\face\webp80

if not exist "%destination_folder%" mkdir "%destination_folder%"

for %%i in ("%source_folder%\*.png") do (
  set filename=%%~ni
  cwebp -q %quality% "%%i" -o "%destination_folder%\!filename!.webp"
)

echo Conversión completada.
pause
