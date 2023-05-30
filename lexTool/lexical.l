%{
    #include <stdio.h>
%}
%%
#.+ {printf("%s is Header File",yytext);}
^(int|float|char|double).+; {printf("%s is DECLERATION STATEMENT",yytext);}
[a-zA-Z_][a-zA-z_0-9]*=.+; {printf("%s is ASSIGNMENT STATEMENT",yytext);}

%%
int main()
{
    FILE *f;
    f=fopen("input.c","r");
    yyin=f;
    yylex();
    printf("\n");
    return 0;
}
int yywrap(){
    return 1;
}