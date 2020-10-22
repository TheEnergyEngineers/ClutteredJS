data <- data <- read.csv("aggregated_results.csv",header=TRUE)

par(mfrow=c(1,2))

hist(data$StdDev, xlab = "Standard Deviation per trial",  main = "Histogram")
boxplot(data$StdDev, main = "Boxplot", xlab = "energy consumption", ylab = "Standard Deviation per trial")
