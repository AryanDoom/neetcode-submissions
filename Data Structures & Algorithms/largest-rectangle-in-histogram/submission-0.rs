impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut result=0;
        for i in 0..=heights.len() {
            let mut current_height;

            if i == heights.len() {
                current_height = 0;
            } else {
                current_height = heights[i];
            }

            while !stack.is_empty()&& heights[*stack.last().unwrap()] > current_height
            {
                let index=stack.pop().unwrap();
                let height=heights[index];
                let width;
                if stack.is_empty() {
                    width = i;
                } else {
                    let left_index = *stack.last().unwrap();
                    width = i - left_index - 1;
                }
                let area =height * width as i32;
                if area > result {
                    result =area;
                }
            }
            stack.push(i);
        }
        result
    }
}