class Post:
# Post クラスのインスタンスを作成する際に呼び出されます。このメソッドは、title（タイトル）と content（コンテンツ）という2つの引数を受け取り、それぞれをインスタンス変数として設定します。
# self.title = title と self.content = content によって、Post インスタンスが持つタイトルとコンテンツが保存されます。
    def __init__(self, title, content):
        self.title = title
        self.content = content

# 現在、実装されていません。通常、__repr__ はインスタンスを文字列として表現する方法を定義するもので、主にデバッグや表示時に使用されます。
# 実装されていないため、Post オブジェクトを出力してもデフォルトのオブジェクト表現が使われます。
    def __repr__(self):
        pass

# Post オブジェクトを辞書形式で返します。返される辞書には、タイトル（title）とコンテンツ（content）がキーと値として含まれます。
# このメソッドは、Post オブジェクトをJSONとして表現したい場合に役立ちます。例えば、WebアプリケーションのAPIレスポンスに使用されることが多いです。
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }