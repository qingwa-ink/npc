package formula

import (
	"math"
)

// Variance 计算平均值、方差、标准差、置信区间
func Variance(data []float64) (avg, variance, standard, resultMin, resultMax float64) {
	sum := float64(0)
	// 计算均值
	for _, d := range data {
		sum += d
	}
	size := float64(len(data))
	avg = sum / size

	// 计算方差
	for _, d := range data {
		variance += math.Pow(d-avg, 2) / size
	}
	standard = math.Sqrt(variance)

	// 计算置信区间
	d := 1.96 * math.Sqrt(1/size) * standard
	resultMin = avg - d
	resultMax = avg + d

	return
}
