"""
Prompt Engineering Module
Implements:
1. Role Prompting
2. Task Prompting
3. Output Formatting
4. Few-shot Prompting
5. Chain of Thought Prompting
6. Self-Consistency Simulation
"""


class PromptEngine:

    def __init__(self):
        pass

    def build_prompt(
        self,
        role,
        task,
        output_format,
        examples="",
        chain_of_thought=False
    ):
        """
        Build a complete prompt.
        """

        prompt = ""

        if role:
            prompt += f"Role:\n{role}\n\n"

        if task:
            prompt += f"Task:\n{task}\n\n"

        if output_format:
            prompt += f"Output Format:\n{output_format}\n\n"

        if examples.strip():
            prompt += "Examples:\n"
            prompt += examples
            prompt += "\n\n"

        if chain_of_thought:
            prompt += (
                "Think through the problem step by step "
                "internally before producing the final answer.\n"
            )

        return prompt

    def few_shot(self, examples, new_question):
        """
        Build Few-shot Prompt
        """

        prompt = "Learn from the following examples:\n\n"

        prompt += examples

        prompt += "\n\nNow solve:\n"

        prompt += new_question

        return prompt

    def self_consistency(self, question):
        """
        Demonstration only.
        Simulates three reasoning paths.
        """

        responses = []

        for i in range(1, 4):
            responses.append(
                f"Reasoning Path {i}:\n"
                f"- Analyse the question.\n"
                f"- Consider different possibilities.\n"
                f"- Produce Answer {i}.\n"
            )

        final = (
            "\nFinal Decision:\n"
            "Choose the answer that appears most consistent "
            "across all reasoning paths."
        )

        return "\n".join(responses) + final