package main

import (
	"fmt"
)

func main() {
	var i, e int = 1, 2

	for i := 0; i <= 10; i++ {
		fmt.Println("Index: ", i)
	}

	for i := range 10 {
		if i == 2 {
			fmt.Println("Lebron Jahamas")
		}
		fmt.Println("Dumbass number: ", i)
	}

	fmt.Println(e, i)
	fmt.Println("Hello Go!")

	var a [5]int
	fmt.Println("no: ", a)

	a[4] = 100
	fmt.Println("what", a)
	fmt.Println("wat", a[4])

	b := [...]int{1, 2, 4, 5, 4: 7, 3, 5, 7}
	fmt.Println("AH", b)
}
