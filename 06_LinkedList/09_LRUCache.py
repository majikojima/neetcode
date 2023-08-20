class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            print(self.cache[key].val)
            return self.cache[key].val
        print(-1)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        print(self.cache)

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4

"""
このコードは、Least Recently Used (LRU) キャッシュを実装するものです。キャッシュは、双方向連結リストとハッシュマップ（Python の辞書）を組み合わせて実装されています。

大まかな説明:
- LRUキャッシュは、最も古く使用された項目を削除することで、指定されたキャパシティ内に項目を保持します。
- この実装は、`Node`クラスを使用して双方向連結リストを作成し、`LRUCache`クラス内の操作を管理します。

部分毎の説明:

1. **Node クラス**:
    - `key`と`val`は、キーと値のペアを保存します。
    - `prev`と`next`は、双方向連結リストの前後のノードへのポインタです。

2. **LRUCache クラス**:
    - `__init__`: キャッシュの初期設定を行います。`left`と`right`はダミーノードで、双方向連結リストの先頭と末尾を示しています。
    - `remove`: 指定されたノードをリストから削除します。
    - `insert`: ノードをリストの末尾（`right`の前）に挿入します。これは、ノードが最近使用されたことを示すためです。
    - `get`: 指定されたキーの値を取得します。このキーがキャッシュに存在する場合、対応するノードを最近使用されたものとして更新します。
    - `put`: 新しいキーと値のペアをキャッシュに追加します。キーがすでに存在する場合、そのキーのノードを削除します。キャッシュがキャパシティを超えている場合、最も古く使用されたノード（`left`の次のノード）を削除します。

このコードは、要求されるO(1)の時間複雑度で`get`と`put`の操作を実行する能力を持っています。
"""

"""
LRUキャッシュ（Least Recently Used Cache）は、キャッシュの一種で、最も古く使用されたデータを破棄することで、キャッシュ内のデータを一定の容量内に保持するように動作します。

以下は、LRUキャッシュの基本的な概念を説明します：

1. **キャッシュ**: データや計算結果を一時的に保存しておき、再度そのデータや計算結果が必要になったときに高速にアクセスするための技術や場所を指します。例えば、ウェブブラウザのキャッシュは、一度アクセスしたウェブページの内容を高速に読み込むために利用されます。

2. **LRUの原則**: 「最近最も使われていないものが、次に使われる可能性が低い」という考えに基づいています。したがって、キャッシュが容量いっぱいになった時、最も古くに使用されたデータを破棄して、新しいデータを保存します。

3. **動作**: LRUキャッシュは、データの追加や参照が行われるたびに、データの使用履歴を更新します。キャッシュが上限に達すると、最も古く使用されたデータを削除し、新しいデータを追加します。

実際のアプリケーションでは、LRUキャッシュはデータベースのクエリ結果や計算結果など、再計算や再取得に時間がかかるデータを一時的に保存するために利用されることが多いです。これにより、システムのレスポンス時間の向上や不要な再計算を避けることができます。
"""

"""
LRUキャッシュの動作原理に基づき、`lRUCache.get(1);` が呼ばれた際に、キー1に関連するアイテムが「最近使われた」とマークされます。したがって、この操作の後、キャッシュ内のアイテムの使用履歴は次のようになります：

1. キー1
2. キー2

次に、`lRUCache.put(3, 3);` が呼ばれた時、キャッシュの容量が2であり、すでに2つのアイテム（キー1とキー2）が存在しているため、新しいアイテム（キー3）を追加するためのスペースを確保する必要があります。

この時点で、最も「古く」使用されたアイテムはキー2に関連するアイテムです。なぜなら、前述の通り、`lRUCache.get(1);` が最後に呼ばれたため、キー1に関連するアイテムが最新としてマークされているからです。

したがって、キャッシュからアイテムを削除する必要がある場合、キー2に関連するアイテムが削除され、キー3に関連する新しいアイテムが追加されます。この結果、キャッシュの内容は`{1=1, 3=3}`となります。
"""