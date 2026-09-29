n = int(input())
contests_points = [int(i) for i in str(input()).split(sep=" ")]
past_contests_points = {contests_points[0]}
total_amazing = 0

for contest_point in contests_points[1::]:
    if contest_point < min(past_contests_points) or contest_point > max(past_contests_points):
        total_amazing += 1
    past_contests_points.add(contest_point)

print(total_amazing)