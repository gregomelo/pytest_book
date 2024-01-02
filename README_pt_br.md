# Python Testing with pytest - Estudos e Práticas

Este repositório contém minhas respostas e estudos baseados no livro ["Python Testing with pytest"](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/). O objetivo é aplicar e aprofundar os conhecimentos adquiridos ao longo da leitura, praticando os conceitos e técnicas apresentados no livro.

## Aprendizado e Uso do Git

Estou alimentando esse repositório gradualmente, conforme avanço no livro. Este processo também está me ajudando a aprender e praticar o uso do Git, garantindo que cada etapa do aprendizado seja documentada e versionada adequadamente.

## Qualidade do Código com Pre-commit

Para melhorar a qualidade do código e garantir boas práticas, o repositório está configurado com a ferramenta `pre-commit`. Aqui estão alguns dos hooks configurados:

- **Trailing Whitespace**: Remove espaços em branco no final das linhas.
- **End-of-file Fixer**: Garante que os arquivos terminem com uma linha em branco.
- **Check YAML**: Checa a correta formatação de arquivos YAML.
- **Check Added Large Files**: Previne a adição acidental de arquivos grandes.
- **Debug Statements**: Detecta e impede commits que contenham declarações de debug.
- **Detect Private Key**: Previne o commit acidental de chaves privadas.
- **Name Tests Test**: Assegura que os arquivos de teste sejam nomeados corretamente.
- **Requirements-txt-fixer**: Ajusta automaticamente o arquivo `requirements.txt`.
- **Isort**: Organiza automaticamente as importações.
- **Pydocstyle**: Verifica a conformidade dos docstrings com os padrões de estilo.
- **Add Trailing Comma**: Adiciona vírgulas no final das listas ou dicionários.
- **Autopep8**: Formata automaticamente o código conforme o PEP 8.
- **Flake8**: Checa o código para seguir as diretrizes do PEP 8.
- **Mypy**: Verifica a tipagem estática do código.
- **Bandit**: Ferramenta de análise estática de segurança do código.
- **Commitizen**: Auxilia na criação de mensagens de commit padronizadas.

### Revisão Contínua da Configuração

O arquivo de configuração do `pre-commit` está em constante revisão. À medida que encontro erros ou conflitos na etapa de commit, faço ajustes para manter o equilíbrio entre a qualidade do código e a usabilidade prática.
