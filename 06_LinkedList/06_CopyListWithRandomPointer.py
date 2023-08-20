# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def createRandomList(data: list) -> Node:
    if not data:
        return None
    
    # make nodelist
    nodes = [Node(x[0]) for x in data]

    # setting
    for i, item in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if item[1]:
            nodes[i].random = nodes[item[1]]

    return nodes[0]

def copyRandomList(head: Node) -> Node:
    oldToCopy = {None: None}

    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    return oldToCopy[head]

head_data = [[10,None],[11,0],[12,4],[13,2],[14,0]]
head = createRandomList(head_data)
result = copyRandomList(head)
while head:
    print(f"head.val, head.random: {head.val}, {head.random}")
    head = head.next
while result:
    print(f"result.val, result.random: {result.val}, {result.random}")
    result = result.next

"""
この`copyRandomList`関数は、ランダムポインタ付きリンクリストをディープコピーするためのものです。ディープコピーとは、新しいノードが元のリンクリストのノードを参照しないように、全てのノードを新しく作成する方法です。

以下、各部分の説明です：

1. `oldToCopy = {None: None}`:
   - オリジナルのノードとそれに対応するコピーのノードを関連付けるための辞書を初期化します。この辞書を使うことで、オリジナルのリストの各ノードに対して、コピーされたリストの対応するノードを効率的に取得できます。

2. リンクリストを最初から最後までトラバースして、各ノードのコピーを作成します。
   ```python
   cur = head
   while cur:
       copy = Node(cur.val)
       oldToCopy[cur] = copy
       cur = cur.next
   ```

3. もう一度リンクリストを最初から最後までトラバースして、コピーの`next`と`random`ポインタを設定します。
   ```python
   cur = head
   while cur:
       copy = oldToCopy[cur]
       copy.next = oldToCopy[cur.next]
       copy.random = oldToCopy[cur.random]
       cur = cur.next
   ```

4. 最後に、コピーされたリストの先頭ノードを返します。
   ```python
   return oldToCopy[head]
   ```

このアルゴリズムの鍵となるのは、`oldToCopy`という辞書を使ってオリジナルのノードとコピーのノードを関連付けることです。これにより、次のトラバースでオリジナルの`next`と`random`ポインタをコピーに正確に反映させることができます。
"""

"""
了解しました。この部分の詳細な説明を進めていきます。

### oldToCopyとは？

`oldToCopy`は、元のリンクリストのノード(`old`)と新しく作成したコピーのノード(`copy`)を対応付けるための辞書です。キーとしてオリジナルのノードを使用し、値としてそのノードのコピーを保存します。

### なぜoldToCopyが必要か？

ランダムポインタ付きリンクリストのディープコピーを作成する際には、新しいノードを作成するだけでなく、そのノードが参照する`next`と`random`のポインタも正確に設定する必要があります。しかし、リンクリストを1回のトラバースで完全にコピーすることは難しいため、2回のトラバースを行っています。

1. **最初のトラバース**：ここではリンクリストの各ノードのコピーを作成し、`oldToCopy`にオリジナルとコピーの関係を保存します。
   
2. **2回目のトラバース**：ここで、コピーの`next`と`random`ポインタを設定します。オリジナルのノードが持っている`next`や`random`ポインタの先を直接コピーに設定することはできません。なぜなら、それは元のリンクリストのノードを参照してしまうためです。代わりに、`oldToCopy`を使ってオリジナルのノードに対応するコピーのノードを取得し、それを新しいリンクリストのポインタとして設定します。

例:
オリジナルのノード`A`の`random`ポインタがノード`B`を指している場合、コピーのノード`a`の`random`ポインタもノード`b`を指すようにしたいです。`oldToCopy[A]`でノード`a`を、`oldToCopy[B]`でノード`b`を取得できるので、`a.random = oldToCopy[B]`としてノード`b`を指すように設定できます。

このように、`oldToCopy`を利用することで、オリジナルのリンクリストのポインタ構造を正確に新しいリンクリストに反映させることができるのです。
"""

