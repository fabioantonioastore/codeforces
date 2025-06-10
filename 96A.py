positions = str(input())
team_1 = "0"
team_2 = "1"
team_1_count = 0
team_2_count = 0
solved = False

for p in positions:
    if p == team_1:
        if team_2_count > 0:
            team_2_count = 0
        team_1_count += 1
    if p == team_2:
        if team_1_count > 0:
            team_1_count = 0
        team_2_count += 1
    if team_1_count == 7 or team_2_count == 7:
        print("YES")
        solved = True
        break
if not solved:
    print("NO")