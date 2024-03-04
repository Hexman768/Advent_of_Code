use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut floor = 0;
    let mut pos = 0;
    let mut part2 = 0;
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    
    for c in contents.chars() {
        pos += 1;
        if c == '(' {
            floor += 1;
        } else if c == ')' {
            floor -= 1;
        }

        if floor == -1  && part2 == 0 {
            part2 = pos;
        }
    }

    println!("Part 1 answer: {}, Part 2 answer: {}", floor, part2);
    Ok(())
}
