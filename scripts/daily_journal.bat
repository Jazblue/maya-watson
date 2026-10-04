@echo off
cd /d "C:\Users\Administrator\maya-site"
set TODAY=%DATE%
echo [%DATE% %TIME%] Generating journal entry...

git status
if not "%ERRORLEVEL%"=="0" (
    echo Git error
    exit /b 1
)

git add .
git commit -m "Daily journal entry for %DATE%"
git push origin main

echo Journal entry committed and pushed.
