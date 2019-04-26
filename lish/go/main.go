package main

import (
	"fmt"
	"npc/lish/go/formula"
	"npc/lish/go/practice"
)

func main() {
	// 测试平均值、方差
	data := []float64{22, 33, 44, 55.5, 67.8, 77.2, 88, 99}
	avg, variance, standard, resultMin, resultMax := formula.Variance(data)

	fmt.Printf("平均 : %f\n", avg)
	fmt.Printf("方差 : %f\n", variance)
	fmt.Printf("标准差 : %f\n", standard)
	fmt.Printf("置信区间 : %f ~ %f\n", resultMin, resultMax)

	// 测试练习题
	practice.P190426()
}
