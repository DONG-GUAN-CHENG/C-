# C-
The process of learning and side project 
#### ***程式語言簡介***
機器語言->組合語言(組譯器，需利用指令集來規劃程式)->編譯語言(編譯器，速度快)->直譯語言(一行一行翻譯，速度較編譯語言慢)
***
#### ***資料型態與格式化輸出***
* ***變數的宣告與使用***  
int, char, float等資料型態，變數在電腦中是一個佔有記憶體空間的資料存放區，將資料的記憶體位址以變數的觀念取代，若要存取資料，則以該變數  
名稱來指定即可存取資料，可將其看作記憶體中存放未知數值的記憶體空間
變數宣告方式: ``**type var-name**`` 其中``type``為變數資料型態，``VAR-NAME``變數名稱須符合變數命名規則
``;``號為告知編譯器此行程式到此結束，變數一般在程式區塊最上方  
* ***整數型態-int, short,long***  
long型態-使用記憶體空間最大，需要4個位元組(bytes)記憶體空間，1byte=8bit(位元)，每個位元儲存0和1的狀態  
short型態-需要2bytes記憶體空間來儲存  
int型態-較為特殊，在早期16位元系統下(DOS)用2bytes儲存，32或64作業系統下用4bytes記憶體空間來儲存  
電腦儲存整書方式式使用2的補數，二進位位元來表示在某一段範圍內的整數 ex:011->3 101->-3  
* ***浮點數型態***  
浮點數其實就是小數，所需記憶體數量比整數大，單精度float需要4 bytes來儲存，雙精度float需要8 bytes來儲存  
* ***字元型態***  
只需要一個byte的記憶體空間來儲存就好，可以利用char來儲存單一個字元
* ***無值-void**  
內涵虛無或沒有的概念  
ex:int rand(void);->沒有引數但有整數傳回值
* ***常數與前置處理器***  
常數與變數的區別，常數無法進行修改值，變數可以被指定或更改
宣告方式:``const type var-name;``，另外可以使用``#define``開頭的前置處理器  
來變換常數或字串的自訂識別名稱(切記不可加上分號) 語法:``#define 識別子 字串``
* ***printf()格式化輸出函式***  
語法:``printf("control string",argument);``
control string 是控制字串，包含想輸出的文字格式，以及想輸出的變數轉換格式或特殊字元  
argument:引數，變數個數依照control string決定要輸出的變數有幾個  
(變數轉換符號)%d->整數, %f->浮點數,%lf->雙精度浮點數,%c->字元,%S->字串,%%->印出%,\\->印出\,  
\'->印出',\''->印出'',\n->換行,\b->逼一聲,\t->Tab  
ex:printf("%d %f %lf",number1,number2,number3)->將變數number以%d所代表的整數型態印出  
單行註解以「//」,多行註解以「/*開頭」,『結尾 */』來包覆  
* ***scanf()格式化輸入函式***  
語法:``scanf("control string",argument);``
control string 是控制字串，包含想輸出的文字格式，以及想輸出的變數轉換格式或特殊字元，輸入時必須用空格或是enter鍵來區分，用法可以參考變數轉換符號
argument:引數，跟printf()函數較為不同，必須在想要儲存的變數名稱前增加一個``&符號``  
ex:scanf("%d %d", &i, &j); 此敘述會將控制台輸入的兩變數，分別儲存入整數變數i及變數j
***
#### ***運算子、運算式與敘述***  
* ***指定運算子***  
assignment operator符號是等號"=",會把等號右方的值(變數或運算式)，指定給等號左方的變數
ex:int i=0; i=i+1; 
* ***算數運算子***  
『+』,『-』,『*』,『/』,『%』(取餘數)  
int a=10;e=a/4; ans=2 而不是2.5 因為變數a式整數型態所以會得到2  
* ***關係運算子***  
為比較關係的運算，可能為`‵True(真)->非零的值‵`或為``False(偽)->零值``，通常用於程式流程控制  
『> 大於,< 小於,>= 大於等於, <= 小於等於, == 等於(比較), != 不等於』  
 ex: int a=5,b; b=(a==5); ans:b值等於1  
