// http://adventofcode.com/2017/day/2
// TODO refactor

package main

import (
	"strings"
	"fmt"
	"strconv"
	"math"
)

const day2Input = `414	382	1515	319	83	1327	116	391	101	749	1388	1046	1427	105	1341	1590
960	930	192	147	932	621	1139	198	865	820	597	165	232	417	19	183
3379	987	190	3844	1245	1503	3151	3349	2844	4033	175	3625	3565	179	3938	184
116	51	32	155	102	92	65	42	48	91	74	69	52	89	20	143
221	781	819	121	821	839	95	117	626	127	559	803	779	543	44	369
199	2556	93	1101	122	124	2714	625	2432	1839	2700	2636	118	2306	1616	2799
56	804	52	881	1409	47	246	1368	1371	583	49	1352	976	400	1276	1240
1189	73	148	1089	93	76	3205	3440	3627	92	853	95	3314	3551	2929	3626
702	169	492	167	712	488	357	414	187	278	87	150	19	818	178	686
140	2220	1961	1014	2204	2173	1513	2225	443	123	148	580	833	1473	137	245
662	213	1234	199	1353	1358	1408	235	917	1395	1347	194	565	179	768	650
119	137	1908	1324	1085	661	1557	1661	1828	1865	432	110	658	821	1740	145
1594	222	4140	963	209	2782	180	2591	4390	244	4328	3748	4535	192	157	3817
334	275	395	128	347	118	353	281	430	156	312	386	160	194	63	141
146	1116	153	815	2212	2070	599	3018	2640	47	125	2292	165	2348	2694	184
1704	2194	1753	146	2063	1668	1280	615	163	190	2269	1856	150	158	2250	2459`



func divisionSolution() int64 {
	lines := strings.Split(day2Input,"\n")
	var sum int64 = 0
	for _, line := range lines {
		numbers := strings.Split(line, "\t")
		var rowNums []int64

		for _, number := range numbers {
			num, _ := strconv.ParseInt(number, 10, 64)
			for _, otherNumber := range rowNums {
				if num < otherNumber {
					if otherNumber % num == 0 {
						sum += otherNumber / num
					}
				} else {
					if num % otherNumber == 0 {
						sum += num / otherNumber
					}
				}
			}
			rowNums = append(rowNums, num)
		}
	}
	return sum
}

func main() {
	var diffSum int64 = 0
	lines := strings.Split(day2Input,"\n")
	for _, line := range lines {
		numbers := strings.Split(line, "\t")
		var rowMin int64 = math.MaxInt64
		var rowMax int64 = 0
		for _, number := range numbers {
			num, _ := strconv.ParseInt(number, 10, 64)
			if num < rowMin {
				rowMin = num
			}
			if num > rowMax {
				rowMax = num
			}
		}
		diffSum += rowMax - rowMin
	}
	fmt.Println(diffSum)
	fmt.Println(divisionSolution())
	}
