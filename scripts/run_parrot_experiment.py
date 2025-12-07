#!/usr/bin/env python3
"""
Run the Parrot_experiment.ipynb notebook headlessly.

This script executes the notebook non-interactively using nbclient and
writes an executed notebook to the provided output path (or overwrites the
input notebook if no output is provided).

Usage:
  python3 scripts/run_parrot_experiment.py --notebook Parrot_experiment.ipynb --output Parrot_experiment_run.ipynb

Requirements (see requirements.txt): nbformat, nbclient
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

from nbformat import read, write
from nbclient import NotebookClient, CellExecutionError


def run_notebook(nb_path: Path, out_path: Path | None, timeout: int = 600) -> None:
    if not nb_path.exists():
        print(f"Notebook not found: {nb_path}", file=sys.stderr)
        raise SystemExit(2)

    with nb_path.open("r", encoding="utf-8") as f:
        nb = read(f, as_version=4)

    client = NotebookClient(nb, timeout=timeout, kernel_name="python3")
    try:
        client.execute()
    except CellExecutionError as e:
        print("Error executing the notebook (aborting).", file=sys.stderr)
        print(str(e), file=sys.stderr)
        raise SystemExit(3)

    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as f:
            write(nb, f)
        print(f"Executed notebook written to: {out_path}")
    else:
        # Overwrite input notebook
        with nb_path.open("w", encoding="utf-8") as f:
            write(nb, f)
        print(f"Executed notebook overwritten: {nb_path}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run a notebook non-interactively")
    p.add_argument("--notebook", "-n", required=True, help="Path to the notebook to execute")
    p.add_argument("--output", "-o", required=False, help="Output executed notebook path (optional)")
    p.add_argument("--timeout", "-t", type=int, default=600, help="Cell execution timeout in seconds")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    nb_path = Path(args.notebook)
    out_path = Path(args.output) if args.output else None
    run_notebook(nb_path, out_path, timeout=args.timeout)


if __name__ == "__main__":
    main()
