function openFile() {
    let lines = [];
    let lr = require('readline').createInterface({
        input: require('fs').createReadStream('input.txt')
    });

    lr.on('line', function(line) {
        lines.push(line);
    });

    lr.on('close', function(line) {
        solve(lines);
    });
}

function solve(lines) {
    let ll = [];
    let rr = [];
    for (let i = 0; i < lines.length; i++) {
        const str = lines[i].split(' ');
        ll.push(str[0]);
        rr.push(str[3]);
    }

    ll.sort();
    rr.sort();

    let vals = [];
    for (let i = 0; i < ll.length; i++) {
        vals.push(Math.abs(ll[i] - rr[i]));
    }

    const result = vals.reduce((a, val) => a + val, 0);
    console.log(result);
}

openFile();

