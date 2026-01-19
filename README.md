This project demonstrates a mini end-to-end DevOps automation setup for an
Automation Anywhere A360 RPA platform, deployed on Azure (simulated).

🎯 Objectives

Enable CI/CD for RPA bots

Apply enterprise DevOps best practices

Operate without a live Azure or Automation Anywhere tenant

The solution mirrors real-world enterprise RPA operations while remaining fully portable.

✨ Features

Key capabilities implemented

🧱 Infrastructure as Code (IaC) using Terraform

🔄 CI/CD automation for RPA bot lifecycle

🌍 Environment separation (Dev / Test / Prod)

🔐 Secure configuration handling (simulated)

📦 Artifact-based promotion strategy

📊 Deployment logs & test reports

🔁 Manual rollback support

🏗️ Architecture

High-level system design

🔹 Architecture Flow
Developer
   │
   │  (Git Commit)
   ▼
Azure Repos (Git)
   │
   ▼
Azure DevOps Pipeline (YAML)
   │
   ├── Build & Validate
   │   └── Package RPA Bots
   │
   ├── Deploy Dev (Mock REST)
   │   └── A360 Control Room (Simulated)
   │
   ├── Deploy Test (Mock REST)
   │   └── Artifact Promotion
   │
   ├── Manual Approval Gate
   │
   └── Deploy Prod (Mock REST)
       └── Final Promotion

🔹 Infrastructure Components (Terraform – Simulated)
Component	Purpose
Resource Group	Logical container for RPA platform
Storage Account	Stores bot packages & artifacts
VM / App Service	Control Room & Bot Runners (mock)
Key Vault	Secrets storage (simulated)

Infrastructure is defined using Terraform but not applied to a real Azure subscription (Option B).

🧰 Technologies Used

Tools & platforms

Category	Technology
CI/CD	Azure DevOps
IaC	Terraform
RPA	Automation Anywhere A360
Scripting	Python
Configuration	YAML
Version Control	Git & GitHub
🔄 CI/CD Pipeline

How automation works

🔹 Pipeline Stages
Stage	Description
Build & Validate	Validate bot structure & package artifact
Deploy Dev	Automated deployment to Dev
Deploy Test	Artifact promotion to Test
Manual Gate	Approval before Prod
Deploy Prod	Production deployment
Rollback	Manual rollback to previous version

✔ Build once, deploy everywhere

🤖 Automation Anywhere Integration

Control Room interaction

🔹 Integration Method

✔ REST API interaction (Mocked)

🔹 Simulated Endpoints
POST /oauth2/token
POST /repository/packages
POST /deployments


Implemented via aa_deploy.py, designed to be easily extended to real APIs.

📊 Monitoring & Logging

Observability & feedback

📝 Pipeline execution logs in Azure DevOps

📂 Deployment logs per environment

🧪 JUnit XML test reports

📢 Alert simulation via notify.py

Published Artifacts

logs-dev

logs-test

logs-prod

🚀 Deployment Strategy

Release approach

🔹 Artifact-Based Promotion

Build once

Promote the same artifact to:

Dev

Test

Prod

No rebuilds between environments

✅ Prevents drift
✅ Ensures reliability

🔁 Rollback Strategy

Failure recovery

Manual rollback trigger

Re-deploy previous artifact

Logs & reports preserved

⚖️ Assumptions & Trade-offs
Assumptions

No live Azure or Automation Anywhere tenant

RPA bots are package-based

Control Room APIs are REST-driven

Trade-offs
Decision	Trade-off
Mock APIs	No real bot execution
Simulated secrets	No real Key Vault
Simple bot logic	Focus on DevOps, not bot complexity
