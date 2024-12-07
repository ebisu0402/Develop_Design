# ジェネレータを使用して数値を生成する関数
def try_generator(n):
    # ジェネレータ式を使って 1 から n までの平方数を生成
    return (i * i for i in range(1, n + 1))


# メイン関数
if __name__ == "__main__":
    # try_generator 関数をジェネレータ式で呼び出す
    gen = try_generator(5)

    # ジェネレータから値を取り出して表示
    for value in gen:
        print(value)
