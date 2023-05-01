'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the jumpingOnClouds function below.
function jumpingOnClouds(c, k) {
    /*
    i = 0
    k = 2
    n = 4
    2/4 = 0 remainder 2
    all numbers less than the size are the same remainder number, oh okay so this is just to
    make it so that if they jump past the size of the array it wraps back aground
    */
    
    // given array c and jump size k
    //each jump costs 1 unit of energy, and if we land on a thunderhead, we lose 2 additional units
    // the game ends when we get back to point 0
    
    
    let thunderHeadCounter = 0
    let energyDecrease = 0
    let i = 0
    
    // if (c[0] == 1) {
    //     thunderHeadCounter += 1
    // }
    
    i += k
    energyDecrease += 1
    if (c[i%c.length] == 1){
        console.log("c[i] and i are", [c[i], i])
        thunderHeadCounter += 1
    }
    while(i%c.length != 0) {
        i += k
        if (c[i%c.length] == 1) {
            console.log("c[i] and i are ", [c[i%c.length], i])
            thunderHeadCounter += 1
        }
        energyDecrease += 1
    }
    console.log("thunderHeadCounter is", thunderHeadCounter)
    return 100-energyDecrease-(2*thunderHeadCounter)

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    const c = readLine().split(' ').map(cTemp => parseInt(cTemp, 10));

    let result = jumpingOnClouds(c, k);

    ws.write(result + "\n");

    ws.end();
}
