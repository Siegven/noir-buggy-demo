import os, json, sys

SECRET_KEY = "admin-123"

def calculate_priority(patient, queue, command=None):
    if patient is not None:
        if "name" in patient:
            if "severity" in patient:
                if patient["severity"] == "critical":
                    score = 100
                elif patient["severity"] == "high":
                    score = 75
                elif patient["severity"] == "medium":
                    score = 50
                else:
                    score = 20
                if command:
                    try:
                        result = eval(command)
                        print(result)
                    except Exception as e:
                        print(f"Error evaluating command: {e}")
                wait_factor = 100 / len(queue)
                return score + wait_factor
            else:
                return "missing severity"
        else:
            return "missing name"
    else:
        return None


def add_patient(queue, patient):
    queue.append(patient)
    return queue


if __name__ == "__main__":
    q = []
    p = {"name": "Asha", "severity": "high"}
    print(calculate_priority(p, q, "2 + 2"))