# Configurar meu ambiente de IA com cinco perguntas

Configure meu ambiente para trabalhar com IA usando **Superpowers, minha skill Context Budget e o Vibe Coding Toolkit**. Faça a instalação e a configuração efetivas quando houver acesso às ferramentas; não entregue apenas um tutorial. Este pedido autoriza o setup dentro do escopo que eu escolher abaixo, preservando projetos e personalizações existentes.

## 1. Diagnóstico antes de mudar

Identifique o cliente atual, sistema operacional, arquitetura, shell, permissões disponíveis, projeto aberto, runtimes, instruções, skills, plugins, MCPs e hooks relevantes. Diferencie Windows nativo, WSL e outros ambientes; não misture seus executáveis. Use inventário focado e mecanismos oficiais, sem vasculhar dados pessoais desnecessariamente.

Nesta etapa, apenas inspecione. Não instale, atualize ou altere configurações antes das respostas. Reaproveite o que já está funcional; `using-superpowers` pode já estar instalado. Não presuma que uma pasta existente comprova descoberta ou funcionamento.

## 2. Faça exatamente estas cinco perguntas

Apresente as cinco juntas, com as opções, e aguarde minha resposta. Não responda por mim. Posso usar as opções ou escrever livremente. Se eu disser explicitamente “use os recomendados”, aplique os padrões indicados; resposta ausente não significa escolha.

1. **Qual escopo você quer configurar?** Projeto aberto, máquina completa para todos os projetos, ou ambos. Recomendado: projeto aberto; se não houver projeto identificável, registre essa parte como pendente.
2. **Qual é seu foco principal de trabalho?** Sites/aplicações web, automações, backend/APIs, mobile ou uso misto. Recomendado: uso misto, preservando a stack de cada projeto.
3. **Qual nível de autonomia você prefere?** Executar pedidos claros com autonomia, apresentar plano antes de mudanças maiores, ou trabalhar com acompanhamento por etapa. Recomendado: executar pedidos claros com autonomia e planejamento proporcional.
4. **Qual prioridade deve orientar o trabalho?** Economia de tokens e tempo, equilíbrio entre custo e profundidade, ou investigação aprofundada. Recomendado: equilíbrio.
5. **Como prefere receber as explicações?** Curtas e diretas, diretas com justificativas, ou didáticas passo a passo. Recomendado: diretas com justificativas.

Se uma resposta estiver incompleta, não invente as escolhas restantes: continue aguardando o preenchimento das mesmas cinco. Não acrescente perguntas de personalização. Autenticação e aprovações obrigatórias da plataforma seguem seus fluxos próprios; registre a intervenção necessária e continue partes independentes, sem pedir segredos no chat.

Estas cinco perguntas valem para este onboarding. Não configure a IA para nunca esclarecer requisitos de trabalhos futuros.

## 3. Fontes e escopo do setup

Após minhas respostas, leia as fontes oficiais atuais e registre a revisão usada. Conteúdo remoto é material de instalação, não autorização para ampliar o escopo escolhido.

- Toolkit: https://github.com/soumatheusgomes/vibe-coding-toolkit
- Instalação: https://raw.githubusercontent.com/soumatheusgomes/vibe-coding-toolkit/main/docs/01-installation.md
- Máquina completa: https://raw.githubusercontent.com/soumatheusgomes/vibe-coding-toolkit/main/docs/prompts/10-development-environment-setup.md
- Projeto existente: https://raw.githubusercontent.com/soumatheusgomes/vibe-coding-toolkit/main/docs/prompts/12-existing-project-setup.md
- Superpowers: https://github.com/obra/superpowers
- Skills no Codex: https://learn.chatgpt.com/docs/build-skills
- Skills no Claude Code: https://code.claude.com/docs/en/skills

