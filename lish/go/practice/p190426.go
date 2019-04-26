package practice

import (
	"fmt"
	"math"
)

// P190426 练习
func P190426() {

	// 已知参数
	avg := 12.5
	variance := 1252.0
	total := 1000.0
	size := 100.0

	// 第一题
	d := 1.96 * math.Sqrt(variance*(1.0-size/total)/size)
	resultMin := avg - d
	resultMax := avg + d
	fmt.Printf("95%%的置信区间 : %f ~ %f\n", resultMin, resultMax) // 95%的置信区间 : 5.920703 ~ 19.079297
}
