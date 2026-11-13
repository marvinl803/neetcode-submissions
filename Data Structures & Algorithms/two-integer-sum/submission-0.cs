public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        /*
        target = 7
        [4,5,6]
         l     r
        */


        var dicti = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            var diff = target - nums[i];

            if (dicti.ContainsKey(diff))
            {
                return new int[] { dicti[diff], i };
            }
            dicti[nums[i]] = i;

        }
        return new int[] { }; 
    }
}