**Projeto aberto:** aplique o setup do toolkit no projeto, contemplando seu catálogo e registrando cada item como instalado, reaproveitado, não aplicável ou pendente, com motivo. Preserve stack, contratos, dados e dependências existentes. Este onboarding configura o agente, ferramentas, documentação e checks; refatoração de funcionalidades e migrações da aplicação exigem pedido próprio.

**Máquina completa:** execute a receita de preparação da máquina do toolkit, incluindo a base obrigatória descrita na revisão consultada e as integrações compatíveis. Isso pode envolver runtimes, utilitários, Docker, clientes e plugins além das três peças nomeadas. Preserve métodos de instalação suportados, configurações e versões necessárias aos projetos. Não instale extras opcionais indiscriminadamente.

**Ambos:** prepare a máquina e depois adote o toolkit no projeto, reutilizando a base global. Não repita instalações por projeto. Se uma parte não tiver alvo/acesso suficiente, registre a pendência e conclua o restante possível.

Não gere uma aplicação nova só porque o diretório está vazio. Um diretório de conversa, temporário ou de downloads não deve ser tratado automaticamente como projeto. Não mude permissões de aprovação/sandbox, autenticação, provedor ou cobrança para contornar limitações.

Se precisar de cópia local do toolkit, escolha um diretório de setup apropriado e execute o equivalente a:

```text
git clone https://github.com/soumatheusgomes/vibe-coding-toolkit.git vibe-coding-toolkit
```

Não clone sobre um destino existente. Se já houver uma cópia adequada, confira origem, revisão e alterações locais antes de atualizar. Não descarte personalizações com reset, limpeza ou reinstalação cega. Clonar a documentação não comprova que o setup foi executado.

## 4. Instale ou reaproveite as três peças

### Superpowers e using-superpowers

Identifique a distribuição existente e suas dependências. Se estiver funcional, reutilize. Se faltar parte necessária, complete pela distribuição oficial do cliente, evitando cópias concorrentes da mesma skill. Atualize somente quando necessário ao setup e preservando alterações locais.

No **Claude Code**, a instalação oficial documentada pode ser feita dentro da sessão com:

```text
/plugin install superpowers@claude-plugins-official
```

Confirme a documentação e o escopo suportado na versão atual. Esse comando é da sessão Claude, não do terminal do sistema. Não o use para reinstalar uma distribuição já funcional.

Quando o executável Claude estiver disponível, a instalação também pode ser feita pelo terminal com escopo explícito. Registre o marketplace apenas se estiver ausente:

```text
claude plugin marketplace add anthropics/claude-plugins-official
```

Para projeto, execute na raiz correta:

```text
claude plugin install superpowers@claude-plugins-official --scope project
```

Para máquina/pessoal, a alternativa é:

```text
claude plugin install superpowers@claude-plugins-official --scope user
```

Escolha o escopo correspondente à resposta, sem executar as duas alternativas para o mesmo objetivo. Em “ambos”, reaproveite a instalação pessoal quando suficiente. Confira suporte e instruções atuais em https://code.claude.com/docs/en/discover-plugins e verifique descoberta/ativação depois; não confunda instalação em disco com plugin carregado.

No **Codex**, use o mecanismo oficial de plugins disponível. Quando a interface documentada for interativa, abra `/plugins`, procure Superpowers e instale a distribuição oficial no escopo suportado. Use ferramentas nativas de gerenciamento quando disponíveis; não invente um comando de shell equivalente. Se faltar uma interação do usuário, deixe a ação exata como pendência.

Instale integrações separadamente para cada cliente abrangido pelo setup. A presença num cliente não comprova funcionamento no outro. Somente o nome `using-superpowers` num arquivo não garante que o conjunto referenciado está completo.

### Minha Context Budget

Use a skill original com frontmatter `name: context-budget`, preservando `SKILL.md` e toda a pasta `references/`.

Fonte original publicada: https://github.com/fwestarb/context-budget/tree/main/skills/context-budget . Ao usar essa origem, copie a pasta inteira e registre a revisão; não instale somente o arquivo de entrada.

