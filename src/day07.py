class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = self.get_type()

    symbol_order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
                    '2': 1, 'j': 0}
    types = {
        (1, 5): 7,
        (2, 4): 6,
        (2, 3): 5,
        (3, 3): 4,
        (3, 2): 3,
        (4, 2): 2,
        (5, 1): 1
    }

    def get_type(self):
        buckets = {}
        for card in self.cards:
            if card not in buckets:
                buckets[card] = 0
            buckets[card] += 1
        return Hand.types[len(buckets), max(buckets.values())]

    def part_2_transform(self):
        buckets = {}
        jockers_count = 0
        self.cards = self.cards.replace("J", "j")
        for card in self.cards:
            if card == "j":
                jockers_count += 1
            else:
                if card not in buckets:
                    buckets[card] = 0
                buckets[card] += 1
        max_bucket = (max(buckets.values()) if buckets else 0) + jockers_count
        buckets_count = len(buckets) if buckets else 1
        self.type = Hand.types[buckets_count, max_bucket]
    def __lt__(self, other):
        if self.type > other.type:
            return False
        elif self.type < other.type:
            return True

        for s, o in zip(self.cards, other.cards):

            a = self.symbol_order[s]
            b = self.symbol_order[o]
            if a < b:
                return True
            elif a > b:
                return False
        return 0


hands = []
for line in open('../inputs/day07.txt', 'r').readlines():
    cards, bid = line.split(sep = ' ')
    hands.append(Hand(cards, bid))


sorted_hands = sorted(hands)
result = 0
for i, hand in enumerate(sorted_hands):
    result += (i + 1) * hand.bid
    print(i, hand.cards, hand.type, hand.bid)

print(result)

for hand in hands:
    hand.part_2_transform()

sorted_hands = sorted(hands)
result2 = 0
for i, hand in enumerate(sorted_hands):
    result2 += (i + 1) * hand.bid
    print(i, hand.cards, hand.type, hand.bid)

print(result2)