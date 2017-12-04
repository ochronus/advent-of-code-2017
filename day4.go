package main

import (
	"os"
	"bufio"
	"fmt"
	"strings"
	"sort"
)

type RuneSlice []rune

func (r RuneSlice) Len() int           { return len(r) }
func (r RuneSlice) Swap(i, j int)      { r[i], r[j] = r[j], r[i] }
func (r RuneSlice) Less(i, j int) bool { return r[i] < r[j] }

func StringToRuneSlice(s string) []rune {
	var r []rune
	for _, runeValue := range s {
		r = append(r, runeValue)
	}
	return r
}

func areAnagrams(s1, s2 string) bool {
	var r1 RuneSlice = StringToRuneSlice(s1)
	var r2 RuneSlice = StringToRuneSlice(s2)

	sort.Sort(r1)
	sort.Sort(r2)

	return string(r1) == string(r2)
}

func isValidPassphrase1(s string) bool {
	words := strings.Fields(s)
	counts := make(map[string]int, len(words))
	for _, word := range words {
		counts[word]++
		if counts[word] > 1 {
			return false
		}
	}
	return true
}

func isValidPassphrase2(s string) bool {
	words := strings.Fields(s)
	for i, word := range words {
		for j := i+1; j < len(words); j++ {
			if areAnagrams(word, words[j]) {
				return false
			}
		}
	}
	return true
}


func main() {
	counter1 := 0
	counter2 := 0
	f, err := os.Open("day4-input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if isValidPassphrase1(scanner.Text()) {
			counter1++
		}
		if isValidPassphrase2(scanner.Text()) {
			counter2++
		}
	}
	fmt.Println(counter1)
	fmt.Println(counter2)
}