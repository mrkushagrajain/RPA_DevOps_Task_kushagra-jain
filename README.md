# RPA DevOps Automation – Automation Anywhere A360

## Introduction

This repository demonstrates a **mini end-to-end DevOps automation setup** for an  
**Automation Anywhere A360 RPA platform**, deployed on **Azure (simulated)**.

The project is designed to showcase how **enterprise RPA platforms** can be operated using
modern **DevOps principles**, even when a live Azure subscription or Automation Anywhere
tenant is not available.

---

## 🏗️ Architecture

The solution follows a **standard enterprise CI/CD architecture** for RPA platforms.

### High-Level Architecture

```text
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
   ├── Deploy Dev
   │   └── Automation Anywhere Control Room (Mock REST)
   │
   ├── Deploy Test
   │   └── Artifact Promotion
   │
   ├── Manual Approval Gate
   │
   └── Deploy Prod
       └── Final Production Deployment
Infrastructure Components (Simulated)
Resource Group
Logical container for all RPA-related resources

Storage Account
Stores bot packages and pipeline artifacts

VM / App Service (Mock)
Represents Automation Anywhere Control Room and Bot Runners

Key Vault (Mock)
Simulates secure storage for secrets and credentials

Infrastructure is defined using Terraform, but not deployed to a real Azure environment.

🔄 CI/CD Flow
The CI/CD pipeline is implemented using Azure DevOps YAML pipelines.

CI/CD Stages
Build & Validate

Bot structure and manifest validation

Packaging of RPA bot artifacts

Artifact versioning

Deploy to Dev

Automatic deployment using mock Control Room REST APIs

Uses Dev-specific configuration

Deploy to Test

Promotes the same artifact from Dev to Test

No rebuilds (build once, deploy many)

Manual Approval Gate

Business or release approval before production

Deploy to Prod

Final production deployment using the approved artifact

Rollback (Manual)

Re-deploys a previously built artifact if needed

🚀 Deployment Strategy
Strategy Used: Artifact-Based Promotion
The deployment model follows a build-once, deploy-many approach.

Deployment Flow
Build the bot package once

Promote the same artifact through:

Dev

Test

Prod

No rebuilding between environments

Benefits
Prevents configuration drift

Ensures production uses tested artifacts

Aligns with enterprise DevOps best practices

📊 Monitoring & Logging
Basic observability is implemented to track pipeline and deployment activity.

What Is Monitored
Pipeline execution logs in Azure DevOps

Bot deployment status logs stored in logs/

JUnit XML reports for deployment steps

Log Artifacts
logs-dev

logs-test

logs-prod

Alert Simulation
Alerts are simulated using a notification script

Can be extended to Email, Microsoft Teams, or Slack

⚖️ Assumptions & Trade-offs
Assumptions
No live Azure subscription is available

No live Automation Anywhere A360 tenant is available

RPA bots are packaged as deployable artifacts

Control Room interactions are REST-based

Trade-offs
Mock REST APIs
→ No real bot execution, but realistic API flow

Simulated Key Vault
→ Secrets are not real, but handled securely in design

Simple bot implementation
→ Focus is on DevOps automation, not bot complexity

These trade-offs were intentional to keep the solution portable, testable, and focused on DevOps practices.

Conclusion
This project demonstrates:

Infrastructure as Code using Terraform

CI/CD automation for RPA bots

Environment-aware deployments

Monitoring, logging, and rollback strategies

The overall design closely mirrors how Automation Anywhere A360 would be operated
in a real enterprise Azure environment, while remaining fully executable in a
simulated setup.











New version of GPT available - Continue chatting to use the old version, or start a new chat for the latest version.
