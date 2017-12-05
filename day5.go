// http://adventofcode.com/2017/day/5

package main

import (
	"os"
	"bufio"
	"strconv"
	"fmt"
)

func solveDay5(instructions []int64, isPart2 bool) int64 {
	steps := int64(0)
	jump := int64(0)
	localCopyOfInstructions := make([]int64, len(instructions))
	copy(localCopyOfInstructions, instructions)
	instructionCount := int64(len(localCopyOfInstructions))
	for jump < instructionCount && jump >= 0 {
		j := localCopyOfInstructions[jump]
		if j >= 3 && isPart2 {
			localCopyOfInstructions[jump] -= 1
		} else {
			localCopyOfInstructions[jump] += 1
		}
		jump += j
		steps++
	}

	return steps
}

func main() {
	f, err := os.Open("day5-input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(f)

	var instructionList []int64

	for scanner.Scan() {
		jump, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		instructionList = append(instructionList, jump)
	}
	defer f.Close()
	fmt.Println(solveDay5(instructionList, false))
	fmt.Println(solveDay5(instructionList, true))
}