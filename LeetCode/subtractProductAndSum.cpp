class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        int result = 0;
        while (n != 0){
            int digit = n%10;
            sum += digit;
            product *= digit;
            result = product - sum;
            n/=10;
        }
        return result;
    }
};