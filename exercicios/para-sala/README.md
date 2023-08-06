# Exercício de Sala 🏫  

## Nome do Exercicio

- Introdução ao terminal e conceitos básicos de navegaçao e manipulacao de arquivos.
- Criando um repositiro remoto
- Criando um repositorio local
- Criando um perfil personalizado para o github
---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [x] Fiz o fork do repositório.
- [x] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [x] Resolvi o exercício.
- [x] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [x] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [x] Pushei os commits na minha branch (`git push origin nome-da-branch`)










#### COMO CORRIGIR ERRO
 remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.

Quando eu estava terminando de enviar para o repositório no github, eu tive esse probleminha de senha, e sempre aparecia esse erro. E aí descobri que precisava de um token e consegui resolver assim:

- Lá em "Settings" no perfil do GitHub
- Em seguida <> Developer Settings
- Personal Acess Token
- New Personal Acess Token
- E aí vai aparecer o token (é bom salvar em algum lugar, porque talvez não consiga copiar novamente)

E aí pra terminar de enviar para o repositório local:

- git remote set-url origin https://[colei-aqui-o-token]@github.com/[url-do-meu-repositorio]
- git remote -v
- git push -u origin main

Daí ele pede a senha, então eu colei o token e deu certo o/


