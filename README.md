# Comprehensive Knowledge Collection

A portfolio-style knowledge base for computer science and software engineering topics, primarily as **Jupyter notebooks** (explanations + visuals + runnable code), with small **code projects** where needed (APIs, infrastructure, demos).

## Register Notebook
- Open `CKC_REGISTER.ipynb` and run the generator cell to update the repository index automatically.
- The generator updates the **Index** section below (and the index block inside `CKC_REGISTER.ipynb`).

## Contents
- Data Science: `data_science/`
  - Statistics, ML, algorithms, deep learning — with “from-scratch” NumPy + practical usage.
- DevOps: `devops/`
  - Architectures, cloud, containers/K8s, CI/CD, observability, IaC (Terraform).
- Backend: `backend/`
  - FastAPI patterns + broader API/system design topics.
- Cybersecurity: `cybersecurity/`
  - Fundamentals, web/network security, secure coding, best practices.
- Frontend: `frontend/`
  - Framework comparisons and usage (React/Next.js/Vue/Svelte), TS, testing, perf, accessibility.

## How to Use
- Start with `CKC_REGISTER.ipynb` to browse all topics.
- Prefer notebooks for learning; keep any optional runnable code inside the relevant topic folder.

## Index (auto-generated)

<!-- CKC_INDEX_START -->

### Data Science
- **Deeplearning**
  - **Tabular Data**
    - **Artificial Neural Networks**
      - [Artificial Neural Networks (MLPs) for Tabular Data](data_science/deeplearning/tabular_data/artificial_neural_networks/00_overview.ipynb)
  - **Timeseries**
    - **Lstm And Gru**
      - [LSTM and GRU for Time Series Forecasting (from scratch + PyTorch)](data_science/deeplearning/timeseries/lstm_and_gru/00_overview.ipynb)
  - **Visual**
    - **Cnn**
      - [Convolutional Neural Networks (CNNs) for Image Data (from scratch NumPy + PyTorch)](data_science/deeplearning/visual/cnn/00_overview.ipynb)
    - **Resnet**
      - [Residual Networks (ResNets) for Image Data (from scratch NumPy + PyTorch)](data_science/deeplearning/visual/resnet/00_overview.ipynb)
- **Machine Learning**
  - **Dimensionality Reduction**
    - **Tabular Data**
      - **Dbscan**
        - [DBSCAN — Density-Based Clustering (Finding crowds instead of shapes)](data_science/machine_learning/dimensionality_reduction/tabular_data/dbscan/00_overview.ipynb)
      - **Ica**
        - [Independent Component Analysis (ICA)](data_science/machine_learning/dimensionality_reduction/tabular_data/ica/00_overview.ipynb)
      - **Isomap**
        - [Isomap — Nonlinear Dimensionality Reduction (Geodesic Distances)](data_science/machine_learning/dimensionality_reduction/tabular_data/isomap/00_overview.ipynb)
      - **Lle**
        - [Locally Linear Embedding (LLE) — Manifold Learning (From Scratch)](data_science/machine_learning/dimensionality_reduction/tabular_data/lle/00_overview.ipynb)
      - **Mds**
        - [Multidimensional Scaling (MDS) — “Recreating a map using only pairwise distances”](data_science/machine_learning/dimensionality_reduction/tabular_data/mds/00_overview.ipynb)
      - **Pca**
        - [Principal Component Analysis (PCA) + Kernel PCA](data_science/machine_learning/dimensionality_reduction/tabular_data/pca/00_overview.ipynb)
      - **Tsne**
        - [t-SNE: Visualizing High-Dimensional Data (Preserve Friendships, Not Geography)](data_science/machine_learning/dimensionality_reduction/tabular_data/tsne/00_overview.ipynb)
      - **Umap**
        - [UMAP (Uniform Manifold Approximation and Projection)](data_science/machine_learning/dimensionality_reduction/tabular_data/umap/00_overview.ipynb)
  - **Supervised Learning**
    - **Tabular Data**
      - **Gaussian Processes**
        - [Gaussian Processes (GP) — Regression & Probabilistic Classification](data_science/machine_learning/supervised_learning/tabular_data/gaussian_processes/00_overview.ipynb)
      - **Generalized Linear Models**
        - [Generalized Linear Models (GLMs)](data_science/machine_learning/supervised_learning/tabular_data/generalized_linear_models/00_overview.ipynb)
      - **K Nearest Neighbors**
        - [K-Nearest Neighbors (KNN) — Classification & Regression (From Scratch)](data_science/machine_learning/supervised_learning/tabular_data/k_nearest_neighbors/00_overview.ipynb)
      - **Linear And Quadratic Discriminant Analysis**
        - [Linear and Quadratic Discriminant Analysis (LDA / QDA)](data_science/machine_learning/supervised_learning/tabular_data/linear_and_quadratic_discriminant_analysis/00_overview.ipynb)
      - **Linear Regression And Co**
        - [Linear Regression & Friends (OLS, Ridge, Lasso, Elastic Net)](data_science/machine_learning/supervised_learning/tabular_data/linear_regression_and_co/00_overview.ipynb)
      - **Naive Bayes**
        - [Naive Bayes (Gaussian, Multinomial, Complement, Bernoulli, Categorical) + Out-of-core](data_science/machine_learning/supervised_learning/tabular_data/naive_bayes/00_overview.ipynb)
      - **Support Vector Machines**
        - [Support Vector Machines (SVC + SVR)](data_science/machine_learning/supervised_learning/tabular_data/support_vector_machines/00_overview.ipynb)
      - **Tree Based Algorithms**
        - [Tree-Based Algorithms (Decision Trees, Random Forests, Gradient Boosting)](data_science/machine_learning/supervised_learning/tabular_data/tree_based_algorithms/00_overview.ipynb)
