fn arrange(remain: &mut Vec<i32>, build: &mut Vec<i32>) {
    if remain.is_empty() {
        println!("{:?}", build);
    } else {
        for i in 0..remain.len() {
            let mut build_copy = build.clone();
            build_copy.push(remain[i]);
            let mut remain_copy = remain.clone();
            remain_copy.remove(i);
            arrange(&mut remain_copy, &mut build_copy);
        }
    }
}

fn main() {
    let mut data = vec![1, 2, 3, 4];
    let mut result = vec![];
    arrange(&mut data, &mut result);
}



fn arrange(remain: &mut Vec<i32>, build: &mut Vec<i32>) {
    if remain.is_empty() {
        println!("{:?}", build);
    } else {
        for i in 0..remain.len() {
            let mut build_copy = build.clone();
            let last = remain[i];
            build_copy.push(last);
            let mut remain_copy = remain.clone();
            remain_copy.remove(i);
            arrange(&remain_copy, build_copy);
        }
    }
}

fn main() {
    let mut data = vec![1, 2, 3, 4];
    let mut result = vec![];
    arrange(&mut data, &mut result);
  
}
