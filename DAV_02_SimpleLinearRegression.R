#User-defined dataset
X <- c(1, 2, 3, 4, 5)
y <- c(12, 19, 29, 37, 45)

#Create Data Frame
data <- data.frame(X, y)

#Create Linear Regression Model 
model <- lm(y ~ X, data=data)

#Calculate slope and intercept
intercept <- coef(model)[1]
slope <- coef(model)[2]

#Prediction for X=6
new_data <- data.frame(X=6)
y_new <- predict(model, new_data)

#print results
cat("Slope (m) : ", slope, "\n")
cat("Intercept (b) : ", intercept, "\n")
cat("Predicted value when X = 6 is ", y_new, " thousand.", "\n")

#plot
plot(X, y,
     main = "SIMPLE LINEAR REGRESSION",
     xlab = "YEAR",
     ylab = "EXPENDITURE IN THOUSANDS",
     pch = 16,
     xlim = c(1,8),
     ylim = c(12, 70))

#regression line 
abline(model, col = "blue")

#Prediction
points(6, y_new, pch = 16, col = "red")

#Display Linear regression equation on graph
text(7, 50, 
     labels = paste("y =", round(slope, 2), "X +", round(intercept, 2)),
     col = "darkgreen")




#output :
#Slope (m) :  8.4 Intercept (b) :  3.2 Predicted value when X = 6 is  53.6  thousand.
#SIMPLE LINEAR REGRESSION
# EXPENDITURE IN THOUSANDS (y)
# 70 |                                    
# 65 |                                    
# 60 |                                    
# 55 |                                ● (Predicted Point)
# 50 |                           ●
# 45 |                       ●
# 40 |                    ●
# 35 |                 ●
# 30 |              ●
# 25 |           ●
# 20 |        ●
# 15 |     ●
# 10 |____________________________________________
#      1    2    3    4    5    6    7    8
#                 YEAR (X)