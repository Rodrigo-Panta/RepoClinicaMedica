# RepoClinicaMedica

# Instalação: 
  
  Para rodar o projeto, será utilizado um ambiente virtual, que concentra a instalação das dependências necessárias, evitando conflitos de versionamento com outros projetos instaladas na máquina do desenvolvedor.
  
  1. Faça Fork do projeto e o clone em um diretório desejado.
  
  2. Instale uma versão de Python 3, de preferência a 3.10.8 para Windows. Segue o link para download.
    
    https://www.python.org/downloads/
  
  3. Verifique a instalação do software Python e do gerenciador de pacotes pip. Em um terminal, execute:
    
    
    python --version
    
    pip --version
    
  
  4. Instale o pacote virtualenv do Python para que seja possível criar e utilizar ambientes virtuais. Em um terminal, execute o comando:
    
    
    pip install virtualenv
    
   
  5. Quando finalizar a instalação, navegue pelo terminal até o diretório raiz do projeto (<CaminhoParaOProjeto>/RepoClinicaMedica) e crie um novo ambiente virtual: 
 
    
    python -m venv venv/clinicamedica   
    
    
   Note que a pasta venv foi criada. O ambiente virtual já foi criado.
  
  6. Ative o ambiente virtual executando o script de ativação, que fica em venv/clinicamedica/Scripts. Do diretório raiz do projeto, basta executar no terminal:
     
     ```
     venv/clinicamedica/Scripts/activate
     ```
  
     Se tudo ocorreu bem, agora o nome do ambiente virtual aparece em verde antes do caminho do diretório atual no terminal:
     <p align="center"><img width="25%" align="center" src="https://github.com/Rodrigo-Panta/RepoClinicaMedica/blob/main/images/venv.png" />
     </p>
     
     Você pode desativar o ambiente virtual a qualquer momento de qualquer diretório utilizando o comando "deactivate" no terminal. Para ativá-lo novamente, é só seguir o passo 6.  
  
  7. Agora que o ambiente virtual está ativo, basta instalar as dependências necessárias que estão listadas no arquivo requirements.txt. Ainda na raiz do projeto, execute:
  
    pip install -r requirements.txt
  
  8. Agora, todos os passos da instalação já foram completos. Para checar se o projeto está funcional, navegue até a pasta clínica médica, execute os comandos de migração do banco de dados e inicie o servidor Django (Caso receba um erro indicando tabelas de banco de dados inexistentes, execute python manage.py migrate --run-syncdb):
    
    cd clinicamedica
    python manage.py makemigrations
    python manage.py migrate 
    python manage.py runserver
  
  9. Abra um navegador e acesse o endereço de IP mostrado na saída do terminal. 
    
