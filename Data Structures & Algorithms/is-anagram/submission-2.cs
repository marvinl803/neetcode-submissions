public class Solution {
    public bool IsAnagram(string s, string t) {

        var strd1 = s.ToCharArray();
        var strd2 = t.ToCharArray();
        Array.Sort(strd1);
        Array.Sort(strd2);

        var str1 = new string(strd1);
        var str2 = new string(strd2);

        return str1 == str2;
    }
}