"""
この問題文は、与えられたリンクリストを「深く」コピーすることを要求しています。このリンクリストは普通のリンクリストとは少し異なり、各ノードは次のノードへのポインタ（next pointer）だけでなく、リンクリスト内の任意のノード、またはnullを指すことができる追加のポインタ（random pointer）も持っています。

以下は問題文の主なポイントです：

1. **リンクリストの構造**:
    - 各ノードには値（value）と2つのポインタ（next pointerとrandom pointer）があります。
    - random pointerはリンクリストの任意のノードを指すか、nullを指すことができます。

2. **コピーの要件**:
    - 元のリンクリストのノードに対応する新しいノードを作成する必要があります。
    - 新しいノードの値は元のノードの値と同じでなければなりません。
    - 新しいノードのnext pointerとrandom pointerは、新しくコピーされたリスト内のノードを指す必要があります。新しいリストのポインタが元のリストのノードを指してはいけません。
    
3. **入出力形式**:
    - 各ノードは、ノードの値とrandom pointerが指すノードのインデックス（またはnull）のペアとして表されます。

4. **タスク**:
    - この特定のリンクリストの「深いコピー」を作成し、コピーされたリンクリストの先頭を返す必要があります。

簡単に言うと、この問題は、与えられた特殊なリンクリストの完全なコピーを作成し、そのコピーを返すことを要求しています。このコピーはオリジナルのリストから独立しており、オリジナルのリストのノードを指すポインタを持ってはいけません。
"""

"""
もちろん、分かりやすく説明しますね！

**トラバース**とは、英語で「通る」や「横切る」といった意味があります。コンピュータの世界では、あるデータの集まりの中の各要素を、1つずつ順番に見ていくことを指します。

例えば、リンクリストというものがありますが、これは電車の車両のようなものだと思ってください。各車両には人が乗っており、その人が持っている数字や情報がリンクリストのノード（要素）となります。そして、電車の車両は連結されていますね。この連結部分がリンクリストでの「次のノードを指すポインタ」となります。

**トラバースする**とは、電車の先頭の車両から最後の車両まで、1つずつ各車両を見て回ることを指します。例えば、車両の中にある人が持っている数字を確認したり、何か特定の人を探したりするときに、先頭から順番に各車両を調べることになります。

このように、トラバースはリンクリストの各ノードを順番に見ていく行為を指します。小学生に例えると、「クラスの全員に順番に何かを尋ねる」や「教室の各机の上にある物を1つずつ確認する」などの行為がトラバースに似ています。
"""

"""
この問題に関して`head_data = [[10,None],[11,0],[12,4],[13,2],[14,0]]`のデータでシミュレーションを行います。

まず、元のリンクリストを以下のように想像します。

1. ノードの値が10、ランダムポインタは設定されていません。
2. ノードの値が11、ランダムポインタは1つ目のノード(10)を指しています。
3. ノードの値が12、ランダムポインタは5つ目のノード(14)を指しています。
4. ノードの値が13、ランダムポインタは3つ目のノード(12)を指しています。
5. ノードの値が14、ランダムポインタは1つ目のノード(10)を指しています。

`copyRandomList`関数のシミュレーションを進めます。

### oldToCopyの初期化

```python
oldToCopy = {None: None}
```

ここで、`oldToCopy`辞書を初期化します。

### 最初のトラバース

元のリンクリストのノードを1つずつ走査し、それぞれのノードのコピーを作成して`oldToCopy`辞書に保存します。

```python
cur = head
while cur:
    copy = Node(cur.val)
    oldToCopy[cur] = copy
    cur = cur.next
```

この段階で`oldToCopy`は以下のようになります：

```
{
 Node(10): CopyNode(10),
 Node(11): CopyNode(11),
 Node(12): CopyNode(12),
 Node(13): CopyNode(13),
 Node(14): CopyNode(14),
 None: None
}
```

### 2回目のトラバース

再度、元のリンクリストのノードを1つずつ走査し、`next`ポインタと`random`ポインタを設定します。

```python
cur = head
while cur:
    copy = oldToCopy[cur]
    copy.next = oldToCopy[cur.next]
    copy.random = oldToCopy[cur.random]
    cur = cur.next
```

このトラバースが完了すると、コピーのリンクリストは元のリンクリストの構造を正確に反映したものになります。

### 結果の返却

最後に、コピーされたリンクリストのヘッドを返却します。

```python
return oldToCopy[head]
```

これにより、`head_data = [[10,None],[11,0],[12,4],[13,2],[14,0]]`のデータに基づいたランダムポインタ付きリンクリストのディープコピーが正しく作成されることになります。
"""