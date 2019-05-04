import pandas as pd


def main():
    votes = pd.read_csv('../inputs/EPE2014-Votes.csv')
    votes = votes.set_index('Local Authority')
    # strip leading/trailing spaces from index/column values
    votes.index = votes.index.str.strip()
    votes.columns = votes.columns.str.strip()

    # Drop unnecessary columns
    votes = votes.drop(
        ['Total number of valid votes counted', 'Eligible Electorate', 'Valid vote % turnout', 'Unnamed: 4'], axis=1)

    # Drop Northern Ireland and NI-only parties, as they use Single Transferable Vote system
    votes = votes.drop('Northern Ireland', axis=0)
    votes = votes.dropna(axis=1, how='all')
    votes = votes.sort_index()

    # Can't convert df to int as it contains NaN so values in votes are comma delimited numbers stored as strings
    votes = votes.T.apply(lambda x: x.dropna().to_dict()).to_dict()

    # Strip commas and convert values to int
    votescast = {}
    for key in votes.keys():
        votescast[key] = {k: int(v.replace(',', '')) for k, v in votes[key].items()}

    seats = pd.read_csv('../inputs/EPE2014-AvailSeats.csv')
    seats = seats.set_index('Electoral region')
    seats.index = seats.index.str.strip()
    seats = seats.drop('Northern Ireland', axis=0)
    seats = seats.sort_index()

    # seats contains no NaNs so pandas imports directly as int
    seatsavail = seats.to_dict()['Representation']

    resultsseats = pd.read_csv('../inputs/EPE2014-ResultsSeats.csv')

    resultsseats = resultsseats.set_index('Local Authority')
    # strip leading/trailing spaces from index/column values
    resultsseats.index = resultsseats.index.str.strip()
    resultsseats.columns = resultsseats.columns.str.strip()

    # Drop Northern Ireland and NI-only parties, as they use Single Transferable Vote system
    resultsseats = resultsseats.drop('Northern Ireland', axis=0)
    resultsseats = resultsseats.dropna(axis=1, how='all')
    resultsseats = resultsseats.sort_index()

    resultsseats = resultsseats.T.apply(lambda x: x.dropna().to_dict()).to_dict()

    results = {}
    for key in resultsseats.keys():
        results[key] = {k: int(v) for k, v in resultsseats[key].items()}

    print('Votes cast by party')
    print(votescast)
    print('Seats available by constituency')
    print(seatsavail)
    print('Seats actually won by party by constituency')
    print(results)


if __name__ == '__main__':
    main()
