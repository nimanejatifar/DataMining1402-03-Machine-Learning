cross_validation = KFold(n_splits=3)
cross_val_score(classifier, iris.data, iris.target, cv=cross_validation)