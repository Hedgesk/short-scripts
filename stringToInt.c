#include <stdio.h>
#include <math.h>

int myAtoi(char * str){
  printf(str);
  int tmp=0;
  int total=0;
  int sign = 1;
  int assigned = 0;
  while(*str != '\0'){
    switch(*str){
      case '0':
        tmp = 0;
        assigned += 1;
        break;
      case '1':
        assigned += 1;
        tmp = 1;
        break;
      case '2':
        assigned += 1;
        tmp = 2;
        break;
      case '3':
        assigned += 1;
        tmp = 3;
        break;
      case '4':
        assigned += 1;
        tmp = 4;
        break;
      case '5':
        assigned += 1;
        tmp = 5;
        break;
      case '6':
        assigned += 1;
        tmp = 6;
        break;
      case '7':
        assigned += 1;
        tmp = 7;
        break;
      case '8':
        assigned += 1;
        tmp = 8;
        break;
      case '9':
        assigned += 1;
        tmp = 9;
        break;
      case '-':
        sign = -1;
        assigned += 1;
        if(assigned> 1){
          return total;
        }
        tmp = 0;
        break;
      case '+':
        assigned += 1;
        if(assigned> 1){
          return total;
        }
        tmp = 0;
        break;
      case ' ':
        str++;
        if(total > 0 || assigned>0){
          return total;
        }else{
          continue;
        }
      default:
        return total;
    }

    if(total > (pow(2, 31)-1-tmp)/10){
       return pow(2, 31)-1;
    }else if(total < (-1*pow(2, 31)+tmp)/10){
      return -1*pow(2, 31);
    }

    total *= 10;
    total += tmp * sign;
    str++;
    
  }
  return total;
}


int main(void)
{
  printf("Hello! This is myAtoi.\n");
 
  int output = myAtoi("1");
  printf("->");
  printf("%d\n", output);

  output = myAtoi("12");
  printf("->");
  printf("%d\n",output);

  output = myAtoi("4193 with words");
  printf("->");
  printf("%d\n",output);

  output = myAtoi("   -42");
  printf("->");
  printf("%d\n",output);

  output = myAtoi("2147483646");
  printf("->");
  printf("%d\n",output);

  output = myAtoi("2147483648");
  printf("->");
  printf("%d\n",output);

  output = myAtoi("-91283472332");
  printf("->");
  printf("%d\n",output);

 return 0;
}