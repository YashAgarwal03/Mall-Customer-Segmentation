import joblib

kmeans = joblib.load('C:\mall-customer-segmentation\deployement\kmeans_model.pkl')

def prediction(age,annual_income,spending_score):
    annual_income = annual_income-56.483871
    annual_income = annual_income/22.165770
    spending_score = spending_score-50.306452
    spending_score = spending_score/25.434126
    age = 1.15108644 if age > 40 else -0.86874449
    data = [age,annual_income,spending_score]
    predection = kmeans.predict([data])
    return predection


if __name__ == '__main__':
    result = prediction(19,15,39)
    print(result)