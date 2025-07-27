\# Flask Alert Receiver (Kubernetes Deployment)



A lightweight Flask-based API that receives POST requests (alerts) from monitoring tools like \*\*Prometheus Alertmanager\*\* and runs in a Kubernetes cluster.



\## 🔧 Features

\- Handles incoming alerts via a `/alert` endpoint

\- Dockerized \& container-ready

\- Kubernetes deployment \& service YAMLs included

\- Easily integrates with Prometheus Alertmanager



\## 🐳 Docker Build



```bash

docker build -t yourdockerhub/alert-receiver:latest .

kubectl apply -f flask-alert-deployment.yaml

Invoke-RestMethod -Uri http://127.0.0.1:<PORT>/alert `

&nbsp; -Method POST `

&nbsp; -Headers @{ "Content-Type" = "application/json" } `

&nbsp; -Body '{ "status": "firing", "alerts": \["test alert"] }'



