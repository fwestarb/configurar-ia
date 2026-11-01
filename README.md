# Configurar IA

Prompt único de onboarding para Codex e Claude Code, com exatamente cinco perguntas iniciais, instalação/reaproveitamento de Superpowers, Context Budget e Vibe Coding Toolkit e preferências persistentes.

## Usar

Abra [o prompt](PROMPT-CONFIGURAR-IA.md), copie o conteúdo e cole na conversa do agente. A execução começa com diagnóstico e as cinco perguntas, aguardando respostas antes de alterar o ambiente.

Context Budget: [fonte original](https://github.com/fwestarb/context-budget/tree/main/skills/context-budget). O prompt também aceita o pacote local original quando necessário.

Escopos: projeto, máquina completa ou ambos. O fluxo de máquina pode instalar runtimes, Docker e outras ferramentas exigidas pela receita do toolkit. O prompt não executa nada por ser aberto no GitHub.

## Verificação e limites

Foram conferidas as cinco perguntas e testado o trecho de cópia PowerShell em diretório temporário, com seis arquivos, caminhos com espaços e fonte preservada. Os comandos de plugins foram conferidos com documentação oficial, mas não foi executado o setup completo da máquina nem uma sessão nativa de Claude Code. Não há garantia de instalação sem intervenções de autenticação/permissões.

Execute `python scripts/check.py` para verificar a integridade deste pacote. Esse check não instala o toolkit. Os cenários do fluxo foram revisados manualmente; isso não equivale a uma avaliação independente por outro modelo.

## Fontes

- [Vibe Coding Toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit)
- [Superpowers](https://github.com/obra/superpowers)
- [Skills no Claude Code](https://code.claude.com/docs/en/skills)
- [Skills no Codex](https://learn.chatgpt.com/docs/build-skills)
