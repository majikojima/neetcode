#include <stdio.h>

int main(){
    int c;
    while(c = getchar() != EOF){
        printf("%d\n", c);
    }
    printf("EOF %d\n", c);
    return 0;
}

/*
このプログラムは、入力から1文字ずつ読み取り、その文字がEOF（End Of File）でない限り、文字のASCII値を出力します。EOFに達したらループを抜け、"EOF"とその値を出力します。

`getchar()` 関数は、標準入力から1文字を読み取り、EOFに達したときにEOFを返します。

コンソール上でEOFを入力する方法は、実行環境によって異なります：

- **Linux/Unix/Mac**：`Ctrl` + `D`を押します。
- **Windows**: `Ctrl` + `Z`を押し、その後にEnterキーを押します。
*/