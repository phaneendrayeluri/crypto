package main

import (
	_ "crypto"
	"crypto/rand"
	_ "crypto/rand"
	"log"
)

func main() {
	bees, err := rand.Read(make([]byte, 16))
	if err != nil {
		panic(err)
	}
	log.Println(bees)
}
