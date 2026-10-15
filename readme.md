# 🌊 Monitoramento de Nível de Reservatório de Água

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Colorama](https://img.shields.io/badge/Colorama-000000?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

Sistema simples em Python para simulação e monitoramento de níveis de água de um reservatório, exibindo alertas visuais e coloridos no terminal conforme o grau de risco.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte de uma atividade prática de programação. O objetivo é simular o monitoramento da água de um reservatório utilizando cores no terminal para destacar o estado do reservatório de forma clara e visual.

### 🎨 Tabela de Cores e Alertas

| Nível | Situação | Cor |
| :---: | :---: | :---: |
| **1** | Muito Baixo (Crítico) | 🔴 Vermelho |
| **2** | Baixo | 🟡 Amarelo |
| **3** | Médio | 🟢 Verde |
| **4** | Alto | 🔵 Ciano |
| **5** | Muito Alto (Alerta) | 🟦 Azul |

---

## 🛠️ Tecnologias e Bibliotecas Usadas

* **[Python 3](https://www.python.org/)** — Linguagem principal
* **[Colorama](https://pypi.org/project/colorama/)** — Estilização e cores no terminal
* **[Random](https://docs.python.org/3/library/random.html)** — Sorteio aleatório de níveis para simulação
* **[OS](https://docs.python.org/3/library/os.html)** — Limpeza do console do sistema operacional

---

## 📋 Requisitos Funcionais Atendidos

- [x] Uso de listas para armazenar os níveis e mensagens.
- [x] Importação e uso da biblioteca `colorama`.
- [x] Função dedicada para atribuição de cor/mensagem de acordo com o nível.
- [x] Exibição formatada no terminal.
- [x] Restauração do estilo do terminal (`Style.RESET_ALL`).
- [x] Simulação com todos os níveis e simulação com nível aleatório.