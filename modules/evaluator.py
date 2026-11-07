EVALUATION_CRITERIA = ["Accuracy", "Relevance", "Clarity", "Completeness"]

def calculate_score(ratings):
    if not ratings:
        return 0
    return round(sum(ratings.values()) / len(ratings), 2)
