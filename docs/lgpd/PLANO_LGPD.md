# Plano de Conformidade LGPD com Automação (Tarefa 3)

## Controles
- **Consentimento rastreável**: logs com {user, ts, ip, versão do termo, origem}. Imutável (append-only).
- **Minimização de dados**: tabela de escopos (Login: e-mail; Cadastro: nome, e-mail).
- **Criptografia**: HTTPS + headers (CSP/HSTS); at-rest com chaves geridas (KMS).
- **RBAC + Auditoria**: matriz de permissões e logs de acesso/exportação.
- **Direitos do titular**: processos para acesso, correção, exclusão, portabilidade.

## Integração CI/CD
- Semgrep `lgpd.yml` e testes `tests/lgpd` rodando no `lgpd-check.yml`.
- Alertas quando coleta excede escopo ou faltam controles.

## Evidências
- Prints do job `LGPD Compliance Checks` e exemplos de logs de consentimento simulados.
