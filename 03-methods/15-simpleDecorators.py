def get_admin_password():
    return "1234"

# デコレーターは、別の関数を引数に取って、新しい機能を追加した関数を返すものです。
# make_secure(func) は、func（元々の関数）を引数に取り、その関数に対してアクセス制限を加える新しい関数 (secure_function) を返します。
# secure_function 内で、user["access_level"] が "admin" であれば元の関数（func）を呼び出し、それ以外のユーザー（例えば "guest"）なら "Access Denied" を返します。
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":  # 条件の修正
            return func()
        else:
            return "Access Denied"  # アクセス拒否のメッセージを追加
    return secure_function

user = {"username": "jose", "access_level": "guest"}  # ユーザー情報を先に設定

# 元の関数をラップ: get_admin_password を変更せずに、その動作に追加の機能（セキュリティチェック）を加えることができます。
get_admin_password = make_secure(get_admin_password)  # デコレーターでラップする
print(get_admin_password())  # 結果を表示
