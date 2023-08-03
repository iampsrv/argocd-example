Commands:

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.1.3/manifests/install.yaml

kubectl get pod -n argocd
kubectl get svc -n argocd

kubectl port-forward svc/argocd-server -n argocd 8080:443

kubectl get secret argocd-initial-admin-secret -n argocd -o yaml

echo hash | base64 --decode