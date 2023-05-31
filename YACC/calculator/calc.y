%{
#include <stdio.h>
%}

%token NUM

%%
start: expr   { printf("Result: %d\n", $1); };

expr: NUM                     { $$ = $1; }
    | expr '+' expr          { $$ = $1 + $3; }
    | expr '-' expr          { $$ = $1 - $3; }
    | expr '*' expr          { $$ = $1 * $3; }
    | expr '/' expr          { if ($3 != 0) $$ = $1 / $3; else yyerror("Division by zero"); }
    | '(' expr ')'           { $$ = $2; }
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
