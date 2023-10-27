package challenge2_2;

public class Solution {
    public static String solution(long x, long y)
    {
        if(y <= 0) {
            return "0";
        }
        long offsetY = y - 1;
        long MaxPossibleSection = x + offsetY;
        // long MaxPossibleSum = recursive_sum(MaxPossibleSection);
        long MaxPossibleSum = 0;
        for(long xloop = MaxPossibleSection; xloop > 0; xloop--) {
            MaxPossibleSum += xloop;
        }
        return String.valueOf( MaxPossibleSum - offsetY );

    }

    public static long recursive_sum(long xmax) {
        if (xmax > 0) {
            return xmax + recursive_sum(xmax - 1);
        } else {
            return 0;
        }
    }
    
    
    public static String test(int x, int y) {
        String id = "";
        id = solution(x, y);
        System.out.printf("[id: %s], x:%d, y:%d\n", id, x, y);

        return id;
    }

    public static void main(String[] args) {
        // int[] input = {1, 2, 2, 5, 2,};
        // int[] input = {'a'};
        test(2, 10);
        test(10, 10);
        test(3, 2);
        test(3, 3);
        test(2, 3);
        test(1, 4);
        test(1, 5);
        test(5, 1);
        
        // int[] input = {1, 2, 3, 4};
        // test(input, 12);
    }
}
