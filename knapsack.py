# 1. データの準備（画像通り）
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
weights = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
values = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]

N = 18               # 品物の数
MAX_CAPACITY = 45    # ナップサックの制限容量

max_value = 0
best_combination = []

# 2. 0 から (2の18乗 - 1) まで普通の for 文で回す
# 2**18 = 262144 通り
for i in range(2**N):
    
    current_weight = 0
    current_value = 0
    current_items = []
    
    # 整数 `i` を 18桁の「0と1の並び（2進数）」に変換する
    # 例: i=5 なら "000000000000000101" になる
    pattern = format(i, f'0{N}b')
    
    # 文字列の「0」か「1」を見て、品物を選ぶか決める
    for idx in range(N):
        if pattern[idx] == '1': # '1' ならその品物を入れる
            current_weight += weights[idx]
            current_value += values[idx]
            current_items.append(items[idx])
            
    # 容量チェック ＆ 最高値の更新
    if current_weight <= MAX_CAPACITY:
        if current_value > max_value:
            max_value = current_value
            best_combination = current_items

# 3. 結果表示
print(f"最大となる総価格: {max_value}")
print(f"選んだ品物の組み合わせ: {best_combination}")