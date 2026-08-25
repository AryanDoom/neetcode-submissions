impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; temperatures.len()];
        let mut stack: Vec<usize> = Vec::new();

        for i in 0..temperatures.len() {
            while let Some(&j) = stack.last() {
                if temperatures[i] > temperatures[j] {
                    stack.pop();
                    ans[j] = (i - j) as i32;
                } else {
                    break;
                }
            }

            stack.push(i);
        }

        ans
    }
}