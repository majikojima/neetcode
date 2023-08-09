from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(f"stones: {stones}, len(s): {len(stones)}")

            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            print(f"first: {first}, second: {second}, push: {first - second}")

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
    
s = Solution()
stones = [2,7,4,1,8,1]
result = s.lastStoneWeight(stones)
print(result)

# stones = [1]
# result = s.lastStoneWeight(stones)
# print(result)

"""
もちろんです。このコードは、与えられた配列（石の重さのリスト）の中から2つの最大の石を取り出し、その差を再びリストに戻すというプロセスを、リストの要素が1つになるまで続けるものです。

以下に、コードの詳細な説明を行います。

1. `def lastStoneWeight(self, stones: List[int]) -> int:`: この行は、関数`lastStoneWeight`を定義しています。この関数は、整数のリスト（石）を受け取り、最後に残る石の重さを返します。

2. `print(stones)`: この行は、関数に渡される元の石のリストを表示します。

3. `stones = [-s for s in stones]`: ここではリスト内包表記を使って、配列`stones`のすべての要素の符号を反転させています。これにより、Pythonのheapqモジュール（最小ヒープのみをサポート）を使用して最大ヒープを実装しています。

4. `heapq.heapify(stones)`: この行は、リスト`stones`をヒープに変換します。

6. `while len(stones) > 1:`: この行は、`stones`リストの要素が1つになるまでループを続けることを指示します。

7. `first = heapq.heappop(stones)`: ここではヒープから最大の要素（最小ヒープでは最小の要素、しかし我々は符号を反転させているので実際には最大の要素）を取り出し、それを`first`に格納しています。

8. `second = heapq.heappop(stones)`: 同様に、次に最大の要素を取り出し、それを`second`に格納しています。

9. `if second > first: heapq.heappush(stones, first - second)`: これは、2つの石（`first`と`second`）が同じ重さでない場合、その差をヒープに追加することを指示しています。

10. `stones.append(0)`: この行は、`stones`リストが空になった場合（すべての石が完全に破壊された場合）に備えて、0をリストに追加しています。

11. `return abs(stones[0])`: 最後に、`stones`リストの先頭要素（これが最後に残った石の重さ、またはすべての石が破壊された場合は0）の絶対値を返します。これは、最後の石の重さがマイナスになることを防ぐためです。
"""