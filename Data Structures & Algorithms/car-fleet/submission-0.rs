impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut cars: Vec<(i32,i32)>= Vec::new();
        let mut stack: Vec<i32> = Vec::new();
        for i in 0..position.len(){
            let car = (position[i],speed[i]);
            cars.push(car);
        }
        cars.sort_by(|a, b| {b.0.cmp(&a.0)});
        //fleet is basically uhhh made by cars whos time which is (target-position)/speed time for say x which is the first elem (most val of position) uske time se less or same works, u keep pushing in the stack as long as time is same or less , when more time is encountered then we add one to asnwer and empty out the stack fully 
        let mut fleet=0;
        let mut last_times=0.0;
        
        for car in cars{
            let pos=car.0;
            let spe=car.1;
            let time = (target-pos) as f64 / spe as f64;
            if time>last_times{
                fleet+=1;
                last_times=time;
            }
        }
        fleet
    }

}
