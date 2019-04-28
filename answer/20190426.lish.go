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
	deviation := 0.1
	p := 0.4

	// 第一题，计算置信区间
	d := 1.96 * math.Sqrt(variance*(1.0-size/total)/size)
	resultMin := (avg - d) * total
	resultMax := (avg + d) * total
	fmt.Printf("95%%的置信区间 : %.0f ~ %.0f\n", resultMin, resultMax) // 95%的置信区间 : 5921 ~ 19079

	// 第二题，计算无放回抽样样本量
	n0 := math.Pow(1.96/(deviation*avg), 2) * variance
	n := n0 / (1 + n0/total)
	fmt.Printf("10%%误差样本量 : %.0f\n", n) // 10%误差样本量 : 755

	// 第三题，计算用水超量的户数
	d2 := 1.96 * math.Sqrt(p*(1.0-p)*(1.0-size/total)/(size-1))
	resultMin2 := (p - d2) * total
	resultMax2 := (p + d2) * total
	fmt.Printf("95%%的置信区间 : %.0f ~ %.0f\n", resultMin2, resultMax2) // 95%的置信区间 : 308 ~ 492

	// 第四题，计算区间降低的样本量
	// 推导：(1.0-size/total)/(size-1)=4*(1.0-n1/total)/(n1-1)
	tmp := (1.0 - size/total) / (size - 1) / 4
	n1 := (1.0 + tmp) / (tmp + 1.0/total)
	fmt.Printf("区间降低一半的样本量 : %.0f\n", n1) // 区间降低一半的样本量 : 306
}
