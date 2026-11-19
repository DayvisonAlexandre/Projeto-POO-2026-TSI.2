# PySide6 no GitHub Codespaces — Fluxbox + VNC

Projeto de demonstração da atividade **Config do Codespaces + PySide6 + Fluxbox + VNC**.

O projeto configura um ambiente Linux no GitHub Codespaces, instala o PySide6 e utiliza a funcionalidade `desktop-lite` para disponibilizar um desktop Fluxbox por meio do noVNC no navegador.

## 1. Estrutura do projeto

```text
PySide6_Codespaces_Fluxbox/
├── .devcontainer/
│   └── devcontainer.json
├── exemplos/
│   ├── app0_basico.py
│   └── app1_com_botao.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Importante:** mantenha o nome `.devcontainer` exatamente assim e coloque `devcontainer.json` dentro dessa pasta. O arquivo `app.py` fica na raiz do repositório.

## 2. Criar o repositório no GitHub

1. Entre em sua conta do GitHub.
2. Crie um repositório para a atividade. Ele pode ser privado; não é necessário torná-lo público para executar o Codespaces.
3. Envie todos os arquivos desta pasta para a raiz do repositório, preservando a estrutura apresentada acima.
4. Confira se o GitHub mostra o caminho `.devcontainer/devcontainer.json` e o arquivo `app.py` na raiz.

## 3. Criar o Codespace

1. Abra o repositório no GitHub.
2. Clique em **Code** e depois na aba **Codespaces**.
3. Selecione **Create codespace on main** (ou o nome da branch principal do seu repositório).
4. Aguarde a criação do contêiner e a execução do `postCreateCommand`. Esse processo instala as bibliotecas de sistema necessárias e o PySide6.
5. Quando o VS Code do navegador estiver pronto, abra o terminal integrado.

Se o Codespace já existia antes de adicionar ou alterar `.devcontainer/devcontainer.json`, use a paleta de comandos (`Ctrl+Shift+P`) e execute **Codespaces: Rebuild Container** para reconstruir o ambiente com a configuração atualizada.

## 4. Abrir o desktop Fluxbox pelo VNC

1. No VS Code do Codespaces, abra a aba **PORTS** (ao lado de Terminal).
2. Localize a porta **6080**, identificada como **noVNC Desktop (Fluxbox)**. Se ela não aparecer, aguarde alguns instantes ou adicione a porta `6080` manualmente.
3. Clique no ícone de globo (**Open in Browser**) da porta 6080.
4. Na página do noVNC, clique em **Connect**.
5. Quando for solicitada a senha, use a senha padrão da funcionalidade `desktop-lite`: `vscode`.
6. Deve aparecer o desktop Fluxbox no navegador. Mantenha essa aba aberta.

A porta encaminhada pelo Codespaces normalmente fica privada por padrão. Não altere sua visibilidade para pública sem necessidade.

## 5. Executar a aplicação PySide6

Volte à aba do VS Code/Codespaces, abra o terminal na pasta raiz do projeto e execute:

```bash
python app.py
```

Volte à aba do noVNC. A janela **PySide6 no GitHub Codespaces** deverá aparecer no desktop Fluxbox com a mensagem:

```text
Olá do GitHub Codespaces!
```

Clique em **Clique Aqui**. O rótulo deverá mudar para:

```text
PySide6 funcionando!
Sinal e slot executados com sucesso.
```

Isso demonstra que a janela gráfica foi criada e que o sinal `clicked` do botão está conectado à ação que atualiza o rótulo.

Para encerrar a aplicação, volte ao terminal e pressione `Ctrl+C`.

## 6. Testar os exemplos opcionais

Os dois arquivos em `exemplos/` reproduzem os passos iniciais fornecidos na atividade:

```bash
python exemplos/app0_basico.py
```

ou

```bash
python exemplos/app1_com_botao.py
```

Execute apenas um programa por vez. A aplicação principal a ser demonstrada é `app.py`.

## 7. Se o PySide6 não estiver instalado

Na raiz do projeto, execute:

```bash
python -m pip install -r requirements.txt
```

Se ocorrer erro de biblioteca gráfica após alteração do `devcontainer.json`, reconstrua o contêiner usando **Codespaces: Rebuild Container** e aguarde o `postCreateCommand` terminar.

## 8. Solução de problemas

### A porta 6080 não aparece

- Abra a aba **PORTS** e adicione manualmente a porta `6080`.
- Confira se o Codespace terminou de iniciar.
- Recarregue a lista de portas e tente abrir a porta pelo ícone de globo.

### O noVNC abre, mas não conecta

- Aguarde alguns segundos e tente novamente.
- Atualize a página do noVNC e clique em **Connect**.
- Confira se está usando a senha padrão `vscode`.
- Se continuar sem funcionar, reinicie/reconstrua o Codespace.

### A janela não aparece no Fluxbox

No terminal, confira o display configurado:

```bash
echo "$DISPLAY"
```

Com `desktop-lite`, o valor esperado é `:1`. Depois, execute novamente:

```bash
python app.py
```

### Erro `No module named 'PySide6'`

Execute:

```bash
python -m pip install -r requirements.txt
```

### Erro de plugin ou biblioteca `xcb`

Reconstrua o contêiner para que o `postCreateCommand` instale as dependências de interface gráfica definidas no `.devcontainer/devcontainer.json`.

## Referências

- Material da atividade: **Estudo Dirigido de Interface Gráfica do Usuário (GUI) com Qt e PySide6**, especialmente seção 2, páginas 6–7.
- Qt for Python — documentação oficial: https://doc.qt.io/qtforpython-6/
- PySide6 — tutorial de sinais e slots: https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html
- Dev Containers — desktop-lite: https://github.com/devcontainers/features/tree/main/src/desktop-lite
- PythonGUIs — tutorial PySide6 indicado pelo professor: https://www.pythonguis.com/pyside6-tutorial/#menu
