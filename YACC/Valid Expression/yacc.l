%{
#include"y.tab.h"
#include<stdio.h>
%}
%%
[\n] {return 0;}
[a-zA-z][a-zA-z0-9]* {return id;}
[0-9]+ {return dig;}
.         {return yytext[0];}
%%
