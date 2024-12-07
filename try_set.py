import random
import datetime

# 100万個のランダムな整数のリストを作成（0～1億の範囲）
a = [random.randint(0, 100000000) for _ in range(1000000)]

# 100個のランダムな整数のリストを作成（0～1億の範囲）
checked_list = [random.randint(0, 100000000) for _ in range(100)]

# 1. リストでの存在チェックの時間計測
start_time = datetime.datetime.now()

# checked_listの要素がaのリスト内に存在するかを確認
for temp in checked_list:
    if temp in a:
        print(f'temp:{temp} in a')

end_time = datetime.datetime.now()
print(f'リストでのチェックにかかった時間: {end_time - start_time}')

# 2. セットでの存在チェックの時間計測
# リストaをセットに変換
a_set = set(a)

start_time = datetime.datetime.now()

# checked_listの要素がa_setのセット内に存在するかを確認
for temp in checked_list:
    if temp in a_set:
        print(f'temp:{temp} in a_set')

end_time = datetime.datetime.now()
print(f'セットでのチェックにかかった時間: {end_time - start_time}')
