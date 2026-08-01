// Generate Prompt
async function generatePrompt() {

    const role = document.getElementById("role").value;

    const task = document.getElementById("task").value;

    const format = document.getElementById("format").value;

    const examples = document.getElementById("examples").value;

    const cot = document.getElementById("cot").checked;

    document.getElementById("loading").style.display = "block";

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

    document.getElementById("loading").style.display = "none";

    // Show Prompt
    document.getElementById("promptResult").textContent = data.prompt;

    // Show AI Response
    await typeWriter(
    document.getElementById("aiResponse"),
    data.ai_response
);

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
    
loadHistory();

}
// Load Prompt History
async function loadHistory() {

    const response = await fetch("/history");

    const history = await response.json();

    const tbody = document.querySelector("#historyTable tbody");

    tbody.innerHTML = "";

    history.forEach(item => {

    tbody.innerHTML += `

    <tr>
        <td>${item.id}</td>
        <td>${item.role}</td>
        <td>${item.task}</td>
        <td>${item.score}</td>
        <td>${item.created_at}</td>
    </tr>

    `;

});

}

// Load history when page opens
loadHistory();

// AI Typing Animation
async function typeWriter(element, text, speed = 15) {

    element.textContent = "";

    for (let i = 0; i < text.length; i++) {

        element.textContent += text.charAt(i);

        await new Promise(resolve => setTimeout(resolve, speed));

    }

}