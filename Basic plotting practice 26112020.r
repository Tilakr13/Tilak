# Basic Plotting in R
# Data set used is Car.

cars
cars$speed
cars$dist

plot(cars$speed, cars$speed)
plot(cars$speed, cars$speed, xlab= "Speed", ylab= "Distance")
plot(cars$speed, cars$speed, xlab= "Speed", ylab= "Distance", main= "Cars speed and distance analysis")
