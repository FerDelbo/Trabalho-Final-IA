# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier

# # Separar treino/teste
# X_train, X_test, y_train, y_test = train_test_split(
#     X, Y, test_size=0.5, stratify=Y, random_state=42
# )

# # Cria o KNN
# knn = KNeighborsClassifier(n_neighbors=3)

# knn.fit(X_train, y_train)
# accuracy = knn.score(X_test, y_test)

# print(f"Acurácia hold-out: {accuracy:.4f}")
-------------------------------------
# from sklearn.model_selection import GridSearchCV

# params = {'n_neighbors': [1, 3, 5, 7, 9]}
# gs = GridSearchCV(knn, params, cv=5)
# gs.fit(X, Y)

# print("Melhor valor de k:", gs.best_params_)
# print("Melhor score:", gs.best_score_)