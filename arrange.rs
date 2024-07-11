fn arrange(remain: &Vec<i32>, build: &Vec<i32>) {
    if remain.is_empty() {
        println!("{:?}", build);
    } else {
        for i in 0..remain.len() {
            let mut build_copy: Vec<i32> = build.clone();
            let last = remain[i];
            build_copy.push(last);
            let mut remain_copy: Vec<i32> = remain.clone();
            remain_copy.remove(i);
            arrange(&remain_copy, &build_copy);
        }
    }
}

fn main() {
    let data = vec![1, 2, 3];
    let result = vec![];
    arrange(&data, &result);
}
