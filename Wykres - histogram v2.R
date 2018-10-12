#wyliczenie ile jest grup produktowych
rm(list = ls())
setwd("D:\\KK\\OneDrive\\Wroclaw w Liczbach\\Gotowe projekty\\20180930 Wybory samorzadowe 2018\\")

# Za³adowanie danych 
#require(xlsx) #do wczytania z Excela
#library(lubridate) # do operacji na datach
#library(plyr) #do join  
library(ggplot2) #do wykresów
library(scales) #do napisania osi jako %
library(dplyr) #do select distinct
library(tidyr) #do zmiany wide w long
library(extrafont) #do czcionek
library(stringr) #do wrap labels

loadfonts(device="win")

ALL_data = read.csv2("all_data.csv")

names(ALL_data)


SPR <- ALL_data %>%
  group_by(Komitet, Okreg) %>%
  summarise(n = n())

ALL_data_sort <- ALL_data %>%
  group_by(Komitet) %>%
  mutate(sr_wiek = mean(Wiek)) %>%
  ungroup() %>%
  arrange(sr_wiek, desc(Komitet))

#tmp1 <- ALL_data_sort 
tmp <- ALL_data_sort %>%
  mutate(Komitet = "Wszytkie komitety")

#for (i in c(1:11)) {
#  ALL_data_sort <- rbind(ALL_data_sort, tmp1)
#}

ALL_data_sort <- rbind(ALL_data_sort, tmp)
  
ALL_data_sort$Komitet_wr <- factor(stringr::str_wrap(ALL_data_sort$Komitet, 30),
                              levels = unique (stringr::str_wrap(ALL_data_sort$Komitet, 30)))


dummy_data <- ALL_data_sort %>%
  group_by(Komitet_wr) %>%
  summarise(sr_wiek = mean(Wiek))

#wykres

Theme <-  theme(legend.position="bottom",
                legend.key.width = unit(1,"cm"),
                legend.title = element_blank(),
                legend.background = element_rect(fill = "#f5f5f2", color = NA),
                legend.text       = element_text(family = "Ubuntu", size = 12, hjust = 0, color = "#22211d"),
                #axis.title   = element_text(family = "Ubuntu", size = 14, color = "#22211d"),
                #axis.title   = element_blank(),
                #axis.text.y  = element_blank(),
                #axis.ticks.y = element_blank(),
                
                #axis.ticks.x = element_text(family = "Ubuntu", size = 11, color = "#22211d"),
                text = element_text(family = "Ubuntu", size = 10, color = "#22211d"),
                axis.text.x  = element_text(family = "Ubuntu", size = 10, color = "#22211d"),
                axis.text.y  = element_text(family = "Ubuntu", size = 10, color = "#22211d"),
                strip.text.x = element_text(family = "Ubuntu", size = 12, color = "#22211d"),
                panel.grid.major = element_blank(),
                panel.grid.minor = element_blank(),
                plot.background  = element_rect(fill = "#f5f5f2",  color = NA), 
                panel.background = element_rect(fill = "#f5f5f2",  color = NA), 
                plot.title    = element_text(family = "Ubuntu", size = 21,  hjust = 0.5,  color = "#4e4d47"),
                plot.subtitle = element_text(family = "Ubuntu", size = 13,  hjust = 0.01,  face = "italic", color = "#4e4d47"),
                plot.caption  = element_text(family = "Ubuntu", size = 11,  hjust = 0.99, color = "#4e4d47"),
                panel.border = element_blank()
)  

p = 
  ggplot(ALL_data_sort, aes(Wiek)) + 
#  geom_histogram(aes(y = (..count..)/sum(..count..)), colour = "grey50", binwidth = 5) + 
  geom_histogram(aes(y = (..density.. * 5)), colour = "grey50", binwidth = 5) + 
  scale_y_continuous(labels = percent ) + 
  coord_cartesian(xlim = c(18, 80), expand = c(0, 0)) +
  facet_wrap(~ Komitet_wr, ncol = 4) + 
  geom_vline(data = dummy_data, aes(xintercept = sr_wiek), 
             colour = "#bd0026", linetype = 2) +
  geom_text(data = dummy_data, 
            mapping = aes(x = (18 + 80) / 2, y = 0.065 * 5, hjust = 0.5, 
                          label = paste0("Œredni wiek: ", round(sr_wiek, 0) )),
            family = "Ubuntu", angle = 0, colour = "#bd0026", size = 3.5,
            inherit.aes = FALSE ) +
  #geom_density(aes(y = ..density..* 600 / 11), colour = "#bd0026", fill =  "#bd0026", alpha = 0.1 ) +
  labs(title="\nRozk³ad wieku kandydatów w wyborach do Rady Miasta 2018",
       subtitle = paste0("Na podstawie danych dla 7 okrêgów wyborczych miasta Wroc³aw"),
       x = "Wiek", 
       y = "Procent kandydatów", 
       caption = "Autor: WroData | ród³o: wybory2018.pkw.gov.pl" ) +
    Theme

  

plot(p)
a = 9
png(filename = paste("W2 ", Sys.Date(), ".png", sep=""),
      bg="white", width = a * 1.5, height = a, units = 'in', res = 150)
  plot(p)
dev.off()





