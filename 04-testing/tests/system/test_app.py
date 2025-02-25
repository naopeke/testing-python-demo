from unittest import TestCase #unittestは、Pythonに標準でついているテスト用のライブラリです。TestCaseは、テストケースを作るための基本クラスです。テストを実行すると、unittestが自動的にtest_で始まるメソッドを見つけて実行します。
from unittest.mock import patch #unittest.mockは、テスト中に特定の部分を「モック」（偽物のオブジェクト）に置き換えるためのツールでModule。patchは、モックを作るための便利な関数Functionです。例えば、外部のAPIを呼び出す部分をモックに置き換えて、実際には呼び出さずにテストすることができます。
import app
from blog import Blog

class AppTest(TestCase): #AppTestクラスはTestCaseを継承
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author') #Blogクラスのインスタンスを作成
        app.blogs = {'Test': blog} #app.blogs辞書(app.py)にブログを追加
        with patch('builtins.print') as mocked_print: #patchを使って、print関数をモックに置き換えています。mocked_printは、モック化されたprint関数です。printはPythonの組み込み関数であり、builtinsモジュールに定義されています。そのため、patchでモック化する際は、builtins.printと完全なパスを指定する必要があります。
            app.print_blogs() #app.pyの中のprint_blogs関数を呼び出しています。
            mocked_print.assert_called_with('- Test by Test Author (0 posts)') #print関数が'- Test Blog'という文字列を出力するかどうかを確認しています。
