function runCode() {
    // Get code, problem, and custom input
    let code = document.getElementById("code").value;
    let problem = document.getElementById("problem").value;
    let customInput = document.getElementById("customInput").value;

    fetch("/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            code: code,
            problem: problem,
            customInput: customInput
        })
    })
    .then(res => res.json())
    .then(data => {
        if(data.status === "error"){
            document.getElementById("output").innerText =
                "❌ Runtime / Syntax Error:\n" + data.output;
        } 
        else if(data.status === "success"){
            document.getElementById("output").innerText =
                "✅ Result: " + data.result +
                "\n\n🖨 Your Output:\n" + data.output +
                "\n\n🎯 Expected Output:\n" + data.expected;
        }
    })
    .catch(err => {
        document.getElementById("output").innerText = "❌ Error:\n" + err;
    });
}
