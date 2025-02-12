def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":  # 条件の修正
            return func()
        else:
            return "Access Denied"  # アクセス拒否のメッセージを追加
    return secure_function

user = {"username": "jose", "access_level": "guest"}  # ユーザー情報を先に設定

get_admin_password = make_secure(get_admin_password)  # ラップする
print(get_admin_password())  # 結果を表示
