# CrystalForge Agent Core

**CrystalForge** is a lightweight, modular multi‑agent framework designed to accelerate rapid experimentation and productionization of autonomous agent workflows.  
This repository contains the **agent core**: the runner, agent interfaces, memory adapters, and utility helpers that coordinate agents, routing, and data I/O.

## Goals
- Provide a minimal, well‑documented core that orchestrates agents and their interactions.
- Keep components small and testable so teams can iterate on agent logic independently.
- Make it easy to swap memory backends, LLM clients, and runner strategies.

## Contents
- **runner.py** — entry point and orchestration loop.
- **agents/** — agent implementations and interfaces.
- **memory/** — lightweight memory artifacts and adapters (example spreadsheets for prototyping).
- **utils/** — helpers for I/O, parsing, and LLM client wrappers.
- **README.md** — this file.

## Quickstart

1. Clone the repo:

2. Create and activate a Python virtual environment:

3. Install dependencies (if a requirements.txt exists):

4. Run the runner (example):


## Development workflow
- Create a feature branch: `git checkout -b feat/<short-description>`
- Add tests for new behavior where applicable.
- Commit small, focused changes and push to GitHub.
- Open a pull request and request at least one reviewer.

## Conventions
- **Agents** implement a simple interface: `receive(input) -> actions` and `act(action)`.
- **Runner** orchestrates agent turns and resolves conflicts via routing rules in `utils/routing.py`.
- Keep side effects (file writes, network calls) isolated behind adapters in `utils/`.

## Recommended files to add
- `.gitignore` (Python + venv) — included in this repo.
- `LICENSE` — MIT recommended for open source.
- `requirements.txt` — pin runtime dependencies.
- `tests/` — unit tests for core logic.

## Contribution
Open issues for design discussions. Use PRs for changes. Keep commits descriptive.

## Contact
Owner: **Martin Langley** — GitHub: `MLangley01`

crystalforge-agent-core/
├─ runner.py
├─ README.md
├─ requirements.txt  (optional)
├─ .gitignore
├─ LICENSE
├─ agents/
│  ├─ __init__.py
│  ├─ idea_intake.py
│  ├─ discovery_agent.py
│  ├─ mvp_architect.py
│  └─ ... (agent modules)
├─ memory/
│  ├─ discovery.xlsx    (prototype data)
│  ├─ ideas.xlsx
│  └─ research.xlsx
├─ utils/
│  ├─ excel_utils.py
│  ├─ json_parser.py
│  ├─ ollama_client.py  (LLM adapter)
│  └─ routing.py
└─ tests/               (recommended)

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
ENV/
env/
env.bak/
venv.bak/

# Distribution / packaging
build/
dist/
*.egg-info/
.eggs/

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# PyInstaller
*.manifest
*.spec

# Unit test / coverage
htmlcov/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover

# IDEs and editors
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# OS files
.DS_Store
Thumbs.db

# Excel / data artifacts you may not want in repo
*.xlsx
*.xls

# Secrets (if any)
.env
.env.*
