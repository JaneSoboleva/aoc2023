package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	file, err := os.Open("day05_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	day05_lines := []string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		day05_lines = append(day05_lines, scanner.Text())
	}
	// fmt.Println(day05_lines)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	seedListString := strings.Fields(day05_lines[0])
	seedListString = seedListString[1:]
	var seedList []int
	for _, str := range seedListString {
		num, err := strconv.Atoi(str)
		if err != nil {
			fmt.Println("Error converting string to integer:", err)
			return
		}
		seedList = append(seedList, num)
	}
	// fmt.Println(seed_list)

	var remapLists [][]interface{}
	var newRemapList []interface{}
	expectANewList := false

	for i := 1; i < len(day05_lines); i++ {
		if day05_lines[i] == "" {
			expectANewList = true
			if len(newRemapList) > 0 {
				remapLists = append(remapLists, newRemapList)
			}
			newRemapList = nil
			continue
		}

		if expectANewList {
			splitResult := strings.Fields(day05_lines[i])
			if len(splitResult) > 0 {
				newRemapList = append(newRemapList, splitResult[0])
			}
			expectANewList = false
			continue
		}

		var newRemapElement []interface{}
		newRemapSplit := strings.Fields(day05_lines[i])
		for j := 0; j < 3; j++ {
			num, err := strconv.Atoi(newRemapSplit[j])
			if err == nil {
				newRemapElement = append(newRemapElement, num)
			} else {
				newRemapElement = append(newRemapElement, newRemapSplit[j])
			}
		}
		newRemapList = append(newRemapList, newRemapElement)
	}

	if len(newRemapList) > 0 {
		remapLists = append(remapLists, newRemapList)
	}

	// Print the resulting slice of slices
	// fmt.Println(remapLists)

	remapNumber := func(initialNumber int, remapElement []interface{}) int {
		for xI := 1; xI < len(remapElement); xI++ {
			switch v := remapElement[xI].(type) {
			case []interface{}:
				// If it's a []interface{}, perform the remapping logic
				if len(v) >= 3 {
					// Ensure that v has at least three elements before accessing v[1], v[2], etc.
					if start, ok := v[1].(int); ok {
						if end, ok := v[2].(int); ok && start <= initialNumber && initialNumber <= start+end-1 {
							return initialNumber - (start - v[0].(int))
						}
					}
				}
				// Add more cases if you have other types in remapElement
			}
			// case []int:
			// If it's a []int, perform the remapping logic
			// if v[1] <= initialNumber && initialNumber <= v[1]+v[2]-1 {
			// return initialNumber - (v[1] - v[0])
			// }
			// Add more cases if you have other types in remapElement
			// }
		}
		return initialNumber
	}

	phase02Minimum := 1000000000
	startTime := time.Now()

	processRange := func(wg *sync.WaitGroup, seedList []int, remapLists [][]interface{}, rangeLeft, rangeRight int, counter int) {
		defer wg.Done()

		for x := rangeLeft; x < rangeRight; x++ {
			counter++
			if counter >= 10000000 {
				newTime := time.Now()
				fmt.Printf("%v seconds passed. Processing %v in range %v - %v\n", newTime.Sub(startTime).Seconds(), x, rangeLeft, rangeRight)
				counter = 0
			}

			seedItem := x
			// fmt.Printf("Initial seed item: %v", seedItem)
			for j := 0; j < len(remapLists); j++ {
				seedItem = remapNumber(seedItem, remapLists[j])
				// fmt.Printf("New seed item: %v\n", seedItem)
			}

			if phase02Minimum > seedItem {
				phase02Minimum = seedItem
			}
		}
	}

	var wg sync.WaitGroup

	for i := 0; i < len(seedList); i += 2 {
		rangeLeft := seedList[i]
		rangeRight := seedList[i+1] + rangeLeft

		wg.Add(1)
		go processRange(&wg, seedList, remapLists, rangeLeft, rangeRight, 0)
	}

	wg.Wait()

	fmt.Printf("Phase 02 result: %v\n", phase02Minimum)
}
