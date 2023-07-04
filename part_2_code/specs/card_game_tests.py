import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    pass


class TestCardGame(unittest.TestCase):
    def test_check_for_ace(self):
        game = CardGame()
        card = Card(value=1, suit="Spades")  
        self.assertTrue(game.check_for_ace(card))

    def test_highest_card(self):
        game = CardGame()
        card1 = Card(value=5, suit="Hearts")  
        card2 = Card(value=8, suit="Diamonds")  
        self.assertEqual(game.highest_card(card1, card2), card2)

    def test_cards_total(self):
        game = CardGame()
        cards = [
            Card(value=2, suit="Clubs"), 
            Card(value=4, suit="Spades"), 
            Card(value=6, suit="Hearts")
        ]
        self.assertEqual(game.cards_total(cards), "You have a total of 12")

if __name__ == '__main__':
    unittest.main()
