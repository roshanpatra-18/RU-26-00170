import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    """Reads the CSV file, cleans invalid rows, and calculates revenue."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Make sure it's in the same folder.")
        return None

    # Ensure required columns exist
    required_cols = ['Order_ID', 'Product', 'Category', 'Quantity', 'Price']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Clean Quantity and Price columns: convert invalid strings/text to NaN
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Filter out rows where Quantity or Price is invalid, zero, or negative
    valid_mask = (df['Quantity'] > 0) & (df['Price'] >= 0)

    # Identify and log skipped/invalid rows
    invalid_rows = df[~valid_mask]
    for idx, row in invalid_rows.iterrows():
        print(f"Row {idx + 2} skipped: invalid data format or negative values.")

    # Keep only the clean, valid rows
    df = df[valid_mask].copy()

    # Calculate row-level revenue: Quantity * Price
    df['Revenue'] = df['Quantity'] * df['Price']

    return df

def show_summary(df):
    """Option 1: Display total revenue, orders, units sold, and top products."""
    if df is None or df.empty:
        print("No valid data available.")
        return

    total_revenue = df['Revenue'].sum()
    total_orders = df['Order_ID'].nunique()
    total_units = df['Quantity'].sum()

    # Product-wise aggregation using groupby()
    product_sales = df.groupby('Product').agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()
    top_product = product_sales.sort_values(by='Revenue', ascending=False).iloc[0]

    print("\n================ SUMMARY REPORT ================")
    print(f"Total Revenue: {total_revenue} | Orders: {total_orders}")
    print(f"Units sold: {int(total_units)} | Top product: {top_product['Product']} ({int(top_product['Revenue'])})")
    print("================================================\n")

    # Show top 5 selling products by revenue
    print("Top 5 Selling Products by Revenue:")
    top_5 = product_sales.sort_values(by='Revenue', ascending=False).head(5)
    print(top_5.to_string(index=False))

def show_category_analysis(df):
    """Option 2: Category-wise revenue, percentage breakdown, and Matplotlib charts."""
    if df is None or df.empty:
        print("No valid data available.")
        return

    total_revenue = df['Revenue'].sum()
    # Groupby category to find category-wise sales
    cat_sales = df.groupby('Category')['Revenue'].sum().reset_index()
    cat_sales['Percentage'] = (cat_sales['Revenue'] / total_revenue) * 100
    cat_sales = cat_sales.sort_values(by='Revenue', ascending=False)

    print("\n============= CATEGORY-WISE REVENUE =============")
    for _, row in cat_sales.iterrows():
        print(f"{row['Category']}: {int(row['Revenue'])} ({row['Percentage']:.2f}%)")
    print("================================================\n")

    # Colors: one per category, so it works with any number of categories
    palette = ['#4F46E5', '#3B82F6', '#60A5FA', '#93C5FD', '#A5B4FC', '#C7D2FE']
    colors = [palette[i % len(palette)] for i in range(len(cat_sales))]

    # Plot two Matplotlib charts (bar and pie) with titles and labels
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Bar Chart
    axes[0].bar(cat_sales['Category'], cat_sales['Revenue'], color=colors)
    axes[0].set_title('Category-wise Revenue (Bar Chart)')
    axes[0].set_xlabel('Category')
    axes[0].set_ylabel('Revenue')

    # Pie Chart
    axes[1].pie(cat_sales['Revenue'], labels=cat_sales['Category'],
                autopct='%1.2f%%', startangle=140, colors=colors)
    axes[1].set_title('Category Revenue Share (Pie Chart)')

    plt.tight_layout()
    print("Displaying Matplotlib charts...")
    plt.show()

def main():
    file_path = 'orders.csv'
    df = load_and_clean_data(file_path)
    if df is None:
        return

    while True:
        print("\n--- E-Commerce Sales Analyzer Menu ---")
        print("1. Summary (Total Revenue, Orders, Units, Top Product)")
        print("2. Category-wise Revenue & Charts")
        print("3. Exit")

        choice = input("Enter your menu option (1/2/3): ").strip()

        if choice == '1':
            show_summary(df)
        elif choice == '2':
            show_category_analysis(df)
        elif choice == '3':
            print("Exiting program. Good luck!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()