"""this files have functions that modifing them will give the user an easy way to change the behvior of the calculations and sorting"""

from itertools import groupby


def calculate_group_score(params, app_sizes):
    apps = {i: len(list(j)) for i, j in groupby(sorted(params, key=lambda k: k.app_index), key=lambda k: k.app_index)}
    res = 0
    for k,v in apps.items():
        res += v/(app_sizes[k]*len(apps))
    return res

def calculate_offer_score(groups):
   return sum(map(lambda g: g.score, groups))/len(groups)

def sort_fleet_offers(offers):
    return sorted(offers,key=lambda g: g.total_price)[:30]
