function openFile(fn) {
    let lines = [];
    let lr = require('readline').createInterface({
        input: require('fs').createReadStream(fn)
    });

    lr.on('line', function(line) {
        lines.push(line);
    });

    lr.on('close', function(line) {
        solve(lines);
    });
}

function isLineSafe(line) {
    for (let j = 0; j < line.length-1; j++) {
        const a = parseInt(line[j]);
        const b = parseInt(line[j+1]);
        console.log(a.toString() + " " + b.toString());
        if ((b - a) === 0) {
            console.log('same values');
            return false;
        } else if ((b - a) > 3) {
            console.log('difference > 3');
            return false;
        }
    }
    //console.log('safe');
    return true;
}

function incCheck(line) {
    const inc = parseInt(line[0]) < parseInt(line[1]);
    console.log(line[0] + " " + line[1]);
    console.log(inc);
    for (let i = 0; i < line.length-1; i++) {
        console.log(line[i] + ' ' + line[i+1]);
        if (inc && parseInt(line[i]) > parseInt(line[i+1])) {
            console.log('should be inc but is not');
            return false;
        } else if (!inc && parseInt(line[i]) < parseInt(line[i+1])) {
            console.log('should not be inc but is');
            return false;
        }
    }
    return true;
}

function solve(lines) {
    let safes = 0;
    for (let i = 0; i < lines.length; i++) {
        const lineUnsort = lines[i].split(' ');
        if (!incCheck(lineUnsort)) {
            console.log('unsafe');
            continue;
        }
        const line = lineUnsort.sort();
        if (isLineSafe(line)) {
            safes += 1;
        } else {
            console.log('unsafe');
            continue;
        }
    }
    console.log(safes);
}

openFile('input.txt');

