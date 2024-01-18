import pandas as pd


def get_suggested_funds(xlsx_file_path, fund_codes):
    df = pd.read_excel(xlsx_file_path)
    df.drop(df.columns[df.columns.str.startswith("Unnamed")], axis=1, inplace=True)

    numeric_columns = [
        "Return 1 Year",
        "Volatility 1 Year",
        "Return 3 Years",
        "Volatility 3 Years",
    ]
    df[numeric_columns] = df[numeric_columns].apply(
        lambda x: pd.to_numeric(x.astype(str).str.replace("%", ""), errors="coerce")
    )

    weights = {
        "Return 1 Year": 1,
        "Volatility 1 Year": -1,
        "Return 3 Years": 1,
        "Volatility 3 Years": -1,
    }

    df["Score"] = df[weights.keys()].dot(pd.Series(weights))
    df["Rank"] = df.groupby("Category")["Score"].rank(ascending=False)

    suggested_funds = {}

    for code in fund_codes:
        fund_data = df[df["Fund Code"] == code]
        if not fund_data.empty:
            category = fund_data["Category"].values[0]
            best_fund_in_category = (
                df[df["Category"] == category]
                .sort_values(by="Rank")
                .iloc[0]["Fund Code"]
            )
            suggested_funds[code] = best_fund_in_category

    return suggested_funds
