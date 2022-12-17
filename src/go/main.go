package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/fatih/color"
)

var (
	authHeader string
)

func init() {
	flag.StringVar(&authHeader, "auth", "", "Authorization header to include in requests")
	flag.Parse()
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Usage: enumerate-http-methods <host>")
	}

	host := os.Args[1]

	fmt.Println("Enumerating HTTP methods for host:", host)

	methods := []string{
		http.MethodGet,
		http.MethodHead,
		http.MethodPost,
		http.MethodPut,
		http.MethodPatch,
		http.MethodDelete,
		http.MethodConnect,
		http.MethodOptions,
		http.MethodTrace,
	}

	for _, method := range methods {
		req, err := http.NewRequest(method, host, nil)
		if err != nil {
			log.Fatal(err)
		}

		if authHeader != "" {
			req.Header.Set("Authorization", authHeader)
		}

		client := &http.Client{}
		resp, err := client.Do(req)
		if err != nil {
			log.Fatal(err)
		}
		defer resp.Body.Close()

		statusCode := resp.StatusCode
		statusText := http.StatusText(statusCode)

		var colorFunc func(format string, a ...interface{}) (n int, err error)
		if statusCode >= 200 && statusCode < 300 {
			color.Set(color.FgGreen)
			colorFunc = fmt.Printf
		} else if statusCode >= 300 && statusCode < 400 {
			color.Set(color.FgCyan)
			colorFunc = fmt.Printf
		} else if statusCode >= 400 && statusCode < 500 {
			color.Set(color.FgYellow)
			colorFunc = fmt.Printf
		} else {
			color.Set(color.FgRed)
			colorFunc = fmt.Printf
		}

		colorFunc("%s %d %s\n", method, statusCode, statusText)
		color.Unset()
	}
}
