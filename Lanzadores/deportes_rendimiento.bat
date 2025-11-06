@echo off
cd c:\clases
streamlit run deportes_rendimiento.py -- server.port =8503 --server.address =0.0.0.0
pause