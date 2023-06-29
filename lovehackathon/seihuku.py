CardSequence = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
OrderSequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
PlayerRankList = [0 for _ in range(52)]
PlayerHandList = [OrderSequence[CardSequence.index(Card)] for Card in input().split()]

HighestCardNum, LastPlayerIndex = 0, 52
while PlayerHandList.count(0) != 52:
    for Index, CardNum in enumerate(PlayerHandList):
        if LastPlayerIndex == Index:
            HighestCardNum = 0
        elif CardNum > HighestCardNum:
            HighestCardNum = CardNum
            LastPlayerIndex = Index
            PlayerHandList[Index] = 0
            PlayerRankList[Index] = max(PlayerRankList) + 1

for rank in PlayerRankList:
    print(rank)
