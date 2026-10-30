import os, json, sys
import ast

SECRET_KEY = os.getenv("SECRET_KEY", "default-123")

def calculate_priority(patient, queue, command=None):
    if patient is None:
        return None
    if "name" not in patient:
        return "missing name"
    if "severity" not in patient:
        return "missing severity"
    
    severity = patient["severity"]
    if severity == "critical":
        score = 100
    elif severity == "high":
        score = 75
    elif severity == "medium":
        score = 50
    else:
        score = 20
    
    if command:
        try:
            result = ast.literal_eval(command)
            print(result)
        except Exception as e:
            print(f"Error evaluating command: {e}")
    
    wait_factor = 100 / len(queue) if queue else 0
    return score + wait_factor


def add_patient(queue, patient):
    queue.append(patient)
    return queue


if __name__ == "__main__":
    q = []
    p = {"name": "Asha", "severity": "high"}
    print(calculate_priority(p, q, "2 + 2"))