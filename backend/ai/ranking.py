def rank_candidates(candidates):

    return sorted(
        candidates,
        key=lambda x: x["skill_match_score"],
        reverse=True
    )