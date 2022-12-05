class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
class Hand:
	def __init__(self, cards):
		self.cards = cards
		assert len(cards) == 5

	def getNumCardsByRank(self):
		numCardsByRank = [0]*13
		for i in range(len(self.cards)):
			j = self.cards[i].rank
			assert 1 <= j <= 13
			numCardsByRank[j-1] += 1
		return numCardsByRank

	def getNumCardsBySuit(self):
		numCardsBySuit = [0]*4
		for i in range(len(self.cards)):
			j = self.cards[i].suit
			assert 0 <= j <= 3
			numCardsBySuit[j] += 1
		return numCardsBySuit

##############################################################

# use this function for atLeastStraight()
def hasConsecutivePositive(L, k):
	n = len(L)
	assert k <= n
	counter = 0
	for i in range(n+1):  # +1: account for wrapping
		if L[i%n] >= 1:
			counter += 1
			if counter == k:
				return True
		else:
			counter = 0  # reset
	return False

	
def atLeastStraight(hand):
	L = hand.getNumCardsByRank()
	return hasConsecutivePositive(L, 5)

	
# for some pattern
def atLeastFlush(hand):
	L = hand.getNumCardsBySuit()
	for i in range(len(L)):
		if L[i] == 5:
			return True
	return False
	
def straightFlush(hand):
	return atLeastStraight(hand) and atLeastFlush(hand)

def flush(hand):
	return atLeastFlush(hand) and not atLeastStraight(hand)

def straight(hand):
	return atLeastStraight(hand) and not atLeastFlush(hand)

##############################################################
	
# for some pattern
def hasMultipleCardsWithSameRank(hand, num):
	L = hand.getNumCardsByRank()
	for i in range(len(L)):
		if L[i] == num:
			return True
	return False
	
def quadruple(hand):
	return hasMultipleCardsWithSameRank(hand, 4)

def fullHouse(hand):
	return hasMultipleCardsWithSameRank(hand, 3) and \
		   hasMultipleCardsWithSameRank(hand, 2)
	
def triple(hand):
	return (not quadruple(hand)) and (not fullHouse(hand)) and\
		   hasMultipleCardsWithSameRank(hand, 3)

# counter pattern
def twoPair(hand):
	L = hand.getNumCardsByRank()
	
	if fullHouse(hand):
		return False
		
	counter = 0
	for i in range(len(L)):
		if L[i] == 2:
			counter += 1
	return counter == 2

def pair(hand):
	if quadruple(hand) or fullHouse(hand) or triple(hand) or twoPair(hand):
		return False
	return hasMultipleCardsWithSameRank(hand, 2)

##############################################################

def joker(cards):
	possible_cards = [[True, True, True, True] for i in range(13)]
	for i in range(4):
		possible_cards[cards[i].rank - 1][cards[i].suit] = False
	hands = []
	joker_card = []
	for i in range(13):
		for j in range(4):
			if possible_cards[i][j]:
				hands.append(Hand(cards + [Card(j, i+1)]))
				joker_card.append(Card(j, i+1))

	max_hand = 9; max_joker = None
	for i in range(len(hands)):
		if straightFlush(hands[i]):
			if 0 < max_hand: max_hand = 0; max_joker = joker_card[i]
		elif quadruple(hands[i]):
			if 1 < max_hand: max_hand = 1; max_joker = joker_card[i]
		elif fullHouse(hands[i]):
			if 2 < max_hand: max_hand = 2; max_joker = joker_card[i]
		elif flush(hands[i]):
			if 3 < max_hand: max_hand = 3; max_joker = joker_card[i]
		elif straight(hands[i]):
			if 4 < max_hand: max_hand = 4; max_joker = joker_card[i]
		elif triple(hands[i]):
			if 5 < max_hand: max_hand = 5; max_joker = joker_card[i]
		elif twoPair(hands[i]):
			if 6 < max_hand: max_hand = 6; max_joker = joker_card[i]
		elif pair(hands[i]):
			if 7 < max_hand: max_hand = 7; max_joker = joker_card[i]
	return max_joker
