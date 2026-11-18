# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Desenvolva uma API REST em Python usando FastAPI para cadastrar e consultar livros. Depois, amplie a API com operações de atualização e exclusão, praticando rotas HTTP, validação de dados e códigos de status.

## 📝 Tarefas

### 🛠️ Criar o modelo e os endpoints de consulta e cadastro

#### Descrição
Complete o código inicial em `starter-code.py` para definir os modelos de livro e criar os endpoints para listar, consultar e cadastrar livros. Instale as dependências e inicie a API com:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Use a documentação interativa em `http://127.0.0.1:8000/docs` para testar os endpoints.

#### Requisitos
O programa concluído deve:

- Definir um modelo de entrada `BookCreate` com os campos `title`, `author` e `year`.
- Implementar `GET /books` para retornar todos os livros cadastrados.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID ou responder com status `404` quando ele não existir.
- Implementar `POST /books` para cadastrar um livro com um ID gerado pela aplicação e responder com status `201`.
- Manter os livros em memória enquanto a API estiver em execução.

### 🛠️ Atualizar e excluir livros

#### Descrição
Amplie a API com endpoints para substituir os dados de um livro existente e removê-lo pelo ID. Trate as solicitações para IDs que não estejam cadastrados.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar o título, autor e ano de um livro existente.
- Implementar `DELETE /books/{book_id}` para excluir um livro existente e responder com status `204`.
- Responder com status `404` ao tentar atualizar ou excluir um ID inexistente.
- Permitir testar as operações de atualização e exclusão pela documentação interativa em `/docs`.