# 🗄️ Módulo 05: Banco de Dados e SQL

## Conceitos Fundamentais
* **banco de dados:** é organizado para armazenar dados de forma estruturada e eficiente, facilitando consultas e manutenção.
* **SGBD:** Software que gerencia e protege os dados (ex: PostgreSQL, MySQL, SQLite).
* **Estrutura:** Banco de Dados, Tabelas, Colunas (atributos) e Linhas (registros).
* **Chave Primária (PK):** Identificador único de cada linha na tabela (ex: `id`).
* **Relacionamentos Entre Tabelas:** `1:1` (Um para Um), `1:N` (Um para Muitos) e `N:N` (Muitos para Muitos, usando tabela associativa).

---

## Propriedades ACID (Transações)
Garantem que uma transação (sequência indivisível de operações) seja confiável:

1. **Atomicity (Atomicidade):** Princípio do "tudo ou nada". Se uma etapa falhar, tudo é desfeito (*rollback*).
2. **Consistency (Consistência):** O banco só passa de um estado válido para outro, respeitando chaves e regras.
3. **Isolation (Isolamento):** Impede que transações simultâneas interfiram umas nas outras (evitando *Dirty Read*, *Non-repeatable Read* e *Phantom Read*).
4. **Durability (Durabilidade):** Após confirmados (*commit*), os dados permanecem salvos mesmo se houver queda de energia (via *WAL - Write-Ahead Logging*).

---

## Comandos Essenciais SQL (SQLite)
* SQLite é um banco de dados leve, que armazena os dados em um único arquivo, ideal paraaplicações pequenas e testes. Ele suporta comandos SQL padrão para criação, inserção e consulta de dados.

### Criar e Apagar Tabelas
```sql
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE
);

DROP TABLE autores;
```

### CRUD (Inserir, Consultar, Atualizar e Deletar)
```sql
-- 1. INSERIR DADOS
-- ⚠️ [CORREÇÃO: Estava escrito "INSEERT INTO ... VALUE(...)". O correto é INSERT e VALUES]
INSERT INTO autores (nome, email) VALUES ('Caio', 'email@gmail.com');

-- 2. CONSULTAR DADOS
SELECT * FROM autores;
SELECT nome FROM autores WHERE nome LIKE '%Caio%';

-- 3. ATUALIZAR DADOS
UPDATE autores
SET nome = 'Caio Silva'
WHERE id = 1;

-- 4. DELETAR DADOS (Sempre use WHERE para não apagar a tabela inteira!)
DELETE FROM autores WHERE id = 1;
```

---

## Integração com Python
* Ao desenvolver aplicações que interagem com bancos de dados relacionais, é comum se deparar com duas abordagens principais:
escrever SQL direto (SQL puro) ou utilizar um ORM (Object-Relational Mapping).

### SQL Direto:
* **SQL Direto:** O Python envia comandos SQL puros através de um driver/conector (como o módulo nativo `sqlite3`).

Python   => SQL => Banco de Dados
![alt text](<Screenshot 2026-11-17 135526.png>)

* No SQL direto, o desenvolvedor escreve manualmente as queries para inserir, consultar, atualizar e deletar dados.

### ORM:
* **ORM (*Object-Relational Mapping*):** Ferramentas (como *SQLAlchemy* ou *Django ORM*) que permitem manipular tabelas do banco usando classes e objetos Python em vez de escrever SQL manual.

Python  => ORM => SQL => Banco de Dados
![alt text](<Screenshot 2026-11-17 141106.png>)

**Comparação Direta:**

