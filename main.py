import database

cycle_info = database.get_cycle(1.2)

print(type(cycle_info))
print(len(cycle_info))

for player in cycle_info:
    print(player["username"])