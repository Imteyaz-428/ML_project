from sklearn.base import BaseEstimator, TransformerMixin

class RealEstateFeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        X = X.copy()

        self.property_freq = X["Property Type"].value_counts()
        self.locality_freq = X["Locality"].value_counts()

        return self

    def transform(self, X):
        X = X.copy()

        X["Property_Type_freq"] = X["Property Type"].map(self.property_freq)
        X["Locality_freq"] = X["Locality"].map(self.locality_freq)

        X["BHK"] = X["Property Type"].str.extract(r'(\d+)').astype(float)

        X["Main_Type"] = X["Property Type"].str.extract(
            r'(Apartment|Floor|Plot|Villa|House|Penthouse)'
        )

        X.drop(["Property Type", "Locality"], axis=1, inplace=True)

        return X