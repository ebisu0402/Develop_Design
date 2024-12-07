import sys
from enum import Enum


# 信号機の色を表す列挙型
class Shingou(Enum):
    TOMARE = "とまれ"
    SUSUME = "すすめ"
    CHUI = "ちゅうい"


# colorに対応した信号機の動作を出力する関数
def act_shingou(color: int) -> Shingou:
    if color == 1:
        print(Shingou.TOMARE.value)
        return Shingou.TOMARE
    elif color == 2:
        print(Shingou.SUSUME.value)
        return Shingou.SUSUME
    elif color == 3:
        print(Shingou.CHUI.value)
        return Shingou.CHUI
    else:
        raise ValueError("信号機の色に対応していません")


# コマンドライン引数を取得
if len(sys.argv) != 2:
    print("使用方法: python shingou_action.py <color>")
    sys.exit(1)

try:
    color = int(sys.argv[1])
    act_shingou(color)
except ValueError as e:
    print(f"エラー: {e}")
