import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def main():
    # 1) CSV file load karna
    data = pd.read_csv("house_data.csv")
    print("Dataset:")
    print(data.head())

    # 2) Features (X) aur Target (y) alag karna
    X = data[["area", "bedrooms", "age"]]  # input
    y = data["price"]                      # output

    # 3) Train–Test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4) Linear Regression model banana & train karna
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5) Model ki performance dekhna
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print(f"\nModel R^2 Score: {score:.2f}")

    # 6) User se new house details leke prediction karna
    print("\n=== New House Price Prediction ===")
    area_val = float(input("Area in sq ft: "))
    bed_val = int(input("Number of bedrooms: "))
    age_val = int(input("Age of house (years): "))

    new_house = [[area_val, bed_val, age_val]]
    predicted_price = model.predict(new_house)[0]

    print(f"\nPredicted House Price: {predicted_price:.2f} Lakh Rupees")


if __name__ == "__main__":
    main()
