cluttered = read.table("cluttered.csv", sep = ",", header = TRUE)
decluttered = read.table("decluttered.csv", sep = ",", header = TRUE)
combined = read.table("combined.csv", sep = ",", header = TRUE)
combined$cluttered = as.factor(combined$cluttered)

sink("summary.txt")
summary(cluttered$batterystats_Joule_calculated)
summary(decluttered$batterystats_Joule_calculated) 
sink()

#plotting
pdf("pl1.pdf", width = 9, height = 7)
plot(cluttered$batterystats_Joule_calculated,pch=4,col="blue",ylab = "Energy consumption (joules)");points(decluttered$batterystats_Joule_calculated, col="green");legend("topleft", c("decluttered","cluttered"),col=c("green","blue"),pch=c(1,4))
#frm this ew can already observe that the results are pretty close to each other
dev.off()
# create for cluttered and decluttered boxplots with joule used


pdf("pl2.pdf", width = 9, height = 7)
boxplot(decluttered$batterystats_Joule_calculated, cluttered$batterystats_Joule_calculated,
        names = c("Decluttered","Cluttered"),
        ylab = "Energy consumption (joules)",
        col = c("green","blue"))
dev.off()
#from this we can already see that the mean of cluttered is lower

# create for each page size a boxplot with joule used, maybe not that intersting if we have the next one
#plot(batterystats_Joule_calculated~size,data=combined)


#boxplot for each page size and treatment
pdf("pl3.pdf", width = 9, height = 7)
boxplot(batterystats_Joule_calculated~size*cluttered, data=combined,
        xlab = "Page size and treament (0=decluttered, 1=cluttered)",
        ylab = "Energy consumption (joules)", 
        main = "Energy consumption per page size and treatment",
        col = c("green","green","green","blue","blue","blue"))
dev.off()
# normal test
# shapiro.test(cluttered$batterystats_Joule_calculated) # it should be p > 0.05 thus not normal
# shapiro.test(decluttered$batterystats_Joule_calculated) # it should be p > 0.05 thus not normal



#simple two smaple t test
library(car)
difference = cluttered$batterystats_Joule_calculated - decluttered$batterystats_Joule_calculated
sink("normalitytest.txt")#describe that the data is paired and therefore we dont have to test whether the data is normal but that the difference has to be normal!!
shapiro.test(difference) #is normal
sink()
#however it is not robust for small sample so do a visual check too:
pdf("pl4.pdf", width = 9, height = 7)
qqPlot(difference, main = "QQ Plot of differenc between cluttered and decluttered") # from this we also find that it is approximately normal
dev.off()

sink("t-tests.txt")
t.test(cluttered$batterystats_Joule_calculated, decluttered$batterystats_Joule_calculated, paired = TRUE) 
#Without taking page size into account: the energy consumption of the decluttered pages are absolutely not smaller, p = 0.9362, its almost the significantly the opposite

#t test per size group, use different p  (not gonna matter tho),
t.test(cluttered$batterystats_Joule_calculated[cluttered$size=='S'], decluttered$batterystats_Joule_calculated[cluttered$size=='S'], paired = TRUE)
t.test(cluttered$batterystats_Joule_calculated[cluttered$size=='M'], decluttered$batterystats_Joule_calculated[cluttered$size=='M'], paired = TRUE)
t.test(cluttered$batterystats_Joule_calculated[cluttered$size=='L'], decluttered$batterystats_Joule_calculated[cluttered$size=='L'], paired = TRUE)

#two way anova with repeated measures
#res.aov2 <- aov(batterystats_Joule_calculated ~ cluttered + size, data = combined)
res.aov2 <- aov(batterystats_Joule_calculated ~ size + cluttered + Error(subject), data = combined)
summary(res.aov2)
# we dont find a significant difference in clutterd vs decluttered. But we do find it in size
sink()

