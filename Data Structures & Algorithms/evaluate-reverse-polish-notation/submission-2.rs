impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();

        for op in tokens {
            match op.as_str() {
                "+" | "-" | "*" | "/" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();

                    let result = match op.as_str() {
                        "+" => a + b,
                        "-" => a - b,
                        "*" => a * b,
                        "/" => a / b,
                        _ => unreachable!(),
                    };

                    stack.push(result);
                }

                _ => stack.push(op.parse::<i32>().unwrap()),
            }
        }

        stack.pop().unwrap()
    }
}