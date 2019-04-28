package practice

// StratifiedVariance 输入分层抽样的个数、平均数、方差，计算总的个数、平均数、方差
func StratifiedVariance(nums, avgs, variances []float64) (sum, avg, variance float64) {

	if len(nums) != len(avgs) || len(avgs) != len(variances) || len(nums) == 0 {
		return
	}

	// 计算总量和平均数
	total := 0.0
	for index, num := range nums {
		sum += num
		total += avgs[index] * num
	}
	avg = total / sum

	// 计算总方差
	for index, vc := range variances {
		w := nums[index] / sum
		variance += (1.0 - w) * w / sum * vc
	}

	return
}
