import sys
from enum import Enum
import random


# 1. 信号機の色を表す列挙型
class TrafficSignal(Enum):
    RED = "とまれ"
    GREEN = "すすめ"
    YELLOW = "ちゅうい"


# 2. 信号機の動作をラムダ式で定義
signal_action = {
    TrafficSignal.RED: lambda: print("信号: とまれ"),
    TrafficSignal.GREEN: lambda: print("信号: すすめ"),
    TrafficSignal.YELLOW: lambda: print("信号: ちゅうい"),
}


# 3. ジェネレータを使って信号機の動作を順次取得
def signal_generator(color_list):
    for color in color_list:
        yield signal_action.get(color, lambda: print("不正な信号色"))


# 4. セットを使って色のチェック
valid_colors = {TrafficSignal.RED, TrafficSignal.GREEN, TrafficSignal.YELLOW}


def check_signal_color(color):
    if color in valid_colors:
        return True
    return False


# メイン処理
def main():
    # コマンドライン引数から色のインデックスを取得
    if len(sys.argv) < 2:
        print("色を指定してください（例: python exercise.py 1 2 3）")
        sys.exit(1)

    # コマンドライン引数を色のインデックスに変換
    color_indices = [int(arg) for arg in sys.argv[1:]]
    color_list = []

    # インデックスに基づいて信号の色を選択
    for idx in color_indices:
        if idx == 1:
            color_list.append(TrafficSignal.RED)
        elif idx == 2:
            color_list.append(TrafficSignal.GREEN)
        elif idx == 3:
            color_list.append(TrafficSignal.YELLOW)
        else:
            print(f"不正な色のインデックス: {idx}")
            sys.exit(1)

    # 信号の動作をジェネレータで処理
    gen = signal_generator(color_list)
    for action in gen:
        action()

    # セットでの色の検証
    random_color = random.choice(list(valid_colors))
    if check_signal_color(random_color):
        print(f"ランダムに選ばれた色 {random_color.name} は有効な信号色です。")
    else:
        print(f"ランダムに選ばれた色 {random_color.name} は無効な信号色です。")


if __name__ == "__main__":
    main()
