/* ============================================== */
/* 程式目的:為了將考試成績分類並擇優列印錄取通知單，
宣告各變數*/  
/* ============================================== */

#include<stdio.h>
#include<stdlib.h>
#define MAXStudentNum 10          /* 定義最大數量的考生數量，利用前置處理器*/
int rank1,rank2,rank3,rank4;   

struct record /*以結構去儲存考生姓名、種類、各科成績*/
{
	char name[10];            /* 字元陣列儲存考生姓名*/
	char rank;                /* 考生成績分類的種類 */
	float chinese;            /* 浮點數資料型態儲存各科成績*/
	float mathematic;
	float english;
	float physics;
	float chemistry;
	float politics;
	float total;
};
typedef struct record Record; /*自定義結構以新型態名稱表示*/
Record student[MAXStudentNum];
Record rankSort[MAXStudentNum];
int studentNum;

/* ---------------------------------------------- */
/* 將各名考生各科成績輸入並進行分類  */
/* ---------------------------------------------- */
void inputData()
{
	int sign = 0;           /* 分類標記 */
	int i;                  /* 循環修正變量 */
	int rankA = 0;          /* 定義各種考生所屬分類*/
	int rankB = 0;
	int rankC = 0;
	int rankD = 0;
	printf( "\t******************************************************\n" );
	printf( "\t**           成績處理系統                **\n" );
	printf( "\t******************************************************\n" );
	printf( "\n\n" );
	printf( "\t成績項目:微積分、演算法、半導體製程、生醫光電" );
	printf( "\n\n" );
	while(1){
        printf( "\n\t 請輸入考生人數 1~%d ", MAXStudentNum);
	    scanf( "%d", &studentNum );
	    if(0 < studentNum && studentNum <= MAXStudentNum)
	        break;
	    else{
            printf("輸入錯誤，請重新輸入");
        }
    }
	
    printf( "\tøÈ§Jßπ¶“•Õ©m¶W§ß´·´ˆ Enter ®Ãß«øÈ§J¶®¡Z\n" );
	/* •H§U®B∆JøÈ§J¶“•Õ™∫¶U¨Ï¶®¡Z°A®√•Œsign≠p∫‚§£§ŒÆÊ¨Ï•ÿ≠”º∆ */
	for ( i = 0; i < studentNum; i++ )
	{
		printf( "\n" );
		printf( "\t¶“•Õ%d:", i + 1 ); printf( "\t" );
		scanf( "%s",&student[i].name ); 
		printf( "\t  ∞Í§Â°G" );scanf( "%f",&student[i].chinese ); 
		     if ( student[i].chinese < 60 ) sign++;
		printf( "\t  º∆æ«°G" );scanf( "%f",&student[i].mathematic ); 
		     if ( student[i].mathematic < 60 ) sign++;
		printf( "\t  ≠^§Â°G" );scanf( "%f",&student[i].english ); 
		     if ( student[i].english < 60 ) sign++;
		printf( "\t  ™´∏Ã°G" );scanf( "%f",&student[i].physics ); 
		     if ( student[i].physics < 60 ) sign++;
		printf( "\t  §∆æ«°G" );scanf( "%f",&student[i].chemistry );
		     if ( student[i].chemistry < 60 ) sign++;
	    printf( "\t  ¨F™v°G" );scanf( "%f",&student[i].politics ); 
		     if ( student[i].politics < 60 ) sign++;
		if ( sign == 0 ) 
		{
			student[i].rank = 'A';
			rankA++;
		}
		else if ( sign == 1 )
		{
			student[i].rank = 'B';
			rankB++;
		}
		else if ( sign == 2 )
		{
			student[i].rank = 'C';
			rankC++;
		}
		else 
		{
			student[i].rank = 'D';
		    rankD++;
        };

        sign = 0;

        student[i].total = student[i].chinese + student[i].mathematic +
                           student[i].english + student[i].physics + 
                           student[i].chemistry + student[i].politics;
    }


    printf( "\n¶π¶∏¶“∏’§§°A¶U√˛¶“•Õ§Hº∆§¿ßO¨∞:\nA:%d\tB:%d\tC:%d\tD:%d\n",
                      rankA, rankB, rankC, rankD );
    printf( "\n A√˛ßO•N™Ì™∫¨O•˛≥°≥£§ŒÆÊ°AB√˛ßO•N™Ì™∫¨O¶≥§@¨Ï§£§ŒÆÊ°A\n");
    printf( " C√˛ßO•N™Ì™∫¨∞®‚¨Ï§£§ŒÆÊ°AD√˛ßO•N™Ì™∫¨∞§T¨Ï•H§W§£§ŒÆÊ\n");
    rank1 = rankA;
    rank2 = rankB;
    rank3 = rankC;
    rank4 = rankD;
}
    
