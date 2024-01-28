file <- read.csv("businesses.csv")
uniqueType <- unique(file$type)
print(uniqueType)
typesToKeep <- c("Restaurant","Brasserie","Restaurant service rapide")
filtered_df <- file[file$type %in% typesToKeep, ]

statut <- unique(file$statut)
print(statut)
statutToKeep <- c("Ouvert","En traitement")
filtered_df <- filtered_df[filtered_df$statut %in% statutToKeep, ]

write.csv(filtered_df, "selected_business.csv", sep = ",")
