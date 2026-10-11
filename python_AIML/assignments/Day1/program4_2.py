def calculate_score(total_sum: int, bonus_points: int) -> int:
    return total_sum + bonus_points


total_sum = 10
bonus_points = 20

print(f"Data Type of total_sum is {type(total_sum)} and")
print(f"bonus_points is {type(bonus_points)}")

final_score = calculate_score(total_sum, bonus_points)

print(f"Final Score is {final_score}")