@echo off
cd c:\clases
streamlit run transporte_consumo.py -- server.port =8504 --server.address =0.0.0.0
pause