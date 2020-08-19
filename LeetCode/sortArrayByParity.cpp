class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> evenNum;
        vector<int> oddNum;
        vector<int> result;
        for(int i = 0; i < A.size(); i++){
            if (A[i] % 2 == 0){
                evenNum.push_back(A[i]);
            } 
            else{
                oddNum.push_back(A[i]);
            }
        }
        result.insert(result.begin(), evenNum.begin(), evenNum.end());
        result.insert(result.end(), oddNum.begin(), oddNum.end());
        return result;
    }
};