from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    total_gas = 0
    remaining_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        remaining_gas += gas[i] - cost[i]

        if remaining_gas < 0:
            remaining_gas = 0
            start_index = i + 1

    if total_gas >= 0:
        return start_index
    else:
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost))

"""
このコードは、ガソリンスタンドの問題を解決するためのものです。一連のガソリンスタンドが与えられ、各スタンドで得られるガソリンの量と次のスタンドまで移動するのに必要なガソリンの量が与えられます。あるスタンドから出発して、全てのスタンドを訪問して元のスタンドに戻ることができるかどうか、そしてどのスタンドから出発すればよいかを判断する問題です。

**大まかな説明**:
- コードは、ガソリンスタンドのリング上を一周できるかどうかを判断し、もし一周できる場合は、どのスタンドからスタートすればよいかを返します。
- もし全体のガソリンの供給量が全体のコストよりも少ない場合、サーキットを完成することはできないので、-1を返します。

**部分毎の説明**:
1. `total_gas = 0` : サーキット全体を通過するためのガソリンの総量を追跡します。
2. `remaining_gas = 0` : 現在のスタート地点からの残りのガソリンの量を追跡します。
3. `start_index = 0` : サーキットを完了できる可能性のある開始スタンドのインデックス。
4. `for i in range(len(gas)):` : 各ガソリンスタンドを順に調べます。
   - `total_gas += gas[i] - cost[i]`: 全体のガソリンとコストの差を計算します。
   - `remaining_gas += gas[i] - cost[i]`: 現在のスタート地点からのガソリンとコストの差を計算します。
   - `if remaining_gas < 0:`: もし残りのガソリンが足りない場合、現在のスタンドは開始スタンドとしては適していないので、次のスタンドを開始スタンドとします。
5. `if total_gas >= 0:` : ガソリンの総供給が総コスト以上であれば、サーキットを完了できるスタート地点が存在するので、そのインデックスを返します。そうでない場合は、-1を返します。

このアルゴリズムは、車がガソリンスタンドのリング上を一周できるかどうかを効率的に判断するためのものです。
"""