from typing import List
import collections

def findItinerary(tickets: List[List[str]]) -> List[str]:
    adj = {u: collections.deque() for u, v in tickets}
    res = ["JFK"]

    tickets.sort()
    for u, v in tickets:
        adj[u].append(v)

    def dfs(cur):
        if len(res) == len(tickets) + 1:
            return True
        if cur not in adj:
            return False

        temp = list(adj[cur])
        for v in temp:
            adj[cur].popleft()
            res.append(v)
            if dfs(v):
                return res
            res.pop()
            adj[cur].append(v)
        return False

    dfs("JFK")
    return res

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))

"""
このコードは、与えられた飛行機のチケットから、すべてのチケットを使ってJFKから開始する行程を再構築する問題のためのものです。この再構築された行程は辞書順で最も小さいものでなければなりません。

**大まかな説明**:
コードはまず隣接リスト`adj`を作成し、各出発地からの目的地のリストを持ちます。次に、深さ優先探索 (DFS) を使用して、JFKからの行程を再構築します。

**部分毎の説明**:

1. `adj = {u: collections.deque() for u, v in tickets}`:
    - すべての出発空港をキーとして持つ隣接リストを作成します。

2. `res = ["JFK"]`:
    - 行程を格納するリスト。最初の空港は常にJFKです。

3. `tickets.sort()`:
    - チケットを辞書順でソートします。これにより、行程が辞書順で最小となるように再構築できます。

4. `for u, v in tickets:`:
    - 各チケットの情報に対してループを回します。

5. `adj[u].append(v)`:
    - 出発地`u`の隣接リストに目的地`v`を追加します。

6. `def dfs(cur):`:
    - 深さ優先探索の関数定義です。この関数は、与えられた出発地`cur`から再構築できる行程を探します。

7. `if len(res) == len(tickets) + 1:`:
    - すべてのチケットが使われ、行程が完成した場合、Trueを返します。

8. `if cur not in adj:`:
    - 現在の空港が出発地として存在しない場合、Falseを返します。

9. `for v in temp:`:
    - 現在の空港`cur`からのすべての可能な目的地`v`に対してループを回します。

10. `adj[cur].popleft()`:
    - 現在の出発地からの最初の目的地を取り除きます。

11. `res.append(v)`:
    - 行程に目的地を追加します。

12. `if dfs(v):`:
    - その目的地からの行程が完了した場合、現在の行程を返します。

13. `res.pop()`:
    - 行程から最後の空港を取り除きます。

14. `adj[cur].append(v)`:
    - 前に取り除いた目的地を再び隣接リストに追加します。

15. `dfs("JFK")`:
    - JFKからの行程の再構築を開始します。

16. `return res`:
    - 再構築された行程を返します。
"""