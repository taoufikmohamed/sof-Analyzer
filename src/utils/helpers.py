def load_data(file_path):
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def format_output(data):
    formatted = ""
    for key, value in data.items():
        formatted += f"{key}: {value}\n"
    return formatted.strip()