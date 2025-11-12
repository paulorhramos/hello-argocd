# Hello ArgoCD

Aplicação Flask de exemplo para demonstração do fluxo GitOps com GitHub Actions e ArgoCD.

## 🎯 Objetivo

Esta aplicação demonstra o fluxo completo de CI/CD GitOps:

1. **Código** → Push para GitHub
2. **CI** → GitHub Actions builda e publica imagem Docker
3. **GitOps** → GitHub Actions atualiza manifesto K8s em repositório separado
4. **CD** → ArgoCD detecta mudança e faz deploy automático no cluster

## 🏗️ Arquitetura

```
┌──────────────┐    push     ┌──────────────────┐
│   Código     │─────────────>│ GitHub Actions   │
│ (hello-argocd)│              │  - Build image   │
└──────────────┘              │  - Push registry │
                              │  - Update manifest│
                              └─────────┬─────────┘
                                        │
                                        v
                              ┌──────────────────┐
                              │  k8s-manifests   │
                              │   repository     │
                              └─────────┬─────────┘
                                        │
                                        v
                              ┌──────────────────┐
                              │     ArgoCD       │
                              │   - Sync auto    │
                              │   - Deploy K8s   │
                              └─────────┬─────────┘
                                        │
                                        v
                              ┌──────────────────┐
                              │  Kubernetes      │
                              │    Cluster       │
                              └──────────────────┘
```

## 📦 Estrutura

```
hello-argocd/
├── app.py                    # Aplicação Flask
├── requirements.txt          # Dependências Python
├── Dockerfile               # Build da imagem
├── .github/
│   └── workflows/
│       └── build-and-push.yaml  # CI/CD pipeline
└── README.md
```

## 🚀 Executar localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py

# Testar
curl http://localhost:5000
```

## 🐳 Build Docker

```bash
docker build -t paulorhramos/hello-argocd:latest .
docker run -p 5000:5000 paulorhramos/hello-argocd:latest
```

## 🔄 Fluxo GitOps

1. **Modificar código**: Edite `app.py`
2. **Commit e push**: `git push origin main`
3. **GitHub Actions**: Automaticamente builda e atualiza manifesto
4. **ArgoCD**: Detecta mudança e faz sync automático
5. **Verificar**: `curl http://hello-argocd.10.20.20.50.nip.io`

## 📝 Variáveis de Ambiente

- `APP_VERSION`: Versão da aplicação (default: v1.0.0)
- `ENVIRONMENT`: Ambiente de execução (default: production)

## 🔐 Secrets Necessários

Configure no GitHub (Settings → Secrets):

- `DOCKER_USERNAME`: Usuário Docker Hub
- `DOCKER_PASSWORD`: Token/senha Docker Hub
- `GH_PAT`: Personal Access Token com permissão `repo`

## 📊 Endpoints

- `GET /` - Hello message com versão e hostname
- `GET /health` - Health check

## 🛠️ Troubleshooting

```bash
# Ver logs da aplicação
kubectl logs -n default -l app=hello-argocd

# Verificar pods
kubectl get pods -n default -l app=hello-argocd

# Status ArgoCD
kubectl get application -n argocd hello-argocd
```
