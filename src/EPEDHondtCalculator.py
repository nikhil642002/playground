from functools import partial
from EPEDataPrep import prep
from collections import Counter

dhont_quotient = lambda v: v + 1
modified_dhont_quotient = lambda v: 2 ** v
webster_quotient = lambda v: 2 * v + 1


def average_voting(quotient, votes, seats):
    '''

    :param quotient:
    :param votes:
    :param seats:
    :return:
    '''
    results = {party: 0 for party in votes}
    while sum(results.values()) < seats:
        victor = max(votes.keys(), key=lambda party: votes[party] / quotient(results[party]))
        results[victor] += 1
    return results


dhondt = partial(average_voting, dhont_quotient)
modified_dhondt = partial(average_voting, modified_dhont_quotient)
webster = partial(average_voting, webster_quotient)

wiki_example = {
    "Party A": 100000,
    "Party B": 80000,
    "Party C": 30000,
    "Party D": 20000,
}

webster_example = {
    "Party A": 53000,
    "Party B": 24000,
    "Party C": 23000,
}

print(dhondt(wiki_example, 8))
print(modified_dhondt(wiki_example, 8))
print(webster(wiki_example, 8))
print()
print(dhondt(webster_example, 7))
print(modified_dhondt(webster_example, 7))
print(webster(webster_example, 7))
print()

votescast, seats_avail, results = prep()

total_dhondt = Counter()
total_modified_dhondt = Counter()
total_webster = Counter()
total_actual = Counter()

print("Results from the 2014 European Parliamentary Elections")
print("------------------------------------------------------")
for seat, result in votescast.items():
    calculated_dhondt = {k: v for k, v in dhondt(result, seats_avail[seat]).items() if v is not 0}
    total_dhondt.update(calculated_dhondt)
    calculated_modified_dhondt = {k: v for k, v in modified_dhondt(result, seats_avail[seat]).items() if v is not 0}
    total_modified_dhondt.update(calculated_modified_dhondt)
    calculated_webster = {k: v for k, v in modified_dhondt(result, seats_avail[seat]).items() if v is not 0}
    total_webster.update(calculated_webster)
    total_actual.update(results[seat])
    print()
    print(seat)
    print("-" * len(seat))
    print("Actual:      ", results[seat])
    print("D'Hondt:     ", calculated_dhondt)
    print("Modified D'H:", calculated_modified_dhondt)
    print("Webster:     ", calculated_webster)
    if seat == "London":
        for k, v in result.items():
            print(k, v)

print()
print("Sum totals")
print("----------")
print("Total Actual:      ", dict(total_actual))
print("Total D'Hondt:     ", dict(total_dhondt))
print("Total Modified D'H:", dict(total_modified_dhondt))
print("Total Webster:     ", dict(total_webster))
