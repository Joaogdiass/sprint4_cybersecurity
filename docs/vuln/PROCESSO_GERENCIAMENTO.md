# Processo de Gerenciamento de Vulnerabilidades (Tarefa 2)

## Objetivo
Fluxo contínuo de identificação, priorização, mitigação e monitoramento.

## Identificação
- SAST (Semgrep), DAST (ZAP), SCA (Dependency-Check) no CI.
- GitHub Security Alerts + Dependabot PRs.

## Priorização
- CVSS + contexto do sistema.
- SLAs: Critical 48h · High 5d · Medium 15d · Low 30d.

## Mitigação
- Atualizações automáticas (Dependabot).
- Correções guiadas por alertas do Semgrep/SCA.
- Hotfix para achados DAST.

## Monitoramento
- Workflow semanal `vuln-weekly.yml`.
- Dashboards: GitHub Security / Actions.
- Métricas: MTTR, #abertas/fechadas por severidade.

## Evidências
- Prints das execuções e issues abertas via template `vulnerability.yml`.
