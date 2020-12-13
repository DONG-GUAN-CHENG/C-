# C-
The process of learning and side project 
#### ***程式語言簡介***
機器語言->組合語言(組譯器，需利用指令集來規劃程式)->編譯語言(編譯器，速度快)->直譯語言(一行一行翻譯，速度較編譯語言慢)
***
#### ***資料型態與格式化輸出***
* ***變數的宣告與使用***  
int, char, float等資料型態，變數在電腦中是一個佔有記憶體空間的資料存放區，將資料的記憶體位址以變數的觀念取代，若要存取資料，則以該變數 
名稱來指定即可存取資料，可將其看作記憶體中存放未知數值的記憶體空間，也可用於宣告自定義函數
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
來變換常數或字串的自訂識別名稱(切記不可加上分號) 語法:``#define 識別子 常數(字串)``
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
ps:起始式、判斷式、運算式都可以為空白，但是中間分號仍然要寫出來，否則會造成語法錯誤  
* ***迴圈結構之while敘述***  
結構與for迴圈相似，但是沒有起始式與運算式的區塊，而是把起始式和運算式所需要的計算，放到while迴圈的前面或迴圈內  
語法:  
```  
while(判斷式){  
程式區塊;  
}  
```  
ex:  
i=0; //起始式  
while(i<5){  //判斷式  
printf("%d",i);  
i++;  //運算式  
}  
* ***迴圈結構之do...while敘述***  
do...while為while迴圈的變形，差別在於迴圈內的敘述會先執行一次，執行一次後再根據判斷式的真偽，決定是否再進入迴圈之中  
語法:  
```  
do{  
程式區塊;  
} while(判斷式);  
```
* ***Continue敘述***  
一般迴圈的執行流程都是在程式區塊執行完畢後，才繼續下一輪。某些特殊情況，需略過接下來的程式碼，然後直接跳到下一輪的起始位置
此時就可用cintinue敘述，通常搭配判斷結構，如if敘述  
語法:  
```  
for(i=0;i<=10;i++){  
> if(i%2)  
>> continue;  
> total=total+i;  
}  
```
* ***break敘述***  
break敘述雨continue敘述剛好相反，程式遇到break時，將會直接跳出迴圈，不在執行迴圈內的敘述  
語法:  
```  
for(i=10;i<100;i++){  
if(!(i%7)) 
break;  
printf("%d",i);  
}
```
***  
#### ***函式***  
* ***函式的架構***  
函式為``結構化設計``一個重要元素，可將複雜的程式分解為較小、較簡單的問題，使程式可讀性增加、偵錯及修改也較為容易  
函式結構包含了:  
* 函式雛形(prototype)  
* 函式本身(敘述)  
* 函式引數(arguments)  
語法:  
```  
型態 函式名稱(引數1,引數2,....)  
{  
程式區塊;  
}  
```  
ps:型態:函式傳回的資料型態，任何一個介紹過的資料型態，也可為各種型態的指標  
   函式名稱:可自訂，不可與變數名稱重複或為保留字  
   引數:欲傳遞進函式的引數  
   
宣告函式的語法:  
```  
型態 函式名稱(引數1 型態,引數2 型態,...);  
```
與函式語法架構類似，但不需要敘述的部分，引數部分可省略引數名稱，只寫引數型態即可，prototype的宣告在結尾要加分號，像printf()和scanf()這類的基本函數雛形宣告，都已經包含在#include<stdio.h>標準輸出與輸入的標頭檔內，故可直接使用  
* ***引數的傳遞***  
每個函數是獨立的，因此當需要外部的資料時，或是在函式內修改到外部資料時，就必須將資料以引數的方法傳遞函式，引數又稱做『傳入值』，傳回值型態就是f(x)答案的型態，可能是整數、小數、字元、運算式...等等。  
C語言本身就是由許多函數所構成，一開始由main()函式出發，有呼叫另一個函式，則跳入該函式，執行完之後，再回到主函式main()繼續執行。   
函式可以有傳入值，也可以有回傳值，利用return敘述可以將變數傳回呼叫它的函式內，一但執行到return敘述，程式將直接結束此函數的執行，將後方的值傳回原先呼叫的函式。  
* ***區域與全域變數***  
區域變數->每個變數都有生命週期(scope)，當一個變數被宣告時，也決定了這個變數該存在的範圍，變數宣告要在程式最上方，只存在於該程式區塊中，離開該程式區塊(大括號)，該變數就會被銷毀，故在不同區塊內的變數名稱是可重複的。
全域變數->在程式一開始即宣告，宣告於所有函式之外，其作用範圍是整個程式。  
* ***變數儲存類別***  
(1) extern修飾字:  
用於告訴編譯器，此變數已在其他地方宣告了，不在配置記憶體給該變數  
語法`` extern type var-name;``  
ps:前置處理器是在編譯器編譯程式前進行作用，#include的作用就是將相關的檔案含括進來使用  
第一種->#include <filename> 使用角括號會在系統設定的含括檔目錄中去尋找  
第二種->#include "filename" 使用雙引號會在目前檔案的工作目錄去尋找檔案，還可以指定路徑去尋找檔案，例如 #include"d:/bill.h"   
(2) register修飾字:  
register是CPU上的memory，CPU要存取register的資料遠比存取memory裡的資料要快。因此C語言提供了register修飾字，讓變數可以持續留在CPU的register內，藉此增加運算的速度，通常迴圈次數頻繁，控制迴圈次數的變數就可用register來宣告，可節省時間  
(3) static修飾字  
可以使變數只初始化一次  
 ex:  
