fn main() {
    let max_n = 100;

    for n in 0..max_n {
        print!("{n}, ");
    }
    println!("");

    let texts = &["Hello", "world", "this", "is", "rust", "tutorial"];

    for text in texts {
        print!("{text} ");
    }
    println!("");
}
