set.seed(1)
library(ggplot2)
library(dplyr)

df <- data.frame(age = runif(900, min = 10, max = 100),
                 group = rep(c("a", "b", "c", "d", "e", "f", "g", "h", "i"), 100))

tmp <- df %>%
  mutate(group = "ALL")

df <- rbind(df, tmp)

ggplot(df, aes(age)) + 
  geom_histogram(aes(y = (..count..)/sum(..count..)), binwidth = 5) + 
  scale_y_continuous(labels = percent ) + 
  facet_wrap(~ group, ncol = 5) 