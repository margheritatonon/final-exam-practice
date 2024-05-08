import luigi
import pandas as pd

class ReadCSVFile(luigi.Task):
    """Task to read the CSV file into a Pandas DataFrame."""
    def output(self):
        return luigi.LocalTarget('sales.csv')

    def run(self):
        df = pd.read_csv('sales.csv')
        df.to_csv(self.output().path, index=False)

class CalculateTotalSales(luigi.Task):
    """Task to calculate the total sales for each product."""
    def requires(self):
        return ReadCSVFile()

    def output(self):
        return luigi.LocalTarget('total_sales.csv')

    def run(self):
        df = pd.read_csv(self.input().path)
        df['TotalSales'] = df['UnitPrice'] * df['Quantity']
        df.to_csv(self.output().path, index=False)

## TODO Implement the following new task to filter sales above 1000:

class FilterHighSalesProducts(luigi.Task):
    """Task to filter the data for products with total sales greater than 100."""
    def requires(self):
        return CalculateTotalSales()

    def output(self):
        # TODO make it produce an output called ‘high_sales_products.csv'
        return luigi.LocalTarget("high_sales_products.csv")

    def run(self):
        df = pd.read_csv(self.input().path)
        ## TODO ##
        dfmodified = df[df["TotalSales"] > 100]
        dfmodified.to_csv(self.output().path, index=False)

if __name__ == '__main__':
    luigi.build([CalculateTotalSales(), FilterHighSalesProducts()], local_scheduler=True)
