@echo off
title Transkriptor

echo.
echo  ================================================
echo   Transkriptor - Kurulum ve Baslat
echo  ================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo  HATA: Python bulunamadi! python.org adresinden indirin.
    pause
    exit /b
)

echo  Gerekli kutuphaneler kontrol ediliyor...

pip show flask >nul 2>&1
if errorlevel 1 (
    echo  Flask yukleniyor...
    pip install flask --quiet
)

pip show openai-whisper >nul 2>&1
if errorlevel 1 (
    echo  Whisper yukleniyor, bu biraz surebilir...
    pip install openai-whisper --quiet
)

pip show werkzeug >nul 2>&1
if errorlevel 1 (
    pip install werkzeug --quiet
)

echo.
echo  Hazir! Tarayicinizda aciliyor: http://localhost:5000
echo.
start "" "http://localhost:5000"
python app.py

pause
