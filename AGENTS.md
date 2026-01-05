# Comprehensive Knowledge Collection (CKC)

## Summary
This repository is a long-lived, portfolio-style knowledge base for computer science and software engineering topics. The default format is **Jupyter notebooks** (explanations + visuals + runnable code). When a topic needs “real” structure (servers, infra, apps), keep the runnable code alongside the notebook inside the relevant topic folder.

Primary sections (top-level directories; notebooks live directly in subtopic folders):
- **Data Science**: statistics, ML, algorithms, deep learning, time series, NLP; emphasis on *intuition + plots* and “from-scratch” NumPy implementations alongside practical library usage.
- **DevOps**: common architectures and tradeoffs, containers/Kubernetes, cloud fundamentals, CI/CD, observability/SRE, and Infrastructure-as-Code (Terraform, etc.).
- **Backend**: FastAPI-focused patterns (validation, dependency injection, auth, testing, async, databases, background jobs), plus broader API and system design fundamentals.
- **Cybersecurity**: fundamentals, web/network security, secure coding, threat modeling, common vulnerabilities, and safe tooling walkthroughs.
- **Frontend**: HTML/CSS/JS/TS foundations, framework comparisons (React/Next.js/Vue/Svelte), state management, testing, performance, and accessibility.

## Repository Layout
- `CKC_REGISTER.ipynb`: main register notebook that auto-generates the index.
- `README.md`: GitHub-facing overview + auto-generated index block.
- `data_science/`, `devops/`, `backend/`, `cybersecurity/`, `frontend/`: the main knowledge base.
  - Optional extra files (code, configs, diagrams) can live in the same topic folder.

## Notebook Conventions
- **Naming**: use two-digit ordering + snake_case, e.g. `01_linear_regression_from_scratch.ipynb`.
- **Structure** (recommended sections):
  - Title + goals
  - Prerequisites (math/tools)
  - Intuition (diagrams/plots)
  - Derivation / key equations (optional)
  - Implementation (NumPy “from scratch” when relevant)
  - Practical usage (sklearn/torch/etc.)
  - Pitfalls + diagnostics
  - Exercises + references
- **Reproducibility**: set seeds, pin/record versions when results depend on them, avoid hidden state.
- **Plots**: label axes/units, annotate key takeaways, keep figures readable.
  - For Plotly notebooks, set `pio.renderers.default = "notebook"` in the first import/config cell.

## Folder Rule (Leaf Topics)
- Every “final” (leaf) folder should contain at least one notebook.
- Recommended: keep a `00_overview.ipynb` per leaf folder, then add numbered topic notebooks.
- `CKC_REGISTER.ipynb` can auto-create missing `00_overview.ipynb` files for leaf folders.

## Content Safety (Cybersecurity)
- No real secrets, tokens, or personal data in repo history.
- Keep examples legal/safe: prefer local targets (containers, toy apps, intentionally vulnerable sandboxes).
