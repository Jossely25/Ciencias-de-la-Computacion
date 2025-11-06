@echo off
cd c:\clases
streamlit run Banco.py -- server.port =8507 --server.address =0.0.0.0
pause