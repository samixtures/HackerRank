'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'repeatedString' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. LONG_INTEGER n
 */

function repeatedString(s, n) {
    // Write your code here
    /*
        We need to find a more efficient algorithm.
        It'll likely due with the fact that we know
        how many a's are in the initial string.
        
        There might be a way to do it in o(1) time.
    */
    let letters = 0;
    let aCounter = 0;
    let currentLetter = "";
    
    while (letters < n) {
        currentLetter = s[letters % s.length];
        
        if (currentLetter == "a") {
            aCounter++;
        }
        
        letters++;
    }

    return aCounter;

}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const n = parseInt(readLine().trim(), 10);

    const result = repeatedString(s, n);

    ws.write(result + '\n');

    ws.end();
}
