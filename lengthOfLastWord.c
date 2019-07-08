

int lengthOfLastWord(char * s){
  int pos = strlen(s);
  int count = 0;
  for(pos=strlen(s)-1; pos >=0; pos--){
    if(count > 0 & s[pos]==' '){
      return count;
    }else if(s[pos]!=' '){
      count ++;
    }
  }
  return count;
}

int main(void)
{
  printf("Hello! This is lengthOfLastWord.\n");
 
  int output = lengthOfLastWord("Hello World");
  printf("->");
  printf("%d\n", output);

  output = lengthOfLastWord("Hello Worlds ");
  printf("->");
  printf("%d\n",output);

  output = lengthOfLastWord("Hello World 4");
  printf("->");
  printf("%d\n",output);

}