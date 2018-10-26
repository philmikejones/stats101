library("tidyverse")

dat = 
  haven::read_sav("~/Downloads/CSEWWeek6.sav") %>% 
  mutate(age = as.integer(age))

summary(dat$age)
summary(dat$age[dat$bcsvictim == 1])
summary(dat$age[dat$bcsvictim == 0])
prop.table(table(dat$homealon))

dat$delibvio
table(dat$delibvio)

table(dat$sex[dat$delibvio < 8], dat$delibvio[dat$delibvio < 8]) %>% 
  chisq.test()

(561/20462) / (388/34617)

age_homealon <- cor.test(
  dat$homealon[!is.na(dat$age) & dat$homealon < 8],
  dat$age[!is.na(dat$age) & dat$homealon < 8],
  method = "kendall"
)

age_homealon


table(
  dat$inner[dat$homealon < 9],
  dat$homealon[dat$homealon < 9]
) %>% 
  chisq.test()
