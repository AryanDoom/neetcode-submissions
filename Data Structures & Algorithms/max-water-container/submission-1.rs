use std::cmp;

impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut j = heights.len() - 1;
        let mut max = 0;
        let mut i = 0;
        while i < j {
            let width = (j - i) as i32;
            let height =cmp::min(heights[j], heights[i]);
            let area =height * width;
            max = cmp::max(area, max);
            if heights[j] > heights[i] {
                i += 1;
            } else {
                j -= 1;
            }
        }

        max
    }
}