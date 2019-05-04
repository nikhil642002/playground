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

    seats = pd.read_csv('../inputs/EPE2014-AvailSeats.csv')
    seats = seats.set_index('Electoral region')
    seats.index = seats.index.str.strip()
    seats = seats.drop('Northern Ireland', axis=0)
    seats = seats.fillna(0)

    votescast = votes.T.apply(lambda x: x.dropna().to_dict()).to_dict()
    seatsavail = seats.to_dict()['Representation']
    print('Votes cast by party')
    print(votescast)
    print('Seats available by constituency')
    print(seatsavail)

if __name__ == '__main__':
    main()
