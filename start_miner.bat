@echo off
echo ========================================
echo    MTG Market Watcher - Data Miner
echo ========================================
echo.
echo Executando mineracao de dados...
echo.

cd miner
python run_miner.py

echo.
echo Pressione qualquer tecla para sair...
pause > nul