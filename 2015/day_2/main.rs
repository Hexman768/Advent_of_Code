use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("test.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let mut owned_string: String = "".to_owned();
    let mut l = 0;
    let mut w = 0;
    let mut h = 0;

    for c in contents.chars() {
        if c != 'x' {
            let borrowed_string: &str = &c.to_string();
            owned_string.push_str(borrowed_string);
        } else {
            println!("current number string: {}", owned_string);
        }
    }
    
    Ok(())
}
