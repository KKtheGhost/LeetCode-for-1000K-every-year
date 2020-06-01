package LeetCode

func twoSum(nums []int, target int) []int {
    var n int
    var res []int
    for i, v := range nums {
        n = target - v
        for i2, v2 := range nums {
            if v2 == n {
                if i != i2{
                    res = append(res, i)
                    res = append(res, i2)
                    return res
                }
            }
        }
    }
    return nil
}
