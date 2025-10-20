# Sprint 3 — Cybersecurity (Entrega Final)

## Equipe
- Júlio César Zampieri — RM98772
- Gustavo Melo — RM98809
- Carlos Augusto Campos Ganzerli — RM99840
- Lucas Carlos Bandeira Teixeira — RM98640
- João Gabriel Dias — RM99092

## Conteúdo desta entrega
- **Tarefa 1 — SSDLC & Codificação Segura**
  - CI unificado `ci-ssdlc.yml` (build/tests + SAST + SCA + DAST)
  - Regras Semgrep (`semgrep-rules/secure.yml`)
  - Testes automatizados (`tests/security`)
  - Relatório técnico (`docs/ssdlc/RELATORIO_SSDLC.md`) — inclui seção do SonarQube
- **Tarefa 2 — Gerenciamento Contínuo de Vulnerabilidades**
  - `vuln-weekly.yml` (scan semanal)
  - Dependabot (`.github/dependabot.yml`)
  - Template de Issue (`.github/ISSUE_TEMPLATE/vulnerability.yml`)
  - Processo documentado (`docs/vuln/PROCESSO_GERENCIAMENTO.md`)
- **Tarefa 3 — LGPD & Conformidade Automatizada**
  - `lgpd-check.yml` (checks em CI)
  - Regras LGPD (`semgrep-rules/lgpd.yml`)
  - Testes LGPD (`tests/lgpd`)
  - Plano de conformidade (`docs/lgpd/PLANO_LGPD.md`)
- **Qualidade de Código — SonarQube/SonarCloud**
  - Workflow `code-quality-sonar.yml`
  - Config `sonar-project.properties`

## Como usar
1. Faça upload de tudo num repositório GitHub (ex.: `sprint4_cybersecurity`).
2. Configure os segredos (Settings → Secrets → Actions):
   - `SONAR_TOKEN`, `SONAR_HOST_URL`, `SONAR_PROJECT_KEY`, `SONAR_ORG` (se usar SonarCloud).
3. Vá em **Actions** e verifique os jobs:
   - CI - SSDLC, LGPD Compliance Checks, Vulnerability Management - Weekly (manual/cron), Code Quality - Sonar.
4. Complete os relatórios em `docs/` com **prints** da aba Actions e do Sonar.

## Observações
Os testes e regras são exemplos mínimos para validar o pipeline e as políticas (não exigem app real). Se quiser apontar DAST para uma URL real de teste, atualize `target` no `dast_zap`.
