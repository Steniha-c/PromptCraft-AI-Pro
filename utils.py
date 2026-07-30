"""
Utility functions for PromptCraft AI
- Validate prompt components
- Calculate prompt quality score
- Generate improvement suggestions
"""


def evaluate_prompt(role, task, output_format, examples, cot):
    """
    Evaluate the quality of a prompt.
    Returns a score, checklist, and suggestions.
    """

    score = 0
    checklist = {}
    suggestions = []

    # Role
    if role.strip():
        score += 20
        checklist["Role"] = "✅ Present"
    else:
        checklist["Role"] = "❌ Missing"
        suggestions.append("Add a clear role for the AI.")

    # Task
    if task.strip():
        score += 20
        checklist["Task"] = "✅ Present"
    else:
        checklist["Task"] = "❌ Missing"
        suggestions.append("Describe the task clearly.")

    # Output Format
    if output_format.strip():
        score += 20
        checklist["Format"] = "✅ Present"
    else:
        checklist["Format"] = "❌ Missing"
        suggestions.append("Specify the expected output format.")

    # Examples (Few-shot)
    if examples.strip():
        score += 20
        checklist["Examples"] = "✅ Present"
    else:
        checklist["Examples"] = "❌ Missing"
        suggestions.append("Include one or more examples.")

    # Chain of Thought
    if cot:
        score += 20
        checklist["Chain of Thought"] = "✅ Enabled"
    else:
        checklist["Chain of Thought"] = "❌ Disabled"
        suggestions.append("Enable Chain of Thought if complex reasoning is needed.")

    return score, checklist, suggestions


def print_report(score, checklist):
    """
    Return a formatted report string.
    """

    report = "\n========== Prompt Report ==========\n"

    for key, value in checklist.items():
        report += f"{key:<20}: {value}\n"

    report += "\n-----------------------------------\n"
    report += f"Overall Score : {score}/100\n"

    if score >= 80:
        report += "Quality       : Excellent ⭐⭐⭐⭐⭐"
    elif score >= 60:
        report += "Quality       : Good ⭐⭐⭐⭐"
    elif score >= 40:
        report += "Quality       : Average ⭐⭐⭐"
    else:
        report += "Quality       : Needs Improvement ⭐"

    return report


def sample_examples():
    """
    Sample Few-shot examples.
    """

    return """
Example 1
Input: Translate Hello to French
Output: Bonjour

Example 2
Input: Translate Thank you to French
Output: Merci
"""