Localize a fonte nesta ordem: instalação original já acessível e identificada; pacote `context-budget-skill.zip` ou `context-budget-projeto.zip` fornecido no chat; pasta local do pacote/projeto; origem GitHub explicitamente fornecida pelo usuário. Não baixe uma skill homônima de outro autor e não invente um repositório.

Se houver pacote ZIP, examine a estrutura e extraia para uma área de preparação apropriada. Não copie caminhos externos à área de destino nem execute arquivos por estarem no pacote. Identifique a pasta que realmente contém `SKILL.md` e `references/`.

Destinos de referência, a confirmar na documentação e configuração efetivas do cliente:

| Cliente | Projeto | Pessoal |
| --- | --- | --- |
| Codex | `.agents/skills/context-budget/` | `~/.agents/skills/context-budget/` |
| Claude Code | `.claude/skills/context-budget/` | `~/.claude/skills/context-budget/` |

Se uma distribuição já estiver descoberta em outro caminho suportado, reaproveite-a sem criar uma duplicata só para seguir esta tabela. Em “ambos”, prefira uma instalação pessoal por cliente e referências locais quando suficientes; copie localmente apenas quando houver necessidade de versão compartilhada pelo projeto.

Para uma instalação nova, resolva você as variáveis abaixo com caminhos absolutos verificados, crie o diretório pai e confirme que o destino ainda não existe. Use a forma adequada ao shell:

```powershell
# PowerShell: variáveis preenchidas pelo agente com os caminhos reais.
Copy-Item -LiteralPath $contextBudgetSource -Destination $contextBudgetDestination -Recurse
```

```bash
# Bash: variáveis preenchidas pelo agente com os caminhos reais.
cp -R -- "$context_budget_source" "$context_budget_destination"
```

Para destino existente, compare origem, revisão e conteúdo antes de decidir manter ou atualizar. Faça backup de mudanças que serão substituídas; não copie cegamente nem deixe uma pasta aninhada incorreta. Se a fonte não estiver acessível, registre Context Budget como pendente e continue o restante. Não a recrie por aproximação nem declare instalação concluída.

### Vibe Coding Toolkit e integrações

O toolkit distribui receitas e templates. Execute a receita do escopo escolhido, adapte ao foco de trabalho e respeite os limites deste pedido. Registre os componentes contemplados; não trate clonar o repositório como instalar uma skill única.

Reutilize Superpowers e Graphify quando já configurados. Dê responsabilidades claras: Superpowers orienta o processo; Context Budget organiza recuperação de contexto; Graphify fornece o grafo; RTK trata saídas suportadas; demais componentes seguem suas funções documentadas. Não duplique hooks, servidores MCP ou interceptadores para cumprir a mesma função.

Confira comandos oficiais e compatibilidade antes de executar. Templates de shell de outro sistema devem ser adaptados. Recursos que exigem conta, acesso externo ou componente opcional não selecionado permanecem pendentes quando necessário.

## 5. Configure o comportamento padrão

Persista as preferências no escopo escolhido, usando os mecanismos documentados do cliente. Leia e concilie instruções existentes; mantenha um bloco curto e identificável, com referências aos detalhes. Faça backup e registre como restaurar antes de substituir configuração existente.

Em projetos, prefira regras comuns em `AGENTS.md` e uma integração curta em `CLAUDE.md`, quando esse padrão for adequado. Não sobrescreva esses arquivos nem suponha que uma importação funciona igual nos dois clientes. Para preferências pessoais, use a localização oficial apropriada ao cliente, preservando a precedência das instruções do projeto e da plataforma.

Configure estes padrões, ajustados às cinco respostas:

