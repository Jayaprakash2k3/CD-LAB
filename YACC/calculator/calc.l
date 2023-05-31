%{
#include "y.tab.h"  // Include the Yacc header file
%}

%%
[0-9]+          { yylval.num = atoi(yytext); return NUM; }
[+\-*/()]      { return yytext[0]; }
[ \t\n]         ;  // Ignore whitespace characters
.               { printf("Invalid character: %c\n", yytext[0]); }
%%

int yywrap() {
    return 1;
}
