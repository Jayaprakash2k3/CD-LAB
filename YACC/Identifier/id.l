%{
#include "y.tab.h"  // Include the Yacc header file
%}

%%
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
.                       { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
