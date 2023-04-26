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
 * Complete the 'cutTheSticks' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function cutTheSticks(arr) {
    // initial the result array and the minimum value variable
    let result = []
    let minimumVal = Infinity
    
    
    function findMin(a) {
        let minimumVal = Infinity
        for (let i = 0; i < a.length; i++) {
            if (a[i] < minimumVal)
                minimumVal = a[i]
        }
        return minimumVal
    }
    
    result.push(arr.length)
    
    if (arr.length > 0) {
        minimumVal = arr.pop(findMin(arr))
        console.log("minimumVal is ", minimumVal)
        
        if (arr.length > 0) {
            for (let i = 0; i < arr.length; i++) {
                arr[i] -= minimumVal
            }
        }
    }
    
    console.log(arr)
    
    return result

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const result = cutTheSticks(arr);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
