%{
#include <stdio.h>
#include <stdlib.h>
%}

%token ID

%%
start: ID   { printf("Valid identifier: %s\n", $1); }
      |     { printf("Invalid identifier\n"); }
      ;
%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char* msg) {
    printf("Error: %s\n", msg);
    return 0;
}
