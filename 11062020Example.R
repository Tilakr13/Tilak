Names=c('Arjun','Jessy','David','Joker')
Gender=c('M','F','M','M')
Age=c('32','40','21','45')
Example =data.frame(Names,Gender,Age)
Example

Example[1,1]
Example[2,3]
Example[1,]
Example[c(1,1),c(2,2)]
Example[,1]
Example[1,1]
Example[1,]
Example[2,2]
Example[,1]
Example[c(1,1),c(2,3)]
Example[1:2,]
Example[2,3]
Example[c(1,3),]
Example[(1,1),c(,2:3)]
Example[c(1,4),4]
Example[c(1,1),2]
df = c(Example[1,1],Example[2,3])
df
df = c(Example[4,1],Example[1,2])
df
