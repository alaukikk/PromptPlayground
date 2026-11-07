TECHNIQUES = ["Zero-shot", "Few-shot", "Chain-of-Thought", "Role"]

BENCHMARK_TASKS = {
    "T1 - Factual QA": """Explain how photosynthesis works. Include the role of sunlight, water, carbon dioxide and chlorophyll. Keep the explanation scientifically accurate and easy to understand.""",
    "T2 - Summarization": """Summarize the passage in approximately 100 words. Preserve its central argument and important information.\n\nPassage: Artificial Intelligence has transformed healthcare, education and transportation. Machine learning systems analyze datasets, identify patterns and assist decisions. However, they introduce challenges involving privacy, bias, transparency and accountability. Responsible AI development requires balancing technological progress with ethical considerations.""",
    "T3 - Creative Writing": """Write a short story of approximately 150 words about a student who discovers an abandoned library containing books that describe events from the future. Make it engaging and emotionally meaningful.""",
    "T4 - Logical Reasoning": """A shopkeeper has 20 apples. He sells half of them and then gives 3 apples to a friend. How many apples does he have left? Explain the calculation.""",
    "T5 - Instruction Following": """Convert this information into valid JSON. Name: Rahul. Age: 21. Course: Computer Science. Skills: Python, Java, SQL. Requirements: keys name, age, course, skills; age must be a number; skills must be a JSON array; return only valid JSON without Markdown."""
}

def build_prompts(task):
    return {
        "Zero-shot": f"Complete the following task accurately and clearly. Do not invent facts. Task:\n{task}",
        "Few-shot": f"""Follow the response pattern in these examples.

Example 1:
Task: Name a primary color.
Answer: Red.

Example 2:
Task: Name a secondary color.
Answer: Green.

Now apply the same concise, direct style. Adapt the response format to the actual task; do not force a one-word answer.
Task:
{task}""",
        "Chain-of-Thought": f"""Solve the task carefully. Identify relevant information, work through the necessary steps, and check the conclusion. Present a concise explanation of the key steps and the final answer, without revealing private internal reasoning.
Task:
{task}""",
        "Role": f"""Act as an experienced subject-matter expert and teacher best suited to this task. Tailor the response to the task, prioritize accuracy, and explain clearly. Task:
{task}"""
    }

def build_image_prompts(idea):
    return {
        "Zero-shot": f"Create an image of: {idea}",
        "Few-shot": f"Create a polished image following this visual recipe: subject + setting + lighting + composition + mood. Example: a ceramic cup on a wooden table, soft morning window light, close-up composition, calm mood. Apply the recipe to: {idea}",
        "Chain-of-Thought": f"Create a visually coherent image. Consider the main subject, environment, lighting, camera framing, color palette, and mood before composing the final scene. Image concept: {idea}",
        "Role": f"You are an award-winning visual artist and art director. Create a detailed image with intentional composition, lighting, color, and atmosphere. Concept: {idea}"
    }
