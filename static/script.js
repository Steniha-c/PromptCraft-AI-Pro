// Generate Prompt
async function generatePrompt() {

    const role = document.getElementById("role").value;

    const task = document.getElementById("task").value;

    const format = document.getElementById("format").value;

    const examples = document.getElementById("examples").value;

    const cot = document.getElementById("cot").checked;

    const response = await fetch("/generate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            role: role,
            task: task,
            format: format,
            examples: examples,
            cot: cot
        })

    });

    const data = await response.json();

    // Show Prompt
    document.getElementById("promptResult").textContent = data.prompt;

    // Show Score
    document.getElementById("score").textContent =
        "Overall Score : " + data.score + "/100";

    // Checklist
    let checklistText = "";

    for (const key in data.checklist) {

        checklistText += key + " : " + data.checklist[key] + "\n";

    }

    document.getElementById("checklist").textContent = checklistText;

    // Suggestions

    const suggestionList =
        document.getElementById("suggestions");

    suggestionList.innerHTML = "";

    if (data.suggestions.length === 0) {

        const li = document.createElement("li");

        li.innerText = "Excellent Prompt! No Suggestions.";

        suggestionList.appendChild(li);

    } else {

        data.suggestions.forEach(item => {

            const li = document.createElement("li");

            li.innerText = item;

            suggestionList.appendChild(li);

        });

    }

}