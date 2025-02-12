import functools

user = {"username": "jose", "access_level": "guest"}  # ユーザー情報を先に設定

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"  # アクセス拒否のメッセージを追加
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

get_admin_password = make_secure(get_admin_password)  # デコレーターでラップする
print(get_admin_password.__name__)  # 結果を表示
