# run_all_utility_tests.py
#
# This script serves as a unified test runner for the utility modules:
# filesystem_utils.py, logging_utils.py, network_utils.py, and path_utils.py.
# It executes the self-test block of each module by running them as separate
# subprocesses, ensuring their independent functionality and proper cleanup.
# run_all_utility_tests.py
#
# This script serves as a unified test runner for the utility modules:
# filesystem_utils.py, logging_utils.py, network_utils.py, and path_utils.py.
# It executes the self-test block of each module by running them as separate
# subprocesses, ensuring their independent functionality and proper cleanup.

import sys
import subprocess
from pathlib import Path
import os
import shutil
import tempfile
import logging 

script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir.parent.parent))

from src.utils import *

def find_project_root_for_runner() -> Path:
    """
    Attempts to find the 'Universal_RunnerApp' project root by searching
    up from the current script's location.
    """
    current_script_dir = Path(__file__).resolve().parent
    # Search up to 5 levels to find 'Universal_RunnerApp' containing 'src'
    for parent in [current_script_dir] + list(current_script_dir.parents):
        if (parent / "src").is_dir() and parent.name == "Universal_RunnerApp":
            return parent
    raise RuntimeError("Could not determine Universal Runner's 'Main Application Root' for test runner.")

# Set up a basic logger for the test runner itself
def setup_runner_logging():
    """Sets up a basic console logger for the test runner script."""
    # Clear existing handlers to prevent duplicate logs if called multiple times
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [TestRunner] - %(message)s')
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO) # Set level for the runner's output

    logging.root.addHandler(console_handler)
    logging.root.setLevel(logging.INFO) # Set root logger level
    logging.info("Test runner logging initialized.")

# Call setup for the runner's logging
setup_runner_logging()

# Determine the project root
try:
    project_root = find_project_root_for_runner()
    logging.info(f"Detected project root for test runner: {project_root}")
except RuntimeError as e:
    logging.critical(f"Setup Error: {e}")
    sys.exit(1)

# List of utility modules to test, relative to the project root
UTILITY_MODULES = [
    project_root / "src" / "utils" / "path_utils.py",
    project_root / "src" / "utils" / "filesystem_utils.py",
    project_root / "src" / "utils" / "logging_utils.py",
    project_root / "src" / "utils" / "network_utils.py",
]

def run_module_self_test(module_path: Path) -> bool:
    """
    Runs the self-test block of a given Python module as a subprocess.

    Args:
        module_path (Path): The absolute path to the Python module file.

    Returns:
        bool: True if the self-test passes, False otherwise.
    """
    logging.info(f"\n--- Running self-test for {module_path.name} ---")
    module_name = f"universal_runner.utils.{module_path.stem}"
    result = subprocess.run(
        [sys.executable, "-m", module_name],
        cwd=str(project_root),
        capture_output=True,
        text=True,
        check=False
    )
    logging.info(f"Output from {module_path.name}:\n{result.stdout}")
    if result.stderr:
        logging.error(f"Errors from {module_path.name}:\n{result.stderr}")
    if result.returncode == 0:
        logging.info(f"Self-test for {module_path.name} PASSED.")
        return True
    else:
        logging.error(f"Self-test for {module_path.name} FAILED with exit code {result.returncode}.")
        return False
