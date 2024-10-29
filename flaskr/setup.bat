@echo off
REM
IF NOT EXIST "venv\" (
    echo Criando o ambiente virtual...
    python -m venv venv
)

REM
echo Ativando o ambiente virtual...
call venv\Scripts\activate

REM
IF EXIST "requirements.txt" (
    echo Instalando as dependências do requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt não encontrado. Instale as dependências manualmente.
)

echo Ambiente configurado com sucesso!
