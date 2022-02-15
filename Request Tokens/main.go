package main

import (
	"crypto/sha256"
	"encoding/hex"
	"strconv"
	"hash"
	"time"
	"fmt"
)

const (
	hashPattern string = "0001110111101110001111010101111011010001001110011000110001000110"
	secret string = "iEk21fuwZApXlz93750dmW22pw389dPwOk"
)

func requestToken(token string, timestamp string) string {
	var firstHash hash.Hash = sha256.New();
	var secondHash hash.Hash = sha256.New();

	firstHash.Write([]byte(secret + token));
	secondHash.Write([]byte(timestamp + secret));

	var stringHashOne string = hex.EncodeToString(firstHash.Sum(nil));
	var stringHashTwo string = hex.EncodeToString(secondHash.Sum(nil));

	var result string;

	for i := 0; i < len(hashPattern); i++ {
		if string(hashPattern[i]) == "0" {
			result += string(stringHashOne[i]);
		} else {
			result += string(stringHashTwo[i]);
		}
	}

	return result;
}

func main() {
	fmt.Println(requestToken("m198sOkJEn37DjqZ32lpRu76xmw288xSQ9", strconv.Itoa(int(time.Now().UnixNano() / 1e6))))
}