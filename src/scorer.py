def calculate_class_attention(scores):
    if not scores:
        return 0

    total = sum(score for score, _ in scores)
    return total / len(scores)