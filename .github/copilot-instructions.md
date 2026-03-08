# AI Instructions (AGENTS / CLAUDE / Copilot)

## WHY

- This repo uses a uniform, reproducible workflow based on **uv** and **pyproject.toml**.
- These instructions exist to prevent tool drift (e.g., pip) and OS mismatch.

## Requirements

- Use **uv** for all environment, dependency, and run commands in this repo.
- Do **not** recommend or use `pip install ...` as the primary workflow.
- This repo targets **Python 3.14**, pinned via uv.
- Commands and guidance must work on Windows, macOS, and Linux.
- If shell-specific commands are unavoidable, provide both:
  - PowerShell (Windows)
  - bash/zsh (macOS/Linux)

## Quickstart

- Install **uv** using the official method for your OS.
- Keep uv current.
- Pin Python 3.14 for this project using uv.
- Sync dependencies (dev + docs) and upgrade.

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

## Common Tasks

Run all commands via **uv**.

- Tests:

```shell
uv run pytest
```

- Lint / format:

```shell
uv run ruff format .
uv run ruff check .
```

- Type check:

```shell
uv run pyright .
```

- Docs (serve / build):

```shell
uv run mkdocs serve
uv run mkdocs build
```

## pre-commit (Optional)

- pre-commit is optional locally; CI is authoritative.
- pre-commit runs only on tracked / staged files.
- Developers should `git add` relevant files before expecting hooks to run.
