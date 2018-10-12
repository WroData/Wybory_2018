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

JEDYNKI = read.csv2("Jedynki.csv")
JEDYNKI = JEDYNKI[, -1]

odzial_plc = JEDYNKI %>%
  group_by(Partia) %>%
  summarise(KOB = mean(Plec_bin),
            MEZ = 1 - KOB) %>%
  arrange(KOB, desc(Partia))

odzial_plc$Partia <- factor(stringr::str_wrap(odzial_plc$Partia), levels = stringr::str_wrap(odzial_plc$Partia))

odzial_plc_rsp = gather(odzial_plc, Plec, odsetek, - Partia)
srednia = 1 - mean(JEDYNKI$Plec_bin)




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
                axis.text.y  = element_text(family = "Ubuntu", size = 13, color = "#22211d"),
                panel.grid.major = element_blank(),
                panel.grid.minor = element_blank(),
                plot.background  = element_rect(fill = "#f5f5f2",  color = NA), 
                panel.background = element_rect(fill = "#f5f5f2",  color = NA), 
                plot.title    = element_text(family = "Ubuntu", size = 21,  hjust = 0.5,  color = "#4e4d47"),
                plot.subtitle = element_text(family = "Ubuntu", size = 13,  hjust = 0.01,  face = "italic", color = "#4e4d47"),
                plot.caption  = element_text(family = "Ubuntu", size = 11,  hjust = 0.99, color = "#4e4d47"),
                panel.border = element_blank()
                )  

stringr::str_wrap(odzial_plc_rsp$Partia, 30)


w <- 
  ggplot(data=odzial_plc_rsp, aes(x = stringr::str_wrap(Partia, 30), 
                                  y = odsetek, 
                                  fill = Plec)) +
    geom_bar(stat="identity") +
    coord_flip() + # Horizontal bar plot
    labs(title = paste0("Udzia³ p³ci wœród 'jedynek'/nw wyborach do Rady Miasta"),
         subtitle = paste0("Na podstawie danych dla 7 okrêgów wyborczych miasta Wroc³aw"),
         x = "",
         y = "",
         caption = "Autor: WroData | ród³o: wybory2018.pkw.gov.pl" ) +
    scale_fill_manual(
      values = c("#fe9929", "#d95f0e"),
      breaks = c("KOB",   "MEZ"),
      labels = c("Kobiet", "Me¿czyzn")) + 
  #  coord_cartesian(ylim = c(0,10)) + 
    geom_hline(yintercept = srednia, colour = "#bd0026", linetype = 2) + 
    geom_text(x = 5, y = srednia + 0.030 , hjust=0, 
              label=paste0("Œrednio kobiet: ", round((1 - srednia) * 100, 0), "%"),
              family = "Ubuntu", angle = 90, colour = "#fe9929") + 
    geom_text(x = 5, y = srednia - 0.030 , hjust=1, 
              label=paste0("Œrednio mê¿czyzn: ", round((srednia) * 100, 0), "%"),
              family = "Ubuntu", angle = -90, colour = "#bd0026") +
    scale_y_continuous(labels = percent, expand = c(0, 0)) +
    Theme


plot(w)

# wielkoœæ obrazka
a <- 9

png(filename = paste("W1 ", Sys.Date(), ".png", sep=""),
    bg="white", width = a * 1.161803, height = a, units = 'in', res = 150)
  plot(w)
dev.off()