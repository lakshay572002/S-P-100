import numpy as np
import matplotlib.pyplot as plt

# Data Information
# save it in form of list
names= (['Apple Inc', 'Abbvie Inc', 'Abbott Laboratories', 'Accenture Plc', 'Allergan Plc', 'American International Group', 'Allstate Corp', 'Amgen', 'Amazon.Com Inc.', 'American Express Company', 'Boeing Company', 'Bank of America Corp', 'Biogen Inc', 'Bank of New York Mellon Corp', 'Blackrock', 'Bristol-Myers Squibb Company', 'Berkshire Hath Hld B', 'Citigroup Inc', 'Caterpillar Inc', 'Celgene Corp', 'Charter Communicatio', 'Colgate-Palmolive Company', 'Comcast Corp A', 'Capital One Financial Corp', 'Conocophillips', 'Costco Wholesale', 'Cisco Systems Inc', 'CVS Corp', 'Chevron Corp', 'Danaher Corp', 'Walt Disney Company', 'Duke Energy Corp', 'Dowdupont Inc.', 'Emerson Electric Company', 'Exelon Corp', 'Ford Motor Company', 'Facebook Inc', 'Fedex Corp', '21st Centry Fox Class B', '21st Centry Fox Class A', 'General Dynamics Corp', 'General Electric Company', 'Gilead Sciences Inc', 'General Motors Company', 'Alphabet Class C', 'Alphabet Class A', 'Goldman Sachs Group', 'Halliburton Company', 'Home Depot', 'Honeywell International Inc', 'International Business Machines', 'Intel Corp', 'Johnson & Johnson', 'JP Morgan Chase & Co', 'Kraft Heinz Co', 'Kinder Morgan', 'Coca-Cola Company', 'Eli Lilly and Company', 'Lockheed Martin Corp', "Lowe's Companies", 'Mastercard Inc', "McDonald's Corp", 'Mondelez Intl Cmn A', 'Medtronic Inc', 'Metlife Inc', '3M Company', 'Altria Group', 'Monsanto Company', 'Merck & Company', 'Morgan Stanley', 'Microsoft Corp', 'Nextera Energy', 'Nike Inc', 'Oracle Corp', 'Occidental Petroleum Corp', 'Priceline Group', 'Pepsico Inc', 'Pfizer Inc', 'Procter & Gamble Company', 'Philip Morris International Inc', 'Paypal Holdings', 'Qualcomm Inc', 'Raytheon Company', 'Starbucks Corp', 'Schlumberger N.V.', 'Southern Company', 'Simon Property Group', 'AT&T Inc', 'Target Corp', 'Time Warner Inc', 'Texas Instruments', 'Unitedhealth Group Inc', 'Union Pacific Corp', 'United Parcel Service', 'U.S. Bancorp', 'United Technologies Corp', 'Visa Inc', 'Verizon Communications Inc', 'Walgreens Boots Alliance', 'Wells Fargo & Company', 'Wal-Mart Stores', 'Exxon Mobil Corp'])
sectors = ['Information Technology', 'Health Care', 'Health Care', 'Information Technology', 'Health Care', 'Financials', 'Financials', 'Health Care', 'Consumer Discretionary', 'Financials', 'Industrials', 'Financials', 'Health Care', 'Financials', 'Financials', 'Health Care', 'Financials', 'Financials', 'Industrials', 'Health Care', 'Consumer Discretionary', 'Consumer Staples', 'Consumer Discretionary', 'Financials', 'Energy', 'Consumer Staples', 'Information Technology', 'Consumer Staples', 'Energy', 'Health Care', 'Consumer Discretionary', 'Utilities', 'Materials', 'Industrials', 'Utilities', 'Consumer Discretionary', 'Information Technology', 'Industrials', 'Consumer Discretionary', 'Consumer Discretionary', 'Industrials', 'Industrials', 'Health Care', 'Consumer Discretionary', 'Information Technology', 'Information Technology', 'Financials', 'Energy', 'Consumer Discretionary', 'Industrials', 'Information Technology', 'Information Technology', 'Health Care', 'Financials', 'Consumer Staples', 'Energy', 'Consumer Staples', 'Health Care', 'Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Financials', 'Industrials', 'Consumer Staples', 'Materials', 'Health Care', 'Financials', 'Information Technology', 'Utilities', 'Consumer Discretionary', 'Information Technology', 'Energy', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Consumer Staples', 'Consumer Staples', 'Information Technology', 'Information Technology', 'Industrials', 'Consumer Discretionary', 'Energy', 'Utilities', 'Real Estate', 'Telecommunications', 'Consumer Discretionary', 'Consumer Discretionary', 'Information Technology', 'Health Care', 'Industrials', 'Industrials', 'Financials', 'Industrials', 'Information Technology', 'Telecommunications', 'Consumer Staples', 'Financials', 'Consumer Staples', 'Energy']
prices= [170.12, 93.29, 55.28, 145.3, 171.81, 59.5, 100.5, 168.93, 1126.82, 93.92, 265.04, 26.7, 311.92, 52.73, 474.05, 60.48, 181.27, 71.87, 137.37, 102.88, 346.2, 72.16, 36.13, 88.26, 49.89, 171.22, 36.38, 70.18, 114.84, 93.45, 103.02, 88.61, 71.12, 60.14, 41.32, 12.11, 179.14, 217.75, 30.42, 31.14, 198.7, 17.91, 71.63, 44.74, 1018.48, 1034.09, 238.05, 41.57, 170.13, 148.04, 151.4, 44.88, 138.54, 98.58, 80.59, 17.04, 45.6, 82.97, 312.93, 81.43, 149.93, 167.01, 42.49, 79.52, 51.85, 232.49, 66.51, 118.19, 53.74, 49.06, 82.49, 155.7, 59.46, 48.97, 68.17, 1762.23, 115.5, 35.38, 88.33, 103.35, 76.55, 66.83, 184.22, 56.83, 61.53, 51.12, 159.25, 34.59, 57.77, 88.62, 98.59, 209.75, 115.58, 113.2, 51.88, 117.05, 110.27, 45.85, 70.25, 54.02, 96.08, 80.31]
eps=[9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79, 12.58, 3.94, 5.22, 9.75, 1.75, 21.59, 3.47, 21.55, 2.96, 6.29, 5.19, 5.55, 6.4, 1.61, 2.87, 2.02, 7.58, 0.02, 5.82, 2.17, 5.71, 3.57, 3.89, 5.7, 4.45, 3.66, 2.58, 2.48, 1.68, 5.19, 11.91, 1.92, 1.92, 10.07, 1.24, 9.58, 6.19, 29.87, 29.87, 19.2, 0.73, 6.96, 6.95, 13.66, 3.18, 7.14, 6.94, 3.56, 0.65, 1.89, 4.09, 12.72, 4.34, 4.31, 6.4, 2.05, 4.69, 5.2, 8.95, 3.16, 5.53, 3.89, 3.61, 3.38, 6.67, 2.35, 2.55, 0.35, 74.45, 5.12, 2.5, 3.98, 4.49, 1.4, 3.78, 7.56, 2.07, 1.29, 2.75, 6.05, 2.93, 4.93, 6.06, 4.06, 9.6, 5.66, 5.98, 3.37, 6.62, 3.48, 3.75, 5.1, 4.14, 4.36, 3.56]

# converting list into arrays

arrayprices=np.array(prices)
arrayeps=np.array(eps)

# calculate price to earning ratio
# formula = prices/ eps
# higher the PE higher will be growth expectation

PE=arrayprices/arrayeps

# get names of companies that work in information technology using boolean arrays
names_array=np.array(names)
sector_array=np.array(sectors)

boolean_array=sector_array=='Information Technology'
it_names=names_array[boolean_array]
it_pe=PE[boolean_array]


boolean_array=sector_array=='Consumer Staples'
cs_names=names_array[boolean_array]
cs_pe=PE[boolean_array]

# creating scatter graph comparing both it and cs


#plt.scatter(cs_names,cs_pe,color='red',label='CS')
#plt.scatter(it_names,it_pe,color='green',label='IT')
#plt.legend()

#plt.xlabel('NAMES')
#plt.ylabel('PE RATIO')
#plt.show()

# creating histogram
plt.hist(it_pe,bins=8)

plt.xlabel('PE ratio')
plt.ylabel('frequency')
#plt.show()

# finding outliers

outliers_price=it_pe[it_pe>50]
outlier_name=it_names[it_pe>50]

print(str(outlier_name),str(outliers_price))