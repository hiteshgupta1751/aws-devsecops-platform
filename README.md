# End-to-End DevSecOps Platform on AWS EKS

A production-style cloud-native DevSecOps pipeline demonstrating automated secure deployments using Kubernetes, GitHub Actions, Docker, and AWS.
This project simulates a real-world enterprise DevOps workflow where every code change automatically goes through testing, security scanning, containerization, and zero-downtime deployment to Kubernetes.
Designed to showcase practical Cloud Engineering, DevOps automation, and DevSecOps security integration.

## Project Objectives

- Automate application deployment using CI/CD pipelines.
- Integrate security scanning directly into delivery workflow (DevSecOps).
- Deploy scalable containerized workloads using Kubernetes.
- Implement rolling updates with zero downtime.
- Demonstrate real cloud-native infrastructure practices.

## Architecture Overview
```
Developer Push → GitHub Repository
                  │
                  ▼
            GitHub Actions CI/CD
      ┌─────────────────────────────┐
      │ Secret Scan (Gitleaks)      │
      │ Unit Tests (Pytest)         │
      │ Security Scan (Trivy)       │
      │ Docker Build                │
      │ Push Image to AWS ECR       │
      │ Update Kubernetes Deployment│
      └───────────────┬─────────────┘
                      ▼
                AWS EKS Cluster
                      ▼
              Rolling Update Deployment
                      ▼
              Kubernetes LoadBalancer
                      ▼
                 Public Endpoint
```

## Tech Stack
Cloud Infrastructure
- AWS EKS (Elastic Kubernetes Service)
- AWS ECR (Elastic Container Registry)
- AWS IAM

## DevOps & Automation

- GitHub Actions — CI/CD automation
- Docker — Containerization
- Kubernetes — Container orchestration
- kubectl — Cluster management

## DevSecOps Security

- Trivy — Vulnerability scanning
- Gitleaks — Secret detection
- Pytest — Automated testing

### Application Layer

- Python Flask REST API
- Containerized microservice architecture

## Project Structure
```
aws-devsecops-platform/
│
├── .github/workflows/
│   └── deploy.yml           # CI/CD pipeline
│
├── app/
│   ├── __init__.py          # Flask application
│   ├── __main__.py          # Package entrypoint
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
│
├── k8s/
│   ├── deployment.yaml      # Kubernetes Deployment
│   └── service.yaml         # Kubernetes Service
│
└── README.md
```

## CI/CD Pipeline Flow

Every push to main branch triggers:

### Continuous Integration (CI):-
- Checkout repository
- Run secret scanning (Gitleaks)
- Install dependencies
- Execute automated tests (pytest)
- Perform vulnerability scanning (Trivy)
- Build Docker image
- Push image to AWS ECR

### Continuous Deployment (CD):-
- Update Kubernetes image tag dynamically
- Apply deployment manifests
- Rolling update to new version
- Verify rollout status

## Kubernetes Deployment Strategy

This project uses:-
- Kubernetes Deployment resource
-  Rolling updates (zero downtime)
-  Multiple replicas for high availability
-  LoadBalancer service for external access

## DevSecOps Security Implementation

Security is integrated directly into pipeline:
- Secret scanning prevents credentials from entering repository
- Container image scanning identifies vulnerabilities early
- Automated testing validates application functionality
- AWS IAM roles enforce secure access control

## Setup & Deployment
1. Clone Repository:- 
```
git clone https://github.com/YOUR_USERNAME/aws-devsecops-platform.git
cd aws-devsecops-platform
```

2. Configure AWS CLI:- 
```
aws configure
```

3️. Create EKS Cluster (example):- 
```
eksctl create cluster \
  --name devsecops-cluster \
  --region ap-south-1 \
  --nodegroup-name workers \
  --node-type t3.medium \
  --nodes 2
```

4️. Configure kubectl:- 
```
aws eks update-kubeconfig --name devsecops-cluster --region ap-south-1
kubectl get nodes
```

5️. Add GitHub Secrets:-

- Repository Settings →
  - Secrets:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY

6️. Deploy:-

Push code to main branch:
```
git add .
git commit -m "Deploy update"
git push
```

## Pipeline will automatically:
- Build image
- Scan vulnerabilities
- Deploy to EKS

## Access Application

Get LoadBalancer URL:
```
kubectl get svc -n devsecops
```
Open the External IP in browser.

## Testing

Run locally:
```
pip install -r app/requirements.txt
python -m pytest
```

## Cost Optimization (IMPORTANT)

Delete resources after testing:
```
eksctl delete cluster --name devsecops-cluster --region ap-south-1
aws ecr delete-repository --repository-name devsecops-app --region ap-south-1 --force
```

## Key DevOps Concepts Demonstrated

- CI/CD automation
- Containerized deployments
- Kubernetes orchestration
- Rolling deployments
- DevSecOps security integration
- Cloud-native architecture

## Project Highlights

- Production-style CI/CD workflow
- Secure DevSecOps pipeline
- Automated Kubernetes deployment
- Zero downtime rolling updates
- Cloud-native infrastructure design
- Security scanning integrated into pipeline

## Author 

### Hitesh Gupta
Cloud & DevOps Engineer
