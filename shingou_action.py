from enum import Enum


class Shingou(Enum):
    TOMARE = 1  # とまれ
    SUSUME = 2  # すすめ
    CHUI = 3  # ちゅうい


def act_shingou(color: int) -> Shingou:
    if color == 1:
        print("とまれ")
        return Shingou.TOMARE
    elif color == 2:
        print("すすめ")
        return Shingou.SUSUME
    elif color == 3:
        print("ちゅうい")
        return Shingou.CHUI
    else:
        raise ValueError("信号機の色に対応していません")


def main():
    try:
        color = int(input("信号の番号を入力してください"))
        shingou = act_shingou(color)  # 入力に基づいた信号の動作を表示
        print(f"選ばれた信号: {shingou.name}, 値: {shingou.value}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
