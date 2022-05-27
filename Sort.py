def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]
    head_idx = 0
    tail_idx = len(array) - 1
    # ここから記述
    while True:
        # 先頭からpivot以上の数値を探索
        while pivot > array[head_idx]:
            head_idx += 1
        # 末端からpivot未満の数値を探索
        while pivot <= array[tail_idx]:
            # pivotがarrayの最小値ならばpivotのみを切り離して同じ処理（再帰）を繰り返す
            if tail_idx == 0:
                return [array[0]] + sort(array[1:])
            # 先頭と末端からの探索がぶつかったらpivot以上と未満のグループに分ける
            elif head_idx >= tail_idx:
                return sort(array[:tail_idx]) + sort(array[tail_idx:])
            else:
                tail_idx -= 1
        # 数値を交換
        head_num = array[head_idx]
        tail_num = array[tail_idx]
        array[head_idx] = tail_num
        array[tail_idx] = head_num
    # ここまで記述

if __name__ == '__main__':
    main()