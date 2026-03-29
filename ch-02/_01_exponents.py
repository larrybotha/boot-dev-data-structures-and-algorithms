def get_estimated_spread(audiences_followers: list[int]):
    num_followers = len(audiences_followers)
    avg = sum(audiences_followers) / num_followers if num_followers > 0 else 0
    result = avg * (num_followers**1.2)

    return result
