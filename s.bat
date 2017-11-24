@echo off

if "%1"=="b" goto bin
if "%1"=="s" goto shut
if "%1"=="apk" goto apk
if "%1"=="d" goto do
if "%1"=="bl" goto ble
if "%1"=="help" goto opt
if "%1"=="git" goto git
if "%1"=="son" goto son
if "%1"=="jd" goto jd
if "%1"=="prgm" goto prgm
if [%1]==[] goto des

:prgm
@echo on
E:
cd shravan\programming\project\node
exit /b 1

:ble
%SystemRoot%\explorer.exe "F:\movies\Bleach Complete Series + Movies\Season 14; The Arrancar 5; Downfall"
exit
exit /B 1

:do
%SystemRoot%\explorer.exe "E:\Downloads"
exit
exit /B 1

:git
%SystemRoot%\explorer.exe "F:\Downloads"
exit
exit /B 1

:son
%SystemRoot%\explorer.exe "E:\Songs"
exit
exit /B 1

:des
cd C:/Users/Shravan Bhat/Desktop
exit /B 1

:opt
echo Enter bin for cd C:/Bin & echo.s for shutdown& echo.apk for apktool& echo.jd for dex2jar& echo.nothing for switching to desktop& echo.ble for bleach& echo. d for going to E:/Downloads
echo son for going to songs & echo.git for F:/Downloads &echo.prgm for E:\shravan\programming\project\node
exit /B 1


:shut
shutdown -s -c "Shutting down"
exit /B 1

:apk
C:/Bin/APKTOOL/apktool d %2
exit /B 1

:jd
C:/Bin/APKTOOL/d2j/d2j-dex2jar -d %2
exit /B 1

:bin
cd C:/Bin
exit /B 1