#Y = a + b1*X1 + b2*X2
#Step 1 : Input Data
X1 <- c(1, 2, 3) #size
X2 <- c(3, 4, 7) #bedroom
Y <- c(2, 5, 9) #Price

#Step 2: Create Data Frame
data <- data.frame(X1, X2, Y)

#Step 3 : Fit Regression Model
model <- lm(Y ~ X1 + X2, data = data)

#Step 4 : Extract Coefficients
a <- coef(model)[1]
b1 <- coef(model)[2]
b2 <- coef(model)[3]

#Step 5 : Display Coefficients
cat("Intercept (a) = ", a, "\n")
cat("Coefficient of Regression b1 = ", b1, "\n")
cat("Coefficient of Regression b2 = ", b2, "\n\n")

#Step 6 : Display Regression Equation
cat("Y = ", round(a, 3), "+ ", round(b1,3),"* X1 + ", round(b2, 3),"* X2\n\n")
#Step 7 : Prediction using equation
X1_new <- 1.5
X2_new <- 3
Y_pred <- a + b1*X1_new + b2*X2_new

#Step 8 : Display Predicted Value
cat("Predicted Price (Y) =", round(Y_pred, 3), " Crores\n")

#Output:
#Intercept (a) =  -2  Coefficient of Regression b1 =  2.5 Coefficient of Regression b2 =  0.5 
# Y =  -2 +  2.5 * X1 +  0.5 * X2 Predicted Price (Y) = 3.25  Crores