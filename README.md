# 🧩 API Design Team Flow (Backend)

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-REST%20Framework-red?logo=django)](https://www.django-rest-framework.org/)
[![Swagger](https://img.shields.io/badge/Swagger-Automático-brightgreen?logo=swagger)](https://swagger.io/)

---

## 📘 Visão Geral

A **API Design Team Flow** é uma API **RESTful** desenvolvida para gerenciar demandas de um time de design.  
Ela permite **criar, listar, atualizar e excluir tarefas (CRUD)**, servindo como backend robusto para:

- Sistemas Kanban  
- Dashboards de produtividade  
- Aplicações de gestão de tarefas  

A API foi construída com **Django + Django REST Framework**, incluindo documentação automática via **Swagger**.

---

## 📦 Pacotes Utilizados

| Pacote               | Função                                      |
|----------------------|----------------------------------------------|
| **Django**           | Framework web principal                      |
| **djangorestframework** | Toolkit para construção da API REST     |
| **drf-yasg**         | Geração automática da documentação Swagger   |
| **django-cors-headers** | Controle de acesso HTTP (CORS)          |

---

## 📁 Estrutura do Projeto

projeto_api/ ├── manage.py ├── requirements.txt ├── setup/                  # Configurações Globais │   ├── settings.py │   └── urls.py             # Rotas (inclui Swagger) └── apps/ └── core/               # Aplicação Principal ├── models.py       # Modelo 'Tarefa' com tags ├── views.py        # ViewSets (Lógica CRUD) ├── serializers.py  # Conversão JSON └── urls.py         # Rotas da API (/tarefas/)


---

## 📚 Documentação da API

A documentação interativa é gerada automaticamente pelo **drf-yasg** e pode ser acessada na raiz do projeto:

- Swagger UI → **http://127.0.0.1:8000/**
- Redoc → **http://127.0.0.1:8000/redoc/**

---

## 🔗 Endpoints Principais

| Método | Endpoint              | Descrição                               |
|--------|------------------------|-------------------------------------------|
| GET    | `/api/tarefas/`       | Lista todas as tarefas                    |
| POST   | `/api/tarefas/`       | Cria uma nova demanda                     |
| GET    | `/api/tarefas/{id}/`  | Detalhes de uma tarefa específica         |
| PUT    | `/api/tarefas/{id}/`  | Atualiza todos os campos de uma tarefa    |
| DELETE | `/api/tarefas/{id}/`  | Remove uma tarefa                         |

---

## 🛠️ Configuração do Ambiente

### 1️⃣ Instale as dependências

```bash
pip install -r requirements.txt

2️⃣ Aplique as migrações

python manage.py migrate

3️⃣ Inicie o servidor

python manage.py runserver

4️⃣ Acesse a documentação 

Acesse a documentação interativa gerada automaticamente pelo Swagger:
• 	http://127.0.0.1:8000/
• 	http://127.0.0.1:8000/redoc/