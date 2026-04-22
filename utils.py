import json

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def build_examples(data, top_k=5):
    examples = ""
    for d in data[:top_k]:
        examples += f"Q: {d['input']}\nA: {d['output']}\n\n"
    return examples