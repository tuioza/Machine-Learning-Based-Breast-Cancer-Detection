import pandas as pd 


def clean_data():
    data = pd.read_csv("data\data.csv")
    print(data.head())
    return data

def main():
    data = clean_data()
    return

if __name__ == '__main__':
    main()