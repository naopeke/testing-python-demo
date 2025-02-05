from typing import List

# def list_avg(sequence: List) -> float:
#     return sum(sequence) / len(sequence)

# list_avg(123)

class Book:
    pass
# Bookクラスは現時点では何も属性やメソッドを持っていません。passステートメントは、クラスや関数の本体が空であることを示すために使われます。

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    # __init__メソッドは、クラスのインスタンスが作成されるときに自動的に呼び出される特殊なメソッド（コンストラクタ）です。
    # このメソッドは、booksという引数を受け取り、それをインスタンス変数self.booksに代入します。
    # booksはBookオブジェクトのリスト（List[Book]）であることが型ヒントで示されています。
    
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
    # __str__メソッドは、オブジェクトを文字列として表現するための特殊なメソッドです。
    # このメソッドは、BookShelfオブジェクトがprint()関数などで文字列として表示されるときに呼び出されます。
    # 返される文字列は、本棚に含まれる本の数を示します。例えば、本棚に5冊の本がある場合、"BookShelf with 5 books."という文字列が返されます。

# Bookオブジェクトをいくつか作成
book1 = Book()
book2 = Book()
book3 = Book()

# BookShelfオブジェクトを作成し、Bookオブジェクトのリストを渡す
shelf = BookShelf([book1, book2, book3])

# BookShelfオブジェクトを文字列として表示
print(shelf)  # 出力: "BookShelf with 3 books."