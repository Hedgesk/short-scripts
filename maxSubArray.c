int maxSubArray(int* nums, int numsSize){
  int dynamic_sums[numsSize];
  int max = nums[0];
  dynamic_sums[0] = max;
  int i;
  for(i=1;i<numsSize;i++){
    if(dynamic_sums[i-1] > 0){
      dynamic_sums[i] = dynamic_sums[i-1] + nums[i];
    }else{
      dynamic_sums[i] = nums[i];
    }
    if(dynamic_sums[i]>max){
      max = dynamic_sums[i];
    }
  }
  return max;
}


int main(void)
{
  printf("Hello! This is maxSubArray.\n");
  int input[] = {-2,1,-3,4,-1,2,1,-5,4};
  int output;
  output = maxSubArray(input, 9);
  printf("->");
  printf("%d\n", output);
}