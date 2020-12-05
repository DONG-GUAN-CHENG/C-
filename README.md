# C-
The process of learning and side project 
#### ***程式語言簡介***
機器語言->組合語言(組譯器，需利用指令集來規劃程式)->編譯語言(編譯器，速度快)->直譯語言(一行一行翻譯，速度較編譯語言慢)
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
常數與變數的區別，常數不行被指定或改變  
宣告方式:``const type var-name;``，另外可以使用``#define``開頭的前置處理器  
來變換常數或字串的自訂識別名稱(切記不可加上分號) 語法:``#define 識別子 字串``
* ***printf()格式化輸出函式***  
語法:``printf(control string ,argument);``
control string 是控制字串，包含想輸出的文字格式，以及想輸出的變數轉換格式或特殊字元
argument:引數，變數個數依照control string決定要輸出的變數有幾個
%d->整數, %f->浮點數,%lf->雙精度浮點數,%c->字元,%S->字串,%%->印出%%,\\->印出\,\'->印出',\''->印出'',\n->換行,\b->逼一聲,\t->Tab  
ex:printf(%d,number)->將變數number以%d所代表的整數型態印出  
單行註解以「//」,多行註解以「/*開頭」,『結尾 */』來包覆



