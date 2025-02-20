from unittest import TestCase
from post import Post

class PostTest(TestCase):
# Post クラスを使って新しい投稿を作成し、そのインスタンスの title と content が期待した通りであることを確認します。
# self.assertEqual('Test', p.title) と self.assertEqual('Test Content', p.content) によって、p の title と content が正しい値を持っているかをテストします。
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

#  Post クラスの json メソッドが期待した辞書を返すことを確認します。
#  p.json() が {'title': 'Test', 'content': 'Test Content'} という辞書を返すことを self.assertDictEqual(expected, p.json()) で確認しています。   
    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())
