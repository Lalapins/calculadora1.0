#!/bin/bash
# Executa a calculadora a partir de qualquer pasta.
cd "$(dirname "$0")" || exit 1
python3 calculadora.py
