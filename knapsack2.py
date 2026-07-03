import time

# 品物のデータ定義
weights = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
values  = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]
CAPACITY = 45
N = len(weights)

def solve_exhaustive():
    """総当り法（ビット全探索）で最大価格を計算する関数"""
    max_price = 0
    total_patterns = 1 << N  # 2^N 通り
    
    for mask in range(total_patterns):
        current_weight = 0
        current_price = 0
        for i in range(N):
            if (mask & (1 << i)) != 0:
                current_weight += weights[i]
                current_price += values[i]
        
        if current_weight <= CAPACITY:
            if current_price > max_price:
                max_price = current_price
                
    return max_price

def main():
    print("--- 課題2: 動的計画法（DP）による高速化と時間計測 (Python) ---")

    # ==========================================
    # 1. 動的計画法（DP）の実行と時間計測
    # ==========================================
    start_dp = time.perf_counter_ns()
    
    # DPテーブルの初期化 (N+1 行 x CAPACITY+1 列)
    dp = [[0] * (CAPACITY + 1) for _ in range(N + 1)]

    for i in range(N):
        for w in range(CAPACITY + 1):
            if w >= weights[i]:
                # 入れる場合と入れない場合の価値の大きい方を選択
                dp[i + 1][w] = max(dp[i][w], dp[i][w - weights[i]] + values[i])
            else:
                # 容量が足りなくて入れられない場合
                dp[i + 1][w] = dp[i][w]
                
    max_price_dp = dp[N][CAPACITY]

    # 詰め込んだ品物の組み合わせを逆算して特定
    chosen_items = []
    w = CAPACITY
    for i in range(N - 1, -1, -1):
        if dp[i + 1][w] != dp[i][w]:
            chosen_items.insert(0, i + 1)  
            w -= weights[i]

    end_dp = time.perf_counter_ns()
    duration_dp = end_dp - start_dp

    # 結果出力
    print("[動的計画法の結果]")
    print(f"品物の組み合わせ: {chosen_items}")
    print(f"総値段 (最大価格): {max_price_dp}")
    print(f"処理時間: {duration_dp:,} ナノ秒\n")

    start_exhaustive = time.perf_counter_ns()
    
    max_price_exhaustive = solve_exhaustive()
    
    end_exhaustive = time.perf_counter_ns()
    duration_exhaustive = end_exhaustive - start_exhaustive

    print("[総当り法（比較用）の結果]")
    print(f"総値段 (最大価格): {max_price_exhaustive}")
    print(f"処理時間: {duration_exhaustive:,} ナノ秒\n")

    print("--- 処理時間の違いの比較 ---")
    ratio = duration_exhaustive / duration_dp
    print(f"動的計画法は総当り法に対して約 {ratio:.1f} 倍高速です。")

if __name__ == "__main__":
    main()