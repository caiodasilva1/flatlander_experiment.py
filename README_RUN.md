# Run instructions (minimal)

This repository contains several Jupyter notebooks. This small helper runs the Parrot_experiment.ipynb notebook non-interactively and saves an executed notebook.

Prerequisites
- Python 3.8+
- Install dependencies:

  python -m pip install -r requirements.txt

Run the experiment

  python3 scripts/run_parrot_experiment.py --notebook Parrot_experiment.ipynb --output Parrot_experiment_executed.ipynb

Notes
- The script uses nbclient to execute the notebook. If the notebook depends on datasets or environment variables not present in the repo, provide them before running.
- If you want the executed notebook to replace the original file, omit the --output argument.
