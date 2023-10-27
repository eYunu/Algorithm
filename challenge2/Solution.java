package challenge2;

// import java.util.Arrays;
  
// Main class
public class Solution {
  
    public static int[] solution(int[] l, int t) {
        // Your code here
        int[] result = {-1, -1};
        int aryLen = l.length;
        if((aryLen < 1) || (aryLen > 100)) {
            return result;
        }
        if((t <= 0) || (t > 250)) {
            return result;
        }

        byte ResultFound = 0;
        for(int i=0; i<aryLen; i++) {
            if((l[i] < 1) || (l[i] > 100)) {
                int[] errorR = {-1, -1};
                return errorR;
            }
            int sum = 0;
            for(int j=i; (j<aryLen)&&(ResultFound==0); j++){
                sum += l[j];
                if(sum == t) {
                    result[0] = i;
                    result[1] = j;
                    ResultFound = 1;
                } else if(sum > t) {
                    break;
                }
            }
        }
        return result;
    }

    public static int[] test(int[] inputs, int t) {
        int[] out = {};
        out = solution(inputs, t);
        System.out.printf("[len: %d], %d, %d", inputs.length, out[0], out[1]);
        return out;
    }

    public static void main(String[] args) {
        // int[] input = {1, 2, 2, 5, 2,};
        // int[] input = {'a'};
        int[] input = {2,1,50,20,90,2,2,2,5,2,1,1,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,20,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,1,2,2,5,2,};
        test(input, 97);
        
        // int[] input = {1, 2, 3, 4};
        // test(input, 12);
    }


}



