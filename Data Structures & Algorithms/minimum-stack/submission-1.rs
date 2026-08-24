struct MinStack {
    stack: Vec<i32>,
}

impl MinStack {
    pub fn new() -> Self {
        MinStack {
            stack: Vec::new(),
        }
    }

    pub fn push(&mut self, val: i32) {
        self.stack.push(val);
    }

    pub fn pop(&mut self) {
        self.stack.pop();
    }

    pub fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    pub fn get_min(&self) -> i32 {
        *self.stack.iter().min().unwrap()
    }
}