``` 
int main(void)  
{  
int i;  
for(i=1;i<5;i++)  
printf("x=%d\n",f());  
system("pause");  
}  
int f(void)  
{  
 static int x=0;  
 return x++;  
}
```  
因為變數x使用了static修飾，只會被初始化一次，不會再下次進入時一再被指定為0                
(4) const修飾字  
被const修飾的變數不能被更改

* ***遞迴函式***  
一個函式直接或間接(在敘述內呼叫其他函式，在該函式內又呼叫了原先的函式)的呼叫函式本身，稱為recursive function  
ex:計算n階乘(n!)，可利用n!=n*(n-1)!來計算  
缺點:遞迴函式，容易做重複的計算，每一次呼叫函式都會再去佔用一些記憶體，故效率不佳  
                  
* ***main函式的引數***  
main()函式的引數，定義為外部傳給main()函式的引數，在執行列command prompt，類似win系統下的cmd或unix系統的shell，可以在程式後加上引數，當成是需要接受這些引數時，就可以用main()函式的引數來輸入  
ps:在C語言中，已經定義main()函式的第一個引數為執行程式本身  
***  
#### ***陣列 array***  
* ***一維陣列的使用***  
陣列為最基本的資料結構之一，宣告一個陣列等同於宣告``多個相同型態``的變數，在記憶體中是連續的。假設當一個具有3個元素的整數陣列被宣告時，程式會要求一個``連續的``記憶體位址  
宣告一維陣列語法:  
```  
型態 陣列名稱[元素個數];  ->int array[10]
```  
C語言中，陣列的第一個元素之索引值(index)為0，第二個為1，依此類推。一維陣列表示方法->array[0]、array[1]、array[2]...，而每一個陣列元素都代表4 bytes的整數變數  
ps:宣告陣列時，元素個數必須為常數，因為編譯器需要知道要配置多少記憶體來存放陣列  
ex:int array[n]->是不行的因為n為變數, int array[5]->可以為常數  
```  
自行輸出與輸入陣列元素的值
int num[5];
scanf("%d",&num[0]); //陣列輸入方式  
printf("%d",num[0]); //陣列輸出方式  
```  
ps:宣告陣列時其元素個數必須為常數，但使用時的索引值可為變數，甚至可為一個運算式  
```  
int i,a[10]  
for(i=0;i<10;i++)  
a[i]=i;  
```  
上述索引值從0開始，a[10]不是合理的使用範圍，也就是說一個具有n個元素陣列被宣告時，索引值的範圍為0~n-1  
設定陣列元素除了一個個指定之外，下列為其它陣列元素設定方式:  
```
int a[5]={0}; //陣列的值皆為0  
int b[3]={10,20,30}; //宣告時使用大括號設定初值  
int c[]={5,2,6,9,7}; //陣列元素個數依初值設定個數而定  
```  
* ***用陣列來表示字串***  
因c語言中並沒有字串型態，如需使用字串，通常會運用陣列與索引值來表示。在C語言中，以``字元'\0'``判斷一個字串是否結束了，因此如果一個字串由n個字元組成，儲存這個字串的陣列大小為n+1個字元  
ex:  
```  
char name[6];  
name[0]='j';  
name[1]='a';  
name[2]='\0';  //指定'\0'給陣列元素  
name[3]='s';
name[4]='0';  
name[5]='n';  
程式只會輸出『ja』，因為遇到了\0，被認定此字串到此結束  
```  
* ***二維和多維陣列***  
宣告二維以上陣列的語法:  
```  
型態 陣列名稱[元素個數(1維)][元素個數(2維)]...[元素個數(n維)];  -> ex: int a[5][5];
```  
元素的資料型態為整數型態，從a[0][0],a[0][1]...a[0][4]....a[4][4]。  
* ***將陣列傳遞進函式***  
陣列也可當作引數，傳遞進函式時，不會將陣列複製一份，而是將陣列第一個元素的記憶體位址傳遞進函式，所以在函式內修改陣列的值是有效的
***
#### ***指標***  
* ***指標的定義***  
指標(pointer)是C語言當中一項非常重要的資料結構，可用來製作堆疊、佇列...等資料結構，並擁有自己的運算子。透果指標存取變數時，因各種變數儲存方式不同，編譯器需要了解的是如何解釋這一塊記憶體，因此宣告變數時，需告知變數為``指標型態``或``指標變數``所指向的記憶體型態。  
宣告指標的語法:  
```  
型態 *變數名稱;  

(型態:指標指向記憶體位址所儲存變數之資料型態  
*變數名稱:表示這是一個指標型態的變數)    
```
指向整數型態變數的指標->整數指標  
指向浮點數變數的指標->浮點數指標  
最基本的運算子有兩個(有順序，需先取得記憶體位址才能取得記憶體位址的值):  
『 & 』->取得變數的``記憶體位址``，後方運算元為一個``變數``  
『 * 』->取得記憶體位址中的``值``，後方運算元為一個``記憶體位址``  
使用指標時有幾點需要注意 ps:  
(1) 指標需指向正確的型態  
ex:  
```  
double *ptr;  
int a;  
ptr=&a;  
*ptr=5;  
```  
當指向double型態的指標時，會修改 8 bytes的記憶體。但變數a實際只佔了4個bytes，另外4 bytes可能正在被程式使用，會造成錯誤的發生。  
(2) 不可用&運算子對常數或運算式取指標值  
ex:  
```  
int *ptr;  
ptr=&3;  //不可用&運算子對常數取指標值
ptr=&(a+b); //不可用&運算子對運算式取指標值  
```  
(3) 不可在指標並未指向任何記憶體時使用``*``運算子  
ex:  
```
int * ptr;  
*ptr=1;  
```  
* ***指標的運算***  
不像一般變數的四則運算，對於指標只有「+」、「-」、「++」、「--」  
使用加法的意義為：將指標往後移動n個該型態的記憶體  
ex:  
```
int * ptr,a;  
ptr=&a;  
ptr++;
```  
執行後，指標ptr將指向變數a記憶體位址後方的4個bytes的記憶體位址  
  
