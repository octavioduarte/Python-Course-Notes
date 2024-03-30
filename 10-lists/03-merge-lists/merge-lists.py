sp_teams = ["CORINTHIANS", "sep", "spfc", "sfc"]
rj_teams = ["crf", "ffc", "crb", "crvg"]

sp_and_rj_teams_way_1 = sp_teams + rj_teams
print(sp_and_rj_teams_way_1)
# ['CORINTHIANS', 'sep', 'spfc', 'sfc', 'crf', 'ffc', 'crb', 'crvg']

sp_teams.extend(rj_teams)
print(sp_teams)
# ['CORINTHIANS', 'sep', 'spfc', 'sfc', 'crf', 'ffc', 'crb', 'crvg']
