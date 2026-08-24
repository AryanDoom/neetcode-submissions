impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for brac in s.chars(){
            match brac{
                '[' | '{' | '(' => stack.push(brac),
                ']' => {if stack.pop() != Some('['){return false;}},
                '}' => {if stack.pop() != Some('{'){return false;}},
                ')' => {if stack.pop() != Some('('){return false;}},
                _ => return false,

            }
        }
        stack.is_empty()
        }
    }

