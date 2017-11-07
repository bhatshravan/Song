cd C:\Users\Shravan Bhat\Desktop\Songs\Downloads\
@echo off

if [%1]==[] goto usage
python sargs.py %1
goto :eof
:usage
python sdown2.py
exit /B 1
cd C:\Users\Shravan Bhat
