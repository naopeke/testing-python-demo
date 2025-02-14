import functools
user = {"username": "jose", "access_level": "guest"}
user = {"username": "ana", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func) #デコレータを使用しても、元の関数のメタデータ（名前やドキュメント文字列）が失われないようにします。
        def secure_function(*arg, **kwargs):
            if user["access_level"] == access_level:
                return func(*arg, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator

# 管理者パスワードを取得する関数  @make_secure("admin")デコレータの一種で、関数の動作を変更または拡張するためのPythonの機能
@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

# ダッシュボードパスワードを取得する関数
@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())