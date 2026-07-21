def calculate_weighted_score(scores: list, weights: list) -> float:

    if len(scores) != len(weights):
        raise ValueError("分数列表和权重列表长度必须一致")
    total_value = sum(s * w for s, w in zip(scores, weights))
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return total_value / total_weight

