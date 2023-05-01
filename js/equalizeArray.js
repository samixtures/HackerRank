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
 * Complete the 'equalizeArray' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function equalizeArray(arr) {
    // Write your code here
    
    /*
        Find out which element is the most frequent using a frequency map
        Keep a counter variable, delete all elements except the one that's most
        frequent, increment variable
        Return Variable
    */
    
    let freq = {};
    let maxCount = 0;
    let mostFrequentedValue = null;
    
    for (let i = 0; i < arr.length; i++) {
        let value = arr[i];
        if (freq[value]) {
            freq[value]++;
        }
        else {
            freq[value] = 1;
        }
        
        if (freq[value] > maxCount) {
            maxCount = freq[value];
            mostFrequentedValue = value;
        }
    }
    
    let removeCounter = 0
    
    for (let i = 0; i < arr.length; i++) {
        let val = arr[i];
        if (val != mostFrequentedValue) {
            removeCounter++;
        }
    }
    
    return removeCounter;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const result = equalizeArray(arr);

    ws.write(result + '\n');

    ws.end();
}
