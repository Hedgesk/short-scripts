#include <stdio.h>
#include <math.h>

char * countAndSay(int n){
  char output[50];
  if(n==0){
    return("0");
  }
  int count[9] = {0};

  int power = 1;
  int tmp;
  while(n > 0){
    tmp = (n % (int)pow(10,power))/pow(10,power-1);
    printf("The mod is: %d\n", tmp);
    count[tmp-1] += 1;
    n = n - (tmp * pow(10,power-1));
    power++;
  }

  int i;
  for(i=0; i < 9; i++){
    if(count[i] > 0){
    	//printf("Count %d = %d\n", i+1, count[i]);
	char str[3];
        sprintf(str, "%d%d", i+1, count[i]);
        strcat(output, str);
    }
  }

  return(&output);
}

int main(void)
{
 printf("Hello! This is countAndSay.\n");
 char * output1 = countAndSay(1);
 printf("->");
 printf(output1);
 printf("\n");


 char * output2 = countAndSay(12);
 printf("->");
 printf(output2);
 printf("\n");
 return 0;
}