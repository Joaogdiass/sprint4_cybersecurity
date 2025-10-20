# Relatório Técnico — SSDLC Automatizado (Tarefa 1)

## Equipe
- Júlio César Zampieri (RM98772)
- Gustavo Melo (RM98809)
- Carlos A. C. Ganzerli (RM99840)
- Lucas C. B. Teixeira (RM98640)
- João Gabriel Dias (RM99092)

---

## Objetivo
Aplicar práticas de SSDLC no pipeline CI/CD e validar automaticamente funcionalidades críticas (Login e Cadastro) com base em análises de SAST, DAST e SCA.

---

## Práticas Implementadas
- **Validação & Sanitização de Entradas** — Implementada via testes unitários (`tests/security/test_input.py`).
- **Autenticação Segura** — Uso de JWT com expiração (`exp`), emissor (`iss`) e audiência (`aud`) controladas (`tests/security/test_auth.py`).
- **Tratamento Seguro de Erros** — Diretriz para não exibir stacktraces e informações sensíveis em ambiente produtivo.
- **Análise Estática (SAST)** — Semgrep (`semgrep-rules/secure.yml`) com regras personalizadas (ex.: SQL concat, `DEBUG=True`).
- **Análise de Dependências (SCA)** — OWASP Dependency-Check, falha se CVSS ≥ 7.
- **Análise Dinâmica (DAST)** — OWASP ZAP Baseline automatizado.

---

## Integração no CI/CD
Pipeline principal (`.github/workflows/ci-ssdlc.yml`):
1. **Build & Testes Automatizados** — Execução de testes (unidade + segurança).
2. **SAST (Semgrep)** — Verifica vulnerabilidades no código.
3. **SCA (Dependency-Check)** — Analisa dependências vulneráveis.
4. **DAST (ZAP)** — Testa endpoints em execução.

Falhas de segurança interrompem o pipeline, impedindo merge/deploy.

---

## 🔍 Integração com SonarQube / SonarCloud — Validação de Código

O **SonarQube/SonarCloud** foi integrado como camada de *code quality* e segurança.

### Objetivo
Complementar o SAST com insights de qualidade: **code smells**, **bugs**, **vulnerabilities**, **security hotspots**, **coverage** e **duplications**.

### Métricas Avaliadas
- **Code Smells**, **Bugs (Reliability)**, **Vulnerabilities (Security)**, **Security Hotspots**
- **Coverage (%)** a partir do `coverage.xml`
- **Duplications (%)**

### Integração no CI/CD
Workflow `.github/workflows/code-quality-sonar.yml`:
1. Executa testes e gera `coverage.xml`.
2. Envia resultados usando `SONAR_TOKEN` e `SONAR_HOST_URL`.
3. Aplica **Quality Gate** para bloquear PRs se métricas < padrão.

### Evidências
- Dashboard com **Quality Gate**.
- Painel de métricas (Smells, Bugs, Vulnerabilities, Coverage, Duplications).
- Comentários no PR (decoração, se SonarCloud).

### Conclusão
O Sonar reforça o SSDLC com validação contínua de **qualidade e segurança** antes do merge.

---

## Conclusão Final
O pipeline implementa DevSecOps de ponta a ponta, automatizando prevenção, detecção e mitigação a cada commit.
