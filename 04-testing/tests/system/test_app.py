from unittest import TestCase #unittestは、Pythonに標準でついているテスト用のライブラリです。TestCaseは、テストケースを作るための基本クラスです。テストを実行すると、unittestが自動的にtest_で始まるメソッドを見つけて実行します。
from unittest.mock import patch, mock_open #unittest.mockは、テスト中に特定の部分を「モック」（偽物のオブジェクト）に置き換えるためのツールでModule。patchは、モックを作るための便利な関数Functionです。例えば、外部のAPIを呼び出す部分をモックに置き換えて、実際には呼び出さずにテストすることができます。
import app
from blog import Blog
import requests #pip install requests
import random
from datetime import datetime

class AppTest(TestCase): #AppTestクラスはTestCaseを継承
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author') #Blogクラスのインスタンスを作成
        app.blogs = {'Test': blog} #app.blogs辞書(app.py)にブログを追加
        with patch('builtins.print') as mocked_print: #patchを使って、print関数をモックに置き換えています。mocked_printは、モック化されたprint関数です。printはPythonの組み込み関数であり、builtinsモジュールに定義されています。そのため、patchでモック化する際は、builtins.printと完全なパスを指定する必要があります。
            app.print_blogs() #app.pyの中のprint_blogs関数を呼び出しています。
            mocked_print.assert_called_with('- Test by Test Author (0 posts)') #print関数が'- Test Blog'という文字列を出力するかどうかを確認しています。


#外部のAPIを呼び出す関数をテストしたいが、実際にはAPIを呼び出したくない場合
def fetch_data():
    response = requests.get('https://api.example.com/data')
    return response.json()

class TestFetchData(TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = fetch_data()

        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('https://api.example.com/data')


#クラスのメソッドをモック化して、そのメソッドが正しく呼び出されるかテストしたい場合
class MyClass:
    def my_method(self):
        return "Real method"
    
def call_my_method(obj):
    return obj.my_method()

class TestMyClass(TestCase):
    @patch.object(MyClass, 'my_method')  # MyClassのmy_methodをモック化
    def test_call_my_method(self, mock_method):
        # モックの戻り値を設定
        mock_method.return_value = "Mocked method"

        # テスト対象の関数を実行
        obj = MyClass()
        result = call_my_method(obj)

        # アサーション
        self.assertEqual(result, "Mocked method")
        mock_method.assert_called_once()


#ファイルを読み込む関数をテストしたいが、実際にはファイルを読み込まずにモックを使いたい場合
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

class TestReadFile(TestCase):
    @patch('builtins.open', mock_open(read_data='file content'))  # open関数をモック化
    def test_read_file(self):
        result = read_file('dummy_path.txt')

        # アサーション
        self.assertEqual(result, 'file content')


#ランダムな値を返す関数をテストしたいが、常に同じ値を返すようにしたい場合
def get_random_number():
    return random.randint(1, 100)

class TestRandomNumber(TestCase):
    @patch('random.randint')  # random.randintをモック化
    def test_get_random_number(self, mock_randint):
        # モックの戻り値を設定
        mock_randint.return_value = 42

        # テスト対象の関数を実行
        result = get_random_number()

        # アサーション
        self.assertEqual(result, 42)
        mock_randint.assert_called_once_with(1, 100)
    

#現在の時刻に依存する関数をテストしたいが、常に同じ時刻を返すようにしたい場合
def get_current_time():
    return datetime.now()

class TestCurrentTime(TestCase):
    @patch('datetime.datetime')  # datetime.datetimeをモック化
    def test_get_current_time(self, mock_datetime):
        # モックの戻り値を設定
        fixed_time = datetime(2023, 10, 1, 12, 0, 0)
        mock_datetime.now.return_value = fixed_time

        # テスト対象の関数を実行
        result = get_current_time()

        # アサーション
        self.assertEqual(result, fixed_time)
        mock_datetime.now.assert_called_once()