# GitHub Secrets - hello-argocd

## 📋 Secrets Necessários

Configure estes secrets em: https://github.com/paulorhramos/hello-argocd/settings/secrets/actions

### 1. DOCKER_USERNAME
- **Valor**: Seu usuário do Docker Hub
- **Exemplo**: `paulorhramos`
- **Uso**: Login no Docker Hub para push de imagens

### 2. DOCKER_PASSWORD
- **Valor**: Token de acesso do Docker Hub
- **Como gerar**:
  1. Acesse: https://hub.docker.com/settings/security
  2. Clique em "New Access Token"
  3. Nome: `github-actions`
  4. Permissões: Read, Write, Delete
  5. Copie o token gerado

### 3. GH_PAT (Personal Access Token)
- **Valor**: Token GitHub com permissão `repo`
- **Como gerar**:
  1. Acesse: https://github.com/settings/tokens
  2. Generate new token (classic)
  3. Nome: `argocd-gitops`
  4. Scopes: Marque `repo` (Full control of private repositories)
  5. Copie o token gerado

## ✅ Verificar Configuração

Após configurar os secrets:

```bash
cd /root/stacks/hello-argocd
git commit --allow-empty -m "trigger: test GitHub Actions workflow"
git push
```

Acompanhe o build em: https://github.com/paulorhramos/hello-argocd/actions

## 🔍 Verificar Deployment

Após o build completar:

```bash
# Status ArgoCD
kubectl get application -n argocd hello-argocd

# Pods
kubectl get pods -n default -l app=hello-argocd

# Service
kubectl get svc hello-argocd

# Ingress
kubectl get ingress hello-argocd

# Testar aplicação
curl http://hello-argocd.10.20.20.50.nip.io
```

## 🎯 Secrets Configurados?

Depois de adicionar os 3 secrets acima, execute:

```bash
cd /root/stacks/hello-argocd
git commit --allow-empty -m "trigger: initial build"
git push
```

O GitHub Actions irá:
1. ✅ Build da imagem Docker
2. ✅ Push para Docker Hub (paulorhramos/hello-argocd:latest)
3. ✅ Update do deployment.yaml com o hash do commit
4. ✅ ArgoCD detecta mudança e faz sync automático
5. ✅ Aplicação disponível em http://hello-argocd.10.20.20.50.nip.io
