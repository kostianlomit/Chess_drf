from django.test import TestCase


from chess_friends.models import Chess

chess = Chess.objects.create(title='hour')

def test_title(self, title):
    self.assertEqual(chess.title, 'hour')