- **Reinforcement Learning**
  - **ACKTR**
    - [ACKTR (Actor–Critic using Kronecker-Factored Trust Region)](data_science/reinforcement_learning/ACKTR/00_overview.ipynb)
    - [ACKTR from scratch (low-level PyTorch) — CartPole-v1](data_science/reinforcement_learning/ACKTR/01_acktr_from_scratch.ipynb)
  - **DDPG**
    - [DDPG (Deep Deterministic Policy Gradient) — Continuous Control](data_science/reinforcement_learning/DDPG/00_overview.ipynb)
    - [DDPG (Deep Deterministic Policy Gradient) — from scratch in PyTorch](data_science/reinforcement_learning/DDPG/01_ddpg_from_scratch.ipynb)
  - **DQN**
    - [Deep Q-Networks (DQN) for Discrete Action Spaces — Low-Level PyTorch](data_science/reinforcement_learning/DQN/00_overview.ipynb)
  - **GAIL**
    - [Generative Adversarial Imitation Learning (GAIL) — low-level PyTorch](data_science/reinforcement_learning/GAIL/00_overview.ipynb)
  - **HER**
    - [Hindsight Experience Replay (HER) — low-level PyTorch (DDPG) in a goal-based environment](data_science/reinforcement_learning/HER/00_overview.ipynb)
  - **PPO1**
    - [PPO1 (PPO-Clip) — low-level PyTorch implementation](data_science/reinforcement_learning/PPO1/00_overview.ipynb)
  - **PPO2**
    - [Proximal Policy Optimization 2 (PPO2) — from scratch in PyTorch](data_science/reinforcement_learning/PPO2/00_overview.ipynb)
  - **SAC**
    - [Soft Actor-Critic (SAC) for Continuous Action Spaces (low-level PyTorch)](data_science/reinforcement_learning/SAC/00_overview.ipynb)
  - **TD3**
    - [Twin Delayed DDPG (TD3) — from scratch in PyTorch](data_science/reinforcement_learning/TD3/00_overview.ipynb)
  - **TRPO**
    - [TRPO (Trust Region Policy Optimization) — low-level PyTorch implementation](data_science/reinforcement_learning/TRPO/00_overview.ipynb)

### Backend

### Frontend

### DevOps
- **Cloud**
  - **Aws**
    - **Cloudformation**
      - [AWS CloudFormation](devops/cloud/aws/cloudformation/00_overview.ipynb)
    - **Cloudfront**
      - [AWS CloudFront](devops/cloud/aws/cloudfront/00_overview.ipynb)
    - **Cloudwatch**
      - [Amazon CloudWatch](devops/cloud/aws/cloudwatch/00_overview.ipynb)
    - **Dynamodb**
      - [Amazon DynamoDB](devops/cloud/aws/dynamodb/00_overview.ipynb)
    - **Ec2**
      - [Amazon EC2 (Elastic Compute Cloud)](devops/cloud/aws/ec2/00_overview.ipynb)
    - **Ecs**
      - [Amazon ECS (Elastic Container Service)](devops/cloud/aws/ecs/00_overview.ipynb)
    - **Eks**
      - [Amazon EKS (Elastic Kubernetes Service)](devops/cloud/aws/eks/00_overview.ipynb)
    - **Elasticache**
      - [Amazon ElastiCache](devops/cloud/aws/elasticache/00_overview.ipynb)
    - **Emr**
      - [Amazon EMR (Elastic MapReduce)](devops/cloud/aws/emr/00_overview.ipynb)
    - **Eventbridge**
      - [Amazon EventBridge](devops/cloud/aws/eventbridge/00_overview.ipynb)
    - **Glue**
      - [AWS Glue](devops/cloud/aws/glue/00_overview.ipynb)
    - **Lambda**
      - [AWS Lambda](devops/cloud/aws/lambda/00_overview.ipynb)
    - **Mwaa**
      - [AWS Managed Workflows for Apache Airflow (MWAA)](devops/cloud/aws/mwaa/00_overview.ipynb)
    - **Rds**
      - [Amazon RDS (Relational Database Service)](devops/cloud/aws/rds/00_overview.ipynb)
    - **S3**
      - [Amazon S3 (Simple Storage Service)](devops/cloud/aws/s3/00_overview.ipynb)
    - **Snowflake**
      - [Snowflake (Cloud Data Platform)](devops/cloud/aws/snowflake/00_overview.ipynb)
    - **Sns**
      - [Amazon SNS (Simple Notification Service)](devops/cloud/aws/sns/00_overview.ipynb)
    - **Sqs**
      - [Amazon SQS (Simple Queue Service)](devops/cloud/aws/sqs/00_overview.ipynb)
    - **Step Functions**
      - [AWS Step Functions](devops/cloud/aws/step_functions/00_overview.ipynb)
    - **Vpc**
      - [Amazon VPC (Virtual Private Cloud)](devops/cloud/aws/vpc/00_overview.ipynb)

### Cybersecurity


<!-- CKC_INDEX_END -->

## Git Remote
Target repository: `https://github.com/tempathack/comprehensive_knowledge_collection.git`
