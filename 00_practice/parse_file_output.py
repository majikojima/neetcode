from typing import Dict

def parse_file_output(output: str) -> Dict[str, str]:
    lines = output.strip().split('\n')
    result_map = {}

    for line in lines:
        # 最後の ': ' で分割する
        idx = line.rfind(': ')
        if idx == -1:
            continue
        
        filename = line[:idx]
        mime_type = line[idx+2:]
        
        result_map[filename] = mime_type

    return result_map

# 使用例
file_output = """file with space: text/plain
anotherfile.jpg: image/jpeg
file_without_space.txt: application/octet-stream"""

print(parse_file_output(file_output))

"""
このコードは、`file` コマンドの結果としての文字列を解析し、ファイル名とそのMIMEタイプをキーと値として持つ辞書を返す関数を定義しています。

大まかな説明:
`parse_file_output`関数は、`file`コマンドの出力形式の文字列を入力として受け取り、その結果を解析して、ファイル名をキーとし、MIMEタイプを値とする辞書を返します。

部分毎の説明:

1. **関数定義とライブラリのインポート**:
    ```python
    from typing import Dict
    def parse_file_output(output: str) -> Dict[str, str]:
    ```
    `typing`モジュールから`Dict`をインポートし、関数`parse_file_output`を定義しています。この関数は、文字列`output`を引数として受け取り、`Dict[str, str]`型の辞書を返します。

2. **出力文字列の前後の空白の削除と行での分割**:
    ```python
    lines = output.strip().split('\n')
    ```
    与えられた`output`文字列から前後の空白を取り除き、各行に分割して`lines`リストに格納します。

3. **結果の辞書の初期化**:
    ```python
    result_map = {}
    ```
    解析結果を保存するための辞書`result_map`を初期化します。

4. **各行の解析**:
    ```python
    for line in lines:
        idx = line.rfind(': ')
        if idx == -1:
            continue
        
        filename = line[:idx]
        mime_type = line[idx+2:]
        
        result_map[filename] = mime_type
    ```
    `lines`リストの各行をループ処理して、ファイル名とMIMEタイプを抽出し、`result_map`に追加します。具体的には、最後の`': '`を基に行を分割しています。

5. **辞書の返却**:
    ```python
    return result_map
    ```
    完成した`result_map`辞書を返します。

6. **使用例**:
以下のコードは、関数の使用例として`file`コマンドのサンプル出力を`file_output`文字列として提供し、関数を呼び出してその結果を表示しています。

```python
file_output = file with space: text/plain
anotherfile.jpg: image/jpeg
file_without_space.txt: application/octet-stream

print(parse_file_output(file_output))
```

実行すると、次のような辞書が出力されます：
```
{'file with space': 'text/plain', 'anotherfile.jpg': 'image/jpeg', 'file_without_space.txt': 'application/octet-stream'}
```
"""