使用減法的意義為:將指標往前移動n個該型態的記憶體  
ex:  
```
int * ptr,a;  
ptr=&a;  
ptr=ptr-20;  
```
執行後，指標ptr將指向變數a記憶體位址前方的「20 * 4 bytes」的記憶體位址  

* ***指標與陣列的關係***  
指標與陣列息息相關，當一個陣列被宣告時，陣列名稱可當作指標使用，指向該型態陣列的第一個元素  
ex:  
```
int * ptr,a[10];  
ptr=a+5;  
printf("%d %d",* a,* ptr);
```  
上述範例宣告了一個指向整數型態的指標和一個具有10個整數元素的陣列，a指向陣列的第一個元素，加上5後指向第六個元素，設定給指標變數ptr，因此第三行會印出a[0]與a[5]的值。陣列名稱雖視為指標，但不可任意修改。  
ps:陣列本身名稱為一指標，指向第一個元素，不是指向整個陣列，但使用sizeof運算子想找出陣列大小時，陣列名稱又代表了整個陣列  
```  
int a [3];  
printf("%d",sizeof(a));  
```  
因為陣列具有三個int型態的元素，3 * 4等於12  

* ***將指標當引數傳遞進函式***  
在C語言中，可以將引數來傳遞函式，因指標紀錄了變數的記憶體位址，可以利用指標進行資料修改


                
 


