package main

import "fmt"

func solveDay15(generator_a int, generator_b int, iter_count int, part2 bool) int {
	count := 0
	for i := 0; i <= iter_count; i++ {
		for true {
			generator_a = (generator_a * 16807) % 2147483647
			if !part2 || generator_a%4 == 0 {
				break
			}
		}

		for true {
			generator_b = (generator_b * 48271) % 2147483647
			if !part2 || generator_b%8 == 0 {
				break
			}
		}

		if generator_a&65535 == generator_b&65535 {
			count++
		}

	}
	return count
}

func main() {
	fmt.Println(solveDay15(289, 629, 40000000, false))
	fmt.Println(solveDay15(289, 629, 5000000, true))

}
