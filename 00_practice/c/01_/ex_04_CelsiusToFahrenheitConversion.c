#include <stdio.h>

int main(){
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    printf("cel\tfahr\n");

    celsius = lower;
    while(celsius <= upper){
        fahr = celsius * (9.0 / 5.0) + 32.0;
        printf("%3.0f\t%6.1f\n", celsius, fahr);
        celsius += step;
    }
    return 0;
}

/*
もちろん、以下にそのプログラムの概要と部分ごとの詳細な説明を提供します。

### 大まかな説明
このプログラムは、定義された範囲内の摂氏温度（下限0度から上限300度まで、ステップ20度ごと）を華氏温度に変換し、その結果をターミナルに表示するCプログラムです。

### 部分毎の説明
1. **前提条件と変数の初期化**:
```c
#include <stdio.h>

int main(){
    float fahr, celsius;
    int lower, upper, step;
```
`stdio.h`ヘッダーを含めることで、標準入出力関数を使用できるようにしています。次に、温度を格納するための浮動小数点変数`fahr`と`celsius`を、範囲とステップを格納する整数変数`lower`、`upper`、`step`を宣言しています。

2. **範囲とステップの設定**:
```c
    lower = 0;
    upper = 300;
    step = 20;
```
摂氏の下限、上限、および増分ステップを定義しています。

3. **ヘッダーの出力**:
```c
    printf("celsius\tfahr\n");
```
これは、出力結果のヘッダー行を表示するためのもので、摂氏と華氏の各列を示しています。

4. **温度変換と結果の出力**:
```c
    celsius = lower;
    while(celsius <= upper){
        fahr = celsius * (9.0 / 5.0) + 32.0;
        printf("%4.0f\t%6.1f\n", celsius, fahr);
        celsius += step;
    }
```
`while`ループを使用して、各摂氏温度を華氏に変換し、その結果を表示しています。摂氏温度はステップごとに増加し、上限に達するまでこのプロセスが続きます。

5. **プログラムの終了**:
```c
    return 0;
}
```
main関数の最後に0を返して、プログラムが正常に終了したことを示しています。
*/