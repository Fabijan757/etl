import pandas as pd
from sqlalchemy import create_engine



engine = create_engine(
    "mysql+mysqlconnector://root:NovaLozinka@localhost:3306/shop_baza"
)

def ocisti_i_spremi(csv_putanja, ime_tablice):
    df = pd.read_csv(csv_putanja)
    df = df.drop_duplicates()
    df = df.dropna()
    df.to_sql(ime_tablice, engine, if_exists="replace", index=False)
    print(f"Spremljeno: {ime_tablice}, redova: {len(df)}")

def main():
    ocisti_i_spremi("customers.csv", "customers")
    ocisti_i_spremi("products.csv", "products")
    ocisti_i_spremi("sales.csv", "sales")

if __name__ == "__main__":
    main()
