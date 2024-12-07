# クロージャを返す関数
def test_closure(initial_value):
    data = initial_value

    # add_data 関数: dataに値を加える
    def add_data(value):
        nonlocal data  # クロージャで外部の変数を変更するために nonlocal を使う
        data += value

    # get_data 関数: dataの現在の値を返す
    def get_data():
        return data

    # add_data と get_data を返す
    return add_data, get_data


# 関数 execute_param_fn の定義
def execute_param_fn(args, hosei, fn):
    return fn(max(args), hosei)


if __name__ == "__main__":
    # クロージャの動作確認
    add_data, get_data = test_closure(3)

    # 値を追加
    add_data(2)  # data = 3 + 2 = 5
    add_data(3)  # data = 5 + 3 = 8
    add_data(4)  # data = 8 + 4 = 12

    # 現在の値を取得
    data = get_data()
    print(f"現在のデータ: {data}")  # 出力: 現在のデータ: 12

    # execute_param_fn の動作確認
    lambda1 = lambda a, b: a + b  # 最大値に補正値を加えるラムダ関数
    result1 = execute_param_fn([1, 2, 3], 4, lambda1)
    print(f"ラムダ関数1の結果: {result1}")  # 出力: ラムダ関数1の結果: 7

    lambda2 = lambda a, b: a - b  # 最小値から補正値を引くラムダ関数
    result2 = execute_param_fn([1, 2, 3], 4, lambda2)
    print(f"ラムダ関数2の結果: {result2}")  # 出力: ラムダ関数2の結果: -3
