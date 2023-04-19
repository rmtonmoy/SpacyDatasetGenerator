#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("trainData.txt", "r", stdin);
    //freopen("trainData_formatted", "w", stdout);

    printf("[");

    char prev_char, next_char;
    scanf("%c", &prev_char);
    while(true){
        printf("%ch", prev_char);
        scanf("%c", &next_char);
        if(next_char == EOF){
            break;
        }

        if(prev_char == '(') printf("[");
        else if(prev_char == ')') printf("]");
        else if(prev_char == '\'') printf("\"");
        else printf("%c", prev_char);

        prev_char = next_char;
    }

    printf("]");

    return 0;
}
