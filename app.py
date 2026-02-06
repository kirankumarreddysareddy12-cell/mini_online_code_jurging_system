from flask import Flask, render_template, request, jsonify
from executor import run_user_code
from problems import PROBLEMS, get_problem

app = Flask(__name__)

def normalize_output(text):
    """
    Normalize output:
    - remove extra spaces
    - remove blank lines
    - strip newlines
    """
    return "\n".join(
        line.strip() for line in text.strip().splitlines() if line.strip() != ""
    )

@app.route("/")
def home():
    return render_template("index.html", problems=PROBLEMS)

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()

    code = data["code"]
    pid = data["problem"]

    # Accept user input
    user_input = data.get("customInput", "").strip()

    problem = get_problem(pid)

    # Default sample input if nothing entered
    final_input = user_input if user_input else problem.get("sample_input", "2 3")

    # Run user code
    output, error = run_user_code(code, final_input)

    # Show runtime/syntax errors
    if error:
        return jsonify({
            "status": "error",
            "result": "Error ❌",
            "output": error
        })

    # 🔥 Generate correct expected output dynamically
    expected_output = problem["solver"](final_input)

    user_out = normalize_output(output)
    expected_out = normalize_output(expected_output)

    if user_out == expected_out:
        result = "Passed ✅"
    else:
        result = "Failed ❌"

    return jsonify({
        "status": "success",
        "result": result,
        "output": output,
        "expected": expected_output
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
