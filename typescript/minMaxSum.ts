'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

/*
    could find min and max on first run through then second run all
    others added together that isnt min or max.
*/
function miniMaxSum(arr: number[]): void {
    let min: number;
    let minSum: number = 0;
    let max: number;
    let maxSum: number = 0;
    let foundMax: boolean = false;
    let foundMin: boolean =  false;
    if (arr[0] > arr[1]) {
        max = arr[0];
        min = arr[1];
    } else if (arr[0] < arr[1]) {
        max = arr[1];
        min = arr[0];        
    } else {
        // they are equal
        max = arr[0];
        min = arr[0];      
   }
    for(let i: number = 2; i < arr.length; i++) {
        if(arr[i] > max) {
            max = arr[i];
        } else if (arr[i] < min) {
            min = arr[i];
        }
    }
    if (min == max) {
          minSum = min*(arr.length-1);
          maxSum = max*(arr.length-1); 
    } else {
        for(let i: number = 0; i < arr.length; i++) {
            if (arr[i] != max){
                minSum = minSum + arr[i];
            }
            if (arr[i] != min) {
                maxSum += arr[i];
            }
        }
    }
    console.log(`${minSum} ${maxSum}`);

}

function main() {

    const arr: number[] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    miniMaxSum(arr);
}
