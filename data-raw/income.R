library("tidyverse")

# Income
# set.seed() is for reproducibility so you get the same simulation
set.seed(42)

# qnorm() simulates data from a normal distribution
# The results are 0 < x < 1 so I multiply by a constant factor to better
# resemble incomes
dat = tibble(
  income = qnorm(seq(0, 1, 0.02), 2.73, 1) * 10000
) %>%
  # Get rid of the -Inf and Inf
  filter(income > 0, income < 100000)

saveRDS(dat, file = "data/dat.rds", compress = FALSE)
