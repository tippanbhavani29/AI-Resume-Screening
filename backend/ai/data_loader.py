import json

def load_jd():
    with open(r'datasets\jobs\role_jd.json', 'r') as f:
        data = json.load(f)
    return data


def load_resumes():
    with open(r'datasets\resumes\resumes.json', 'r') as f:
        data = json.load(f)
    return data