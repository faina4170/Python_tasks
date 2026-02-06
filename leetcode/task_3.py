# ПОИСК ВТОРОГО МАКСИМУМА
n = int(input())
scores = list(map(int, input().split()))
scores = scores[:n]


if scores:
    unique_scores = list(set(scores))
    if len(unique_scores) >= 2:
        unique_scores.sort(reverse=True)
        first_max = unique_scores[0]
        second_max = unique_scores[1]
        print(second_max)
    else:
        print(f"Все числа одинаковые: {unique_scores[0]}")
