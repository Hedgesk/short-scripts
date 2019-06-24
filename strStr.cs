public class Solution {
    public int StrStr(string haystack, string needle) {
        int pos = 0;
        int i = 0;
        if(needle.Length == 0){
            return 0;
        }
        
        while(i < haystack.Length){
            if(haystack[i] == needle[pos]){
                pos = pos + 1;
                if(pos == needle.Length){
                    return i - pos + 1;
                }
            }else{
                i = i - pos;
                pos = 0;
            }
            i = i + 1;
        }   
        return -1;
    }
}