* ***邏輯運算子***  
『&&』式邏輯符號AND, 『||』是邏輯符號OR, 『!』是邏輯符號NOT  
* ***遞增與遞減運算子***  
『++』->遞增運算子, 『--』->遞減運算子 將所運算的變數值進行加1或者是減1  
優點為:在電腦中提供比較低階的運算，執行效率較佳  
ex: a++的意義是，先將變數a的值取出使用，結束後再將變數a值加1,++a的意義是，先將變數a加上1之後取出其數值    
* ***sizeof 運算子***
可用來計算程式內變數所占用的記憶體大小，在``動態配置``記憶體很重要  
語法:``printf("%d",sizeof(int));``  
* ***資料型態的轉換***  
可以進行強制資料型態轉換。將整數型態變數轉換為浮點數型態，在儲存到浮點數變數  
語法:``(type)variable;``  
ex:{  
int a,b;  
float c;  
a=7;  
b=2;  
c=(float)a/b;  
printf("%f",c);  
}  ans:3.50000 假若沒加(float)則會顯示3.0000
* ***三元運算子***  
由兩個符號組成，分別是『？』,『:』  
語法:``條件判斷 ？ 運算式1 : 運算式2 ;``  
當條件成立時，執行運算式1，當條件判斷不成立時，執行運算式2  
int a,b,c; a=b>c？b:c; b>c成立將b值指派給a，反之則將c值指派給a  
* ***逗點運算子***  
將運算式接再一起，用於宣告多個變數時
ex: int i, j, k;  
* ***運算子優先運算順序***  
1. () 2. !,-(算數運算子的負號),++,-- 3.*,/,% 4.+,- 5.<<,>>,>>> 6.>,>=,<,<= 7.==,!= 8.&(位元AND) 9.^(位元XOR) 10.|(位元OR) 11.&&(邏輯AND) 12.||(邏輯OR) 13.？:(條件控制運算，由右至左) 14.=,op=(指定運算子，由右至左)
* ***運算式與敘述***  
所謂的運算式(expression):就是由運算子(operator)或運算元(operand)組合而成，運算子有前面所提的算術、邏輯、指定...等等;而運算元可以是常數、變數或是函數皆可  
statement:指的是完整的指令，用分號來做結尾  
program:是許多有意義的敘述所組成  
***
#### ***流程圖與選擇性敘述***  
algorithm定義為->為解決某一問題或完成特定工作，一系列有次序且明確的指令集合  
包含 輸入、輸出、明確性、有限性、有效性。對於複雜演算法用流程圖更能了解整個流程，方便進行修改、維護及除錯，並且可增加程式的可讀性  
* ***判斷結構if敘述***  
用於判斷是否進入程式區塊，條件式成立，則會進入程式區塊，如果條件不成立，則會進入if敘述之後的其他敘述  
語法:  
```  
if(條件式){  
程式區塊;}  
```  
* ***判斷結構if...else...敘述***  
會根據條件式的真偽，決定要進入的程式區塊為何，成立執行程式區塊1，不成立執行程式區塊2  
語法:  
```  
if(條件式){  
程式區塊1;}  
else {  
程式區塊2;}  
```  
* ***判斷結構if...else if...else...敘述***  
此敘述提供了多種狀況的選擇判斷  
語法:  
```  
if(條件式1){  
程式區塊1;  
}  
else if(條件式2){  
程式區塊2;  
}  
else if(條件式N){  
程式區塊N;  
}  else{  
程式區塊N+1;  
}  
```  
* ***判斷結構之巢狀if***  
當if敘述包含其他if敘述時，稱此種if敘述為巢狀if  
語法:  
```  
if(條件式1){   
if(條件式2){  
程式區塊1;
}  
else {  
程式區塊2;  
}  
else {  
if(條件式3){  
程式區塊3;
}  
else{  
程式區塊4;  
}  
}  
```  
* ***判斷結構之switch敘述***  
為何將多選一的情況簡化，還提供了switch敘述，switch會根據某一個字元或是整數變數，來判斷要進入哪一個程式碼區塊，直到遇到break敘述，再跳出switch的程式區塊;如果沒有值符合，會進入default之後的程式區塊，有時也可以不寫default，直接跳出switch區塊  
語法:  
```  
switch(變數或運算式){  
case 值1:  
程式區塊1;  
break;  
case 值2:  
程式區塊;  
break;  
...  
case 值N:  
程式區塊N;  
break;  
default:  
程式區塊N+1;  
}  
```  
***  
#### ***迴圈***
* ***迴圈結構之for敘述***  
迴圈結構又稱為重複性結構，通常在明確到要執行迴圈的次數時，會使用for迴圈來設計，使用左右大括號來含括敘述，如只有一行程式敘述時，可省略大括號  
語法:  
```  
for(起始式;判斷式;運算式)  
{  
程式區塊;  
}  
```  
起始式:初始化一個或多個變數的值  
判斷式:藉此判斷是否進入程式區塊  
運算式:對變數做一些運算  
ex: for(i=0;i<5;!++)  
printf("%d",i);  

