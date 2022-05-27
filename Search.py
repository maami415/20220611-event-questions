def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 探索範囲に関して先頭と末端のインデックスの初期値を設定
    start_idx = 0
    end_idx = len(sorted_array) - 1
    # 探索範囲の要素数が1でない限り探索を続ける
    while end_idx - start_idx > 0:
        # 探索範囲における中間のインデックス（mid_idx）とその値（mid_num）を取得
        temp = end_idx + start_idx
        mid_idx = int(temp / 2) if temp % 2 == 0 else int((temp - 1) / 2)
        mid_num = sorted_array[mid_idx]
        # 中間の値が探索対象の値と一致していたら、そのインデックスを返す
        if mid_num == target_number:
            return mid_idx
        # 中間の値が探索対象の値より小さかったら、それより後ろの要素を探索
        elif mid_num < target_number:
            start_idx = mid_idx + 1
        # 中間の値が探索対象の値より大きかったら、それより前の要素を探索
        else:
            end_idx = mid_idx
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()