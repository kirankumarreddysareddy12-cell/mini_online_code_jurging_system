import subprocess
import sys
import os

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def run_user_code(code, user_input):
    """
    Executes user code in a separate temporary file with given input.
    Returns output and error (if any).
    """
    # Save user code in temp folder
    temp_file_path = os.path.join(TEMP_DIR, "user_code.py")
    with open(temp_file_path, "w") as f:
        f.write(code)

    # Normalize input: convert spaces to newlines
    safe_input = "\n".join(user_input.strip().split()) + "\n"

    try:
        result = subprocess.run(
            [sys.executable, temp_file_path],
            input=safe_input,
            text=True,
            capture_output=True,
            timeout=5
        )

        if result.stderr:
            return "", result.stderr

        return result.stdout.strip(), ""

    except subprocess.TimeoutExpired:
        return "", "Time Limit Exceeded ⏱️"

    except Exception as e:
        return "", str(e)
