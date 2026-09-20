@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title Projeto 1 - Calculadora
cd /d "%~dp0calculadora"

rem Tenta primeiro o launcher "py" e depois o comando "python"
where py >nul 2>nul
if %errorlevel%==0 (
    py calculadora.py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python calculadora.py
    ) else (
        echo.
        echo Python nao foi encontrado neste computador.
        echo Baixe em https://www.python.org/downloads/
        echo e marque "Add Python to PATH" durante a instalacao.
    )
)

echo.
pause