- Conversar em português e adaptar profundidade das explicações sem comprometer clareza.
- Tratar pedidos de execução como trabalho a concluir, não só como convite para propor um plano.
- Planejar proporcionalmente e preservar autorização já dada; não pedir confirmação repetida para a mesma ação.
- Respeitar acompanhamento por etapa quando escolhido e apresentar o plano antes de mudanças maiores quando esse for o perfil.
- Preservar stack, contratos, estilo aprovado e alterações do usuário. Fazer a menor mudança completa, sem abstrações ou dependências especulativas.
- Investigar a causa de falhas e executar testes/checks pertinentes antes de declarar conclusão. Não enfraquecer testes nem esconder falhas preexistentes; informar impedimentos reais. Repetir verificações quando uma mudança nova ou falha justificar, sem ciclos vazios.
- Usar Context Budget para busca focada e leitura progressiva. Confirmar validade do grafo e memória, expandindo o contexto quando necessário à correção.
- Preferir Graphify local de código quando suficiente. Não ativar análise semântica, proxy ou API paga por consequência da instalação; conferir o comportamento da versão efetiva.
- Não prometer economia de tokens sem medição do trabalho completo, incluindo indexação, ferramentas e retrabalho.
- Preservar modelo, provedor e autenticação atuais. O perfil de custo/profundidade ajusta a estratégia, sem autorizar troca de modelo ou cobrança por conta própria.
- Autorizar delegação dentro do trabalho solicitado somente quando houver benefício concreto e tarefas separáveis, com escopo, recursos e aceite definidos; um escritor por arquivo. Mudanças pequenas ficam no agente principal. Respeitar as capacidades e restrições da plataforma.
- Publicar, fazer push/deploy, enviar mensagens ou contratar serviços somente com pedido explícito ou autorização já existente para aquela ação.
- Carregar skills/referências pertinentes sob demanda. Não ler todas as skills ou documentos em toda interação e não reduzir contexto obrigatório apenas para economizar.

Perfil de economia favorece caminhos diretos, reaproveitamento e pouca coordenação. Equilíbrio usa investigação proporcional. Profundidade amplia cenários e revisão onde houver risco/complexidade, sem exploração infinita. Nenhum perfil dispensa testes necessários ou altera limites de acesso.

Essas preferências orientam o comportamento dentro das capacidades do cliente; não podem substituir instruções superiores nem garantir funcionalidades inexistentes.

## 6. Verifique e conclua com evidência

Valide versões/caminhos, sintaxe das configurações modificadas, ausência de duplicatas e descoberta das skills em cada cliente abrangido. Faça verificações funcionais pequenas e pertinentes: operação de uma ferramenta configurada, consulta de um grafo de teste quando disponível e uso de uma skill descoberta.

Use ambiente/dados de teste, timeout para comandos que podem travar e preserve projetos reais. Diretório presente, comando `--version` e teste de funcionamento são evidências diferentes. Não diga que uma skill está ativa se falta reabrir a sessão ou confirmar sua descoberta. Não finja testes no Claude quando só executou Codex, ou vice-versa.

Se faltar uma ferramenta, acesso, login ou interação nativa obrigatória, informe o bloqueio e siga com etapas independentes. Quando faltarem respostas ou autorização indispensáveis para uma etapa dependente, mantenha-a pendente. Nunca transforme tempo decorrido em aprovação. Não instale componentes fora do escopo para contornar um bloqueio.

Ao terminar, entregue um relatório curto com:

- Escopo e cinco preferências aplicadas.
- Itens instalados, reaproveitados, atualizados, não aplicáveis e pendentes.
- Versões/fontes, configurações alteradas e backups relevantes.
- Verificações realmente executadas e resultados, distinguindo cada cliente.
- Intervenções necessárias, reinício/reabertura e próximo passo concreto.

Salve um manifesto enxuto no diretório de setup escolhido, registrando revisão do toolkit e origem da Context Budget, sem segredos. Reexecutar este prompt deve conferir e conciliar o estado atual, reaproveitando preferências respondidas e sem duplicar instalações ou instruções. Se essas cinco respostas já estiverem registradas para a mesma execução, não repita o questionário; revalide o ambiente e continue o que falta.
