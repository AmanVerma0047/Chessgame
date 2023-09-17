#include <stdio.h>


void print_board(int row_no,int col_no)
{
    if(row_no == 1 && col_no==1 || row_no == 8 && col_no==1) {
        printf("♖");
        printf(".");
    } else if(row_no == 1 && col_no==2 || row_no == 8 && col_no==2) {
        printf("♘");
        printf(".");
    } else if(row_no == 1 && col_no==3 || row_no == 8 && col_no==3) {

        printf("♗");
        printf(".");
    } else if(row_no == 1 && col_no==4 || row_no == 8 && col_no==4) {
        printf("♕");
        printf(".");
    } else if(row_no == 1 && col_no==5 || row_no == 8 && col_no==5) {
        printf("♔");
        printf(".");
    } else if(row_no == 1 && col_no==6 || row_no == 8 && col_no==6) {
        printf("♗");
        printf(".");
    } else if(row_no == 1 && col_no==7|| row_no == 8 && col_no==7) {
        printf("♘");
        printf(".");
    } else if(row_no == 1 && col_no==8 || row_no == 8 && col_no==8) {
        printf("♖");
        printf(".");
    } else if(row_no==3 || row_no==4||row_no==5||row_no==6) {
        printf(" . ");
    }
}

void main()
{
    int row,col,row_input,col_input;
    for(row=1; row<9; row++) {
        for(col=1; col<9; col++) {
            print_board(row,col);
// all important piecss printed above
            if(row ==2 || row==7) {
                printf("♙");
                printf(".");

            }

        }
        printf("\n");
    }
    printf("{Player-1}Enter the position of piece to move\n");
    printf("{Player-1}Enter the row_no:");
    scanf("%d",&row_input);
    printf("{Player-1}Enter the col_no:");
    scanf("%d",&col_input);


}

