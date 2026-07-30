from flask import Flask, render_template, request, jsonify
from prompt_engine import PromptEngine
from database import PromptDatabase
from utils import evaluate_prompt

app = Flask(__name__)

# Create PromptEngine object
engine = PromptEngine()
db = PromptDatabase()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    role = data.get("role", "")
    task = data.get("task", "")
    output_format = data.get("format", "")
    examples = data.get("examples", "")
    cot = data.get("cot", False)

    # Build Prompt
    prompt = engine.build_prompt(
        role=role,
        task=task,
        output_format=output_format,
        examples=examples,
        chain_of_thought=cot
    )

    # Evaluate Prompt
    score, checklist, suggestions = evaluate_prompt(
        role,
        task,
        output_format,
        examples,
        cot
    )

    print("=== /generate called ===")
    print("Role:", role)
    print("Task:", task)

    # Save Prompt
    db.save_prompt(
        role=role,
        task=task,
        output_format=output_format,
        examples=examples,
        prompt=prompt,
        score=score
    )

    print("Prompt saved successfully!")

    return jsonify({
        "prompt": prompt,
        "score": score,
        "checklist": checklist,
        "suggestions": suggestions
    })

@app.route("/history", methods=["GET"])
def history():

    prompts = db.get_all_prompts()

    history = []

    for row in prompts:

        history.append({

            "id": row[0],
            "role": row[1],
            "task": row[2],
            "format": row[3],
            "score": row[4],
            "created_at": row[5]

        })

    return jsonify(history)


@app.route("/fewshot", methods=["POST"])
def fewshot():

    data = request.get_json()

    examples = data.get("examples", "")
    question = data.get("question", "")

    result = engine.few_shot(examples, question)

    return jsonify({
        "fewshot": result
    })


@app.route("/selfconsistency", methods=["POST"])
def self_consistency():

    data = request.get_json()

    question = data.get("question", "")

    result = engine.self_consistency(question)

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)