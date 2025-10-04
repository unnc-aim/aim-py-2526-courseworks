import os
import subprocess
import sys


def test_main_outputs_hello_world():
    """Run main.py and assert that its output contains 'Hello World' (case-insensitive)."""
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    proc = subprocess.run([sys.executable, 'main.py'],
                          cwd=project_root, capture_output=True, text=True)
    output = (proc.stdout or '') + (proc.stderr or '')
    assert 'Hello World' in output, f"Expected 'Hello World' in output, got:\n{output!r}"