/* ------------------------------------------------------ */
/* 列印錄取學生的通知單信息                          */
/* ------------------------------------------------------ */
void typeNotice( int j )
{
    int i;
    for( i = 0; i < 20; i++ ) printf( "====" ); printf( "\n" );
    printf( "\t\t\t-----ø˝®˙≥q™æ-----\n" );
    printf( "\t\t\t%s \n",rankSort[j].name );
    printf( "\t\t\t  Æ•≥ﬂ±z°I±z§w≥Qø˝®˙°C\n" );
    printf( "\t\t\t     ±z™∫¶®¡Z:\n" );
    printf( "\t\t\t∞Í§Â\t\t%.2f\n\t\t\tº∆æ«\t\t%.2f\n\t\t\t≠^§Â\t\t%.2f\n",
           rankSort[j].chinese, rankSort[j].mathematic, rankSort[j].english);
    printf( "\t\t\t™´≤z\t\t%.2f\n\t\t\t§∆æ«\t\t%.2f\n\t\t\t¨F™v\t\t%.2f\n", 
           rankSort[j].physics, rankSort[j].chemistry, rankSort[j].politics);
    printf( "\t\t\t¡`§¿\t\t%.2f\n",rankSort[j].total);
    
    for( i = 0; i < 20; i++ ) printf( "====" ); printf( "\n" );
}
/* ----------------------------------- */
/* ®œ•ŒøÔæ‹±∆ß«™k°A®Ãæ⁄¡`§¿•—§j±∆®Ï§p  */
/* ----------------------------------- */
void sort()   
{
    int i,j;
    Record temp;
    for( i = 0; i < studentNum-1; i++ )
        for( j = i + 1; j < studentNum; j++ )
            if( student[i].total < student[j].total )
            {
                temp = student[i];
                student[i] = student[j];
                student[j] = temp;
            }
}


/* ------------------------------------------ */
/* πÔ§w∏g´ˆ¡`§¿±∆¶nß«™∫¶“•Õ∂i¶Ê§¿√˛±∆ß«≥B≤z   */
/* ------------------------------------------ */
void addressSort()          
{
    int ja, jb, jc, jd;   /* ¶U√˛¶“•Õ¶b∑sº∆≤’§§™∫∞_©l¶aß} */
    int i;

    ja = 0;               /* ™Ï©l§∆ */
    jb = rank1;
    jc = rank1 + rank2;
    jd = rank1 + rank2 + rank3;
    
    for( i = 0; i < studentNum; i++ )  /* ±N¶“•Õ´ˆA,B,C,D•|√˛±∆ß« */
    {
        switch ( student[i].rank )
        {
        case 'A':
            rankSort[ja] = student[i];
            ja++; break;
        case 'B':        
            rankSort[jb] = student[i];
            jb++; break;
        case 'C':
            rankSort[jc] = student[i];
            jc++; break;
        case 'D':
            rankSort[jd] = student[i];
            jd++; break;
        }
    }
}

/* ------------------------------------------- */
/* ø˝®˙∞TÆß™∫øÈ§J§Œ≥q™æÆ—øÈ•X   */
/* ------------------------------------------- */
void ioControl()
{
    int i;
    int admitNum;         /* ≥o¶∏ø˝®˙™∫¡`§Hº∆ */

    printf( "\nΩ–øÈ§J≠pπ∫ø˝®˙™∫§Hº∆: " );
    scanf( "%d", &admitNum );
    if ( admitNum > studentNum )
    {
        printf( "\nøÈ§Jø˘ª~,∂W•X¶“•Õ¡`º∆Ωd≥Ú°CΩ–≠´∑søÈ§J:  " );
        scanf( "%d", &admitNum );
    }
    for ( i = 0; i < admitNum; i++ )
        typeNotice( i );
}
/* ------------------------------------------- */
/* •Dµ{¶°                                      */
/* ------------------------------------------- */
int main()
{
    inputData();
    sort();               /* ¡`§¿¿u•˝ */
    addressSort();        /* √˛ßO¿u•˝ */
    ioControl();
    system("pause");
    return 0;
}

