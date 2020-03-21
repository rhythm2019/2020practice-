#include <stdio.h>
#include <string.h>
#include <malloc.h>
#define ElementType Spot
#define Stack_Size 100
#define TRUE 1
#define FALSE 0
/*
@说明：骑士漫游，常规深度搜索（用栈实现）。
@author:rhythm
@date:20200321
*/
typedef struct
{
    int x;
    int y;
    int d; //探索过的方向
} Spot;
typedef struct
{
    ElementType elem[Stack_Size];
    int top;
} SeqStack;
void InitStack(SeqStack *S)
{
    S->top = -1;
}
int IsEmpty(SeqStack *S)
{
    return (S->top == -1 ? TRUE : FALSE);
}
int IsFull(SeqStack *S)
{
    return (S->top == Stack_Size - 1 ? TRUE : FALSE);
}
int Push(SeqStack *S, ElementType e)
{
    if (S->top == Stack_Size - 1)
        return (FALSE);
    S->top++;
    S->elem[S->top].x = e.x;
    S->elem[S->top].y = e.y;
    S->elem[S->top].d = e.d;
    return (TRUE);
}
int Pop(SeqStack *S, ElementType *e)
{
    if (S->top == -1)
        return (FALSE);
    else
    {
        e->x = S->elem[S->top].x;
        e->y = S->elem[S->top].y;
        e->d = S->elem[S->top].d;
        S->top--;
        return (TRUE);
    }
}
int GetTop(SeqStack *S, ElementType *e)
{
    if (S->top == -1)
        return (FALSE);
    else
    {
        e->x = S->elem[S->top].x;
        e->y = S->elem[S->top].y;
        e->d = S->elem[S->top].d;
        return (TRUE);
    }
}
int Board[8][8] = {0};
int Direction[2][9] = {{0, -2, -1, 1, 2, 2, 1, -1, -2},
                       {0, 1, 2, 2, 1, -1, -2, -2, -1}};
int Feasible(int x, int y)
{
    if ((0 <= x) && (x < 8) && (0 <= y) && (y < 8) && (Board[x][y] == 0))
        return 1;
    else
        return 0;
}
int NextDirection(Spot Cur)
{
    int i, x, y;
    for (i = Cur.d + 1; i <= 8; i++)
    {
        x = Cur.x + Direction[0][i];
        y = Cur.y + Direction[1][i];
        if (Feasible(x, y))
            return i;
    }
    return 0;
}

int print_chess()
{
    int i, j;
    for (i = 0; i < 8; i++)
        for (j = 0; j < 8; j++)
            printf("%d %d %d\n", i, j, Board[i][j]);
    return 1;
}

int main()
{
    Spot Cur, Next;
    int k, Step = 1;
    SeqStack *path = (SeqStack *)malloc(sizeof(SeqStack));
    InitStack(path);
    Cur.x = 0;
    Cur.y = 0;
    Cur.d = 0;
    Push(path, Cur);
    Board[Cur.x][Cur.y] = Step;
    while (Step > 0 && Step < 64)
    {
        k = NextDirection(Cur);
        if (k != 0)
        {
            Pop(path, &Next);
            Cur.d = k;
            Push(path, Cur);
            Next.x = Cur.x + Direction[0][k];
            Next.y = Cur.y + Direction[1][k];
            Next.d = 0;
            Push(path, Next);
            //
            Cur.x = Next.x;
            Cur.y = Next.y;
            Cur.d = Next.d;
            Step++;
            Board[Cur.x][Cur.y] = Step;
        }
        else
        {
            Step--;
            Board[Cur.x][Cur.y] = 0;
            Pop(path, &Cur);
            GetTop(path, &Cur);
        }
    }
    printf("%d\n", Step);
    print_chess();
    printf("******************************\n");
    for (k = 0; k <= path->top; k++)
    {
        printf("%d %d %d\n", path->elem[k].x, path->elem[k].y, path->elem[k].d);
    }
    getchar();
    return 1;
}