import statistics
import math

data = [60,61,65,63,98,99,90,95,91,96]
mean = statistics.mean(data)

deviations = []
for i in data:
    deviation = i-mean
    deviations.append(deviation)

squares = []
for i in deviations:
    square = i * i
    squares.append(square)

sum = 0
for i in squares:
    sum = sum + i
print(sum)

length = len(deviations)
variance = sum/length
standardDeviation = math.sqrt(variance)
print(standardDeviation)

standardDeviation2 = statistics.stdev(data)
print(standardDeviation2)