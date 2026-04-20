install.packages("ggplot2")
install.packages("readr")
library(ggplot2)
library(readr)

data <- data.frame(
  gender = c("female","male","female","male","female","male","female","male", "male"),
  math = c(95, 60, 78, 45, 88, 70, 92, 55, 90),
  reading = c(90, 58, 80, 50, 85, 72, 94, 60, 40),
  writing = c(88, 62, 79, 48, 87, 75, 91, 59, 80)
)

# SCATTER PLOT
ggplot(data, aes(math, reading, color=gender)) +
  geom_point(size=3) +
  ggtitle("Math vs Reading") +
  theme_minimal()

# HISTOGRAM 
ggplot(data, aes(math, fill=gender)) +
  geom_histogram(bins=5, alpha=0.7) +
  ggtitle("Math Score Distribution") +
  theme_minimal()

# BOX PLOT 
ggplot(data, aes(gender, math, fill=gender)) +
  geom_boxplot() +
  ggtitle("Gender vs Math Score") +
  theme_minimal()

# VIOLIN PLOT 
ggplot(data, aes(gender, writing, fill=gender)) +
  geom_violin() +
  ggtitle("Writing Score Distribution") +
  theme_minimal()

# BAR CHART
ggplot(data, aes(gender, fill=gender)) +
  geom_bar() +
  ggtitle("Gender Count") +
  theme_minimal()

# PIE CHART
g <- as.data.frame(table(data$gender))

ggplot(g, aes(x="", y=Freq, fill=Var1)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y") +
  ggtitle("Gender Distribution") +
  theme_minimal()

data <- read_csv("C:\\Users\\PRANJAL\\Documents\\StudentsPerformance.csv", show_col_types = FALSE)

# 1. SCATTER PLOT
ggplot(data, aes(x=`math score`, y=`reading score`)) +
  geom_point(color="blue") +
  ggtitle("Scatter Plot: Math vs Reading")

# 2. HISTOGRAM
ggplot(data, aes(x=`math score`)) +
  geom_histogram(fill="green", bins=10) +
  ggtitle("Histogram: Math Score")

# 3. BOX PLOT
ggplot(data, aes(x=gender, y=`math score`)) +
  geom_boxplot(fill="orange") +
  ggtitle("Box Plot: Gender vs Math Score")

# 4. VIOLIN PLOT
ggplot(data, aes(x=gender, y=`reading score`)) +
  geom_violin(fill="purple") +
  ggtitle("Violin Plot: Gender vs Reading Score")

# 5. BAR CHART
ggplot(data, aes(x=gender)) +
  geom_bar(fill="skyblue") +
  ggtitle("Bar Chart: Gender Distribution")

# 6. PIE CHART
gender_count <- as.data.frame(table(data$gender))

ggplot(gender_count, aes(x="", y=Freq, fill=Var1)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y") +
  ggtitle("Pie Chart: Gender Distribution")



#PLOTLY

install.packages("plotly")
install.packages("readr")

# Load libraries
library(plotly)
library(readr)

# 1. USER DEFINED DATA
data <- data.frame(
  gender = c("female","male","female","male","female","male","female","male","male"),
  math = c(95,60,78,45,88,70,92,55,90),
  reading = c(90,58,80,50,85,72,94,60,40),
  writing = c(88,62,79,48,87,75,91,59,80)
)

# SCATTER PLOT
plot_ly(data, x=~math, y=~reading, color=~gender,
        type="scatter", mode="markers")

# BAR CHART
g <- as.data.frame(table(data$gender))

plot_ly(g, x=~Var1, y=~Freq, type="bar", color=~Var1,
        text=~Freq, textposition="auto")

# PIE CHART
g <- as.data.frame(table(data$gender))
plot_ly(g, labels=~Var1, values=~Freq, type="pie")

# BUBBLE PLOT
plot_ly(data, x=~math, y=~reading, size=~writing,
        color=~gender, type="scatter", mode="markers")

# HISTOGRAM
plot_ly(data, x=~math, type="histogram")

# BOX PLOT
plot_ly(data, y=~math, color=~gender, type="box")


data <- read_csv("C:/Users/PRANJAL/Documents/StudentsPerformance.csv", show_col_types = FALSE)

# SCATTER
plot_ly(data, x=~`math score`, y=~`reading score`,
        type="scatter", mode="markers")

# HISTOGRAM
plot_ly(data, x=~`math score`, type="histogram")

# BOX
plot_ly(data, x=~gender, y=~`math score`, type="box")

# BAR
g2 <- as.data.frame(table(data$gender))
plot_ly(g2, x=~Var1, y=~Freq, type="bar",
        color=~Var1, text=~Freq, textposition="auto")

# PIE
g2 <- as.data.frame(table(data$gender))
plot_ly(g2, labels=~Var1, values=~Freq, type="pie")








