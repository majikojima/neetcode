#include <stdio.h>

int main(){
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    printf("fahr\tcelsius\n");

    fahr = lower;
    while(fahr <= upper){
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%4.0f\t%6.1f\n", fahr, celsius);
        fahr += step;
    }
    return 0;
}

/*
このCプログラムは、華氏から摂氏への温度変換を行うものです。具体的には、0度から300度までの華氏の温度を20度ずつ増やしながら、それぞれの摂氏の温度を計算し、結果を表示します。

以下は、このプログラムの各部分の説明です。

1. 必要なヘッダーファイルのインクルード
```c
#include <stdio.h>
```

2. `main`関数の定義開始
```c
int main(){
```

3. 必要な変数を定義
```c
    float fahr, celsius;
    int lower, upper, step;
```

4. 温度の下限、上限、およびステップ幅の初期値を設定
```c
    lower = 0;
    upper = 300;
    step = 20;
```

5. タイトルの表示
```c
    printf("fahr\tcelsius\n");
```

6. `fahr`（華氏の温度）を`lower`（ここでは0度）から`upper`（ここでは300度）まで増加させながらループを行います。
```c
    fahr = lower;
    while(fahr <= upper){
```

7. 各華氏の温度に対する摂氏の温度を計算
```c
        celsius = (5.0 / 9.0) * (fahr - 32.0);
```

8. 計算結果を表示
```c
        printf("%4.0f\t%6.1f\n", fahr, celsius);
```

9. 華氏の温度をステップ幅だけ増加
```c
        fahr += step;
    }
```

10. プログラム終了時に0を返す
```c
    return 0;
}
```

このプログラムを実行すると、華氏の温度とそれに対応する摂氏の温度が20度ずつ増加しながら表示されます。
*/