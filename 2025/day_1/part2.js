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

    let vals = [];
    for (let i = 0; i < ll.length; i++) {
        let count = 0; 
        for (let j = 0; j < rr.length; j++) {
            if (rr[j] === ll[i]) {
                count++;
            }
        }

        // push similary score into array
        vals.push(ll[i] * count);
    }

    const result = vals.reduce((a, val) => a + val, 0);
    console.log(result);
}

openFile();
