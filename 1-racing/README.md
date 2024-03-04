# Racing

In order to compete at the race the team should hire a pilot and a race car

Description
-
The race consists of two laps. Each lap time depends on several factors:
 - Driver's skill (`noob`/`avg-`/`avg`/`avg+`/`pro`)
 - Tire compound (`kF`)
 - Weight and power of the car (`W`, `hp`)

Final formula for the lap time: `t = kF * hp / W + sF`, where `sF` is determined by the driver's skill using table:
 - `noob => +0.5`
 - `avg- => +0.0` 
 - `avg => -0.1`. 
 - `avg+ => -0.5` 
 - `pro => -0.85`

Output
-
Result of the race is determined by total time of the two laps.
Your code should administrate the race, determine it's winners
and print results to the console in a form of table.
