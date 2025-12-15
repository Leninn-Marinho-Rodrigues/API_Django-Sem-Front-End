Design Team Flow - Sistema Kanban com Django

Índice

Visão Geral

Funcionalidades

Configuração do Ambiente

Estrutura do Projeto

Endpoints da API

Execução Local

Deploy

Visão Geral

Este é um sistema de Gestão de Tarefas (Kanban) desenvolvido especificamente para times de design. Ele permite o gerenciamento visual de demandas com recursos modernos como "Arrastar e Soltar", categorização por Tags coloridas e estatísticas em tempo real.

O projeto utiliza Django no backend para servir uma API RESTful, enquanto o frontend consome esses dados para renderizar uma interface reativa estilizada com TailwindCSS.

Funcionalidades

✅ Quadro Kanban Interativo: Mova tarefas entre "Backlog", "Em Produção" e "Finalizado" arrastando os cartões.
✅ Sistema de Tags Inteligente: Classifique demandas (ex: Urgente, Instagram, TikTok) com cores automáticas.
✅ Dashboard de Métricas: Contadores em tempo real no topo da página.
✅ Filtros Avançados: Pesquise por texto, tags específicas, data exata ou navegue por mês.
✅ Atualização em Tempo Real: O quadro se atualiza automaticamente (polling) quando outros usuários fazem alterações.
✅ Interface Responsiva: Funciona bem em desktops e dispositivos móveis.

Configuração do Ambiente

1. Pré-requisitos

Certifique-se de ter o Python instalado:

python --version


2. Clonar o repositório

git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio


3. Criar Ambiente Virtual

Windows:

python -m venv venv
venv\Scripts\activate


Linux/Mac (Codespaces):

python -m venv venv
source venv/bin/activate


4. Instalar Dependências

pip install -r requirements.txt


Estrutura do Projeto

A organização segue as boas práticas do Django (MTV):

projeto_django/
├── .venv/                    # Ambiente Virtual
├── db.sqlite3                # Banco de Dados (Desenvolvimento)
├── manage.py                 # Utilitário de comando do Django
├── requirements.txt          # Lista de bibliotecas
├── build.sh                  # Script de deploy para o Render
├── setup/                    # (Projeto Principal)
│   ├── __init__.py
│   ├── settings.py           # Configurações globais (Apps, DB, Middleware)
│   ├── urls.py               # Rotas principais (Admin, API, Home)
│   └── wsgi.py               # Entrada para servidor web
└── apps/                     # (Pasta de Aplicações)
    └── core/                 # (App Principal: Gestão de Tarefas)
        ├── templates/        # Arquivos HTML
        │   └── interface_kanban.html
        ├── admin.py          # Configuração do painel administrativo
        ├── models.py         # Modelo do Banco de Dados (Tabela Tarefa)
        ├── serializers.py    # Conversão de Dados (Model <-> JSON)
        ├── views.py          # Lógica da API (ViewSets)
        └── urls.py           # Rotas específicas do App


setup/ - Pasta do PROJETO Django

Esta é a pasta de configuração que "amarra" todo o sistema.

settings.py: Define o banco de dados, apps instalados (apps.core, rest_framework) e configurações de segurança (CSRF, CORS).

urls.py: Define que a rota /api/ vai para o nosso app e a rota / (raiz) carrega o template do Kanban.

apps/core/ - Pasta da APLICAÇÃO

Onde a lógica de negócio reside.

models.py: Define a estrutura da Tarefa (título, descrição, prazo, tags, status).

views.py: Utiliza ModelViewSet do Django REST Framework para criar automaticamente as operações de CRUD (Criar, Ler, Atualizar, Deletar).

templates/: Contém o arquivo HTML único que roda todo o frontend via JavaScript (fetch API).

Endpoints da API

O sistema expõe uma API REST completa em /api/tarefas/.

Método

Endpoint

Descrição

GET

/api/tarefas/

Lista todas as tarefas (JSON)

POST

/api/tarefas/

Cria uma nova tarefa

GET

/api/tarefas/{id}/

Detalhes de uma tarefa

PUT

/api/tarefas/{id}/

Atualiza uma tarefa completa

PATCH

/api/tarefas/{id}/

Atualiza parcial (ex: mudar status ao arrastar)

DELETE

/api/tarefas/{id}/

Remove uma tarefa

Execução Local

1. Aplicar Migrações

Cria as tabelas no banco de dados SQLite:

python manage.py makemigrations
python manage.py migrate


2. Criar Superusuário (Opcional)

Para acessar o painel administrativo (/admin):

python manage.py createsuperuser


3. Rodar o Servidor

python manage.py runserver


Acesse no navegador:

Kanban: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Deploy

O projeto está configurado para deploy automático na plataforma Render.

Arquivos de Configuração

requirements.txt: Lista o gunicorn (servidor de produção).

build.sh: Script que instala dependências e roda migrações automaticamente no servidor.

settings.py: Configurado com STATIC_ROOT para servir arquivos estáticos corretamente.

Desenvolvido como Projeto Integrador de Desenvolvimento Web.