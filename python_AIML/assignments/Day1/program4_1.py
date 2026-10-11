def calculate_score(total_sum, bonus_points):
    final_score = total_sum + bonus_points
    return final_score


total_sum = 10
bonus_points = 20

final_score = calculate_score(total_sum, bonus_points)

print(f"Final Score is {final_score}")