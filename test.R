install.packages('palmerpenguins')
library('palmerpenguins')

installed.packages('ggplot2')
library('ggplot2')

ggplot(data=penguins, aes(x=flipper_length_mm, y=body_mess_g)) + geom_point()