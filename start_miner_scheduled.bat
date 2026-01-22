@echo off
echo ========================================
echo    MTG Market Watcher - Data Miner
echo         (Execucao Agendada)
echo ========================================
echo.
echo Iniciando mineracao automatica...
echo O minerador executara a cada 30 minutos.
echo Pressione Ctrl+C para parar.
echo.

cd miner
python run_miner.py --schedule