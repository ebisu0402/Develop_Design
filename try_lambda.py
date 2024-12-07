# execute_param_fnの定義
def execute_param_fn(args, hosei, fn):
    # 最大値または最小値に補正値を加えたものを関数に渡して結果を取得
    return fn(
        max(args), hosei
    )  # maxを使用してaの最大値にb（hosei）を加えるラムダ関数を使う


# 1回目のラムダ関数：最大値に補正値を加える
lambda1 = lambda a, b: a + b

# 2回目のラムダ関数：最小値に補正値を引く
lambda2 = lambda a, b: a - b

# 引数と補正値を設定して実行
result1 = execute_param_fn([1, 2, 3], 4, lambda1)  # 最大値3に4を加える
print(result1)  # 出力: 7

result2 = execute_param_fn([1, 2, 3], 4, lambda2)  # 最小値1に4を引く
print(result2)  # 出力: -3


# execute_param_fnの定義
def execute_param_fn(args, hosei, fn):
    # 最大値または最小値に補正値を加えたものを関数に渡して結果を取得
    return fn(
        max(args), hosei
    )  # maxを使用してaの最大値にb（hosei）を加えるラムダ関数を使う


# 1回目のラムダ関数：最大値に補正値を加える
lambda1 = lambda a, b: a + b

# 2回目のラムダ関数：最小値に補正値を引く
lambda2 = lambda a, b: a - b

# 引数と補正値を設定して実行
result1 = execute_param_fn([1, 2, 3], 4, lambda1)  # 最大値3に4を加える
print(result1)  # 出力: 7

result2 = execute_param_fn([1, 2, 3], 4, lambda2)  # 最小値1に4を引く
print(result2)  # 出力: -3
