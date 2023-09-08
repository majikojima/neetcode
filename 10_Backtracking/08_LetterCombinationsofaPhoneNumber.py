from typing import List

def letterCombinations(digits: str) -> List[str]:
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res

digits = "23"
print(letterCombinations(digits))

digits = ""
print(letterCombinations(digits))

"""
コードの大まかな説明:
このコードは、電話の数字キーとそれに対応する文字を使って、与えられた数字文字列から作成可能なすべての文字列の組み合わせを生成します。

部分毎の説明:

1. `class Solution:`  
   - 解法を表すクラスを定義します。
   
2. `def letterCombinations(self, digits: str) -> List[str]:`  
   - `digits`という数字文字列を入力として受け取り、可能な文字列の組み合わせのリストを返すメソッドを定義します。
   
3. `res = []`  
   - 結果を保存するための空のリストを初期化します。

4. `digitToChar = {...}`  
   - 電話の数字キーとそれに対応する文字のマッピングを定義します。ただし、`"7": "qprs"`はタイプミスかもしれません。正しくは`"7": "pqrs"`のはずです。
   
5. `def backtrack(i, curStr):`  
   - 再帰的なバックトラック関数を定義します。`i`は現在処理している`digits`のインデックス、`curStr`は現在の組み合わせ文字列を表します。
   
6. `if len(curStr) == len(digits):`  
   - 現在の組み合わせ文字列が`digits`の長さと同じ場合、完全な組み合わせが作成されたとみなして、結果リストに追加します。
   
7. `for c in digitToChar[digits[i]]:`  
   - 現在の数字キーに対応する各文字について繰り返します。
   
8. `backtrack(i + 1, curStr + c)`  
   - 次の数字に進むための再帰呼び出しを行います。現在の組み合わせ文字列に新しい文字を追加します。
   
9. `if digits:`  
   - `digits`が空でない場合、バックトラック関数を呼び出して処理を開始します。

10. `return res`  
   - 最終的な結果リストを返します。
"""

"""
`digits = "23"` の場合のシミュレーションを実行します。

1. まず、`res`（結果のリスト）を空で初期化します。
2. `digitToChar` というマッピングを利用して、各数字がどの文字にマッピングされるかを定義します。
3. 入力 `digits` が空でないか確認します。この場合、`digits = "23"` なので空ではありません。
4. `backtrack(0, "")` を呼び出して、バックトラックの処理を開始します。ここで、`i=0` と `curStr=""` です。

- 初めての `backtrack` 呼び出し:

  1. `i = 0`、`curStr = ""`
  2. `digitToChar[digits[0]]` は `"abc"` です。この文字列をループします。
  3. `c = "a"` の場合:

     - `backtrack(1, "a")` を呼び出します。
       
       - 2回目の `backtrack` 呼び出し:

         1. `i = 1`、`curStr = "a"`
         2. `digitToChar[digits[1]]` は `"def"` です。この文字列をループします。
         3. `c = "d"` の場合:

            - `backtrack(2, "ad")` を呼び出します。
              
              - この時点で、`len(curStr) == len(digits)` なので、`res` に `"ad"` を追加します。

         4. `c = "e"` の場合:

            - `backtrack(2, "ae")` を呼び出します。
              
              - 同様に、`res` に `"ae"` を追加します。

         5. `c = "f"` の場合:

            - `backtrack(2, "af")` を呼び出します。
              
              - 同様に、`res` に `"af"` を追加します。

  4. `c = "b"` の場合:

     - `backtrack(1, "b")` を呼び出します。
       
       - ここでも `"bd"`, `"be"`, `"bf"` の3つの文字列が `res` に追加されます。

  5. `c = "c"` の場合:

     - `backtrack(1, "c")` を呼び出します。
       
       - ここでも `"cd"`, `"ce"`, `"cf"` の3つの文字列が `res` に追加されます。

5. すべての可能な組み合わせが `res` に追加されたので、`res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]` となります。

6. 最後に、`res` が返されます。
"""