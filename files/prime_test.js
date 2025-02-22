const fs = require('fs');

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function findPrimes(limit) {
    const startTime = process.hrtime();
    const primes = [];
    for (let i = 2; i < limit; i++) {
        if (isPrime(i)) primes.push(i);
    }
    const endTime = process.hrtime(startTime);
    return [primes.length, endTime[0] + endTime[1] / 1e9];
}

function runTest() {
// Create array from 1000 to 100000 with step of 1000
    const ranges = Array.from(
        { length: 200 }, 
        (_, i) => (i + 1) * 1000
    );
    
    const results = [];
    
    ranges.forEach(range => {
        const [count, duration] = findPrimes(range);
        results.push([range, count, duration]);
        // Add progress indicator
        console.log(`Completed range: ${range}`);
    });
    
    const csv = 'Range,Primes Found,Duration\n' + 
        results.map(row => row.join(',')).join('\n');
    fs.writeFileSync('nodejs_results.csv', csv);}

runTest();
