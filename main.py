import datetime
import os
import csv

def save_data_to_file(dict):
    print(dict)
    {'cr': 32.0, 'target': 40.0, 'unrealized_profit': '25.00%', 'date_time': '2024-07-12 23:16:47', 'comment': 'target 24 months', 'recomended_by': 'anil'}
    fieldnames = ['STOCK NAME', 'BUY PRICE', 'TARGET', 'EXPECTED PROFIT', 'DATE', 'COMMENT', 'RECOMMENDED BY' ]
    if os.path.isfile('data.csv') == False:

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'STOCK NAME':dict['stock_name'], 'BUY PRICE':dict['cr'], 'TARGET':dict['target'], 'EXPECTED PROFIT':dict['unrealized_profit'], 'DATE':dict['date_time'], 'COMMENT':dict['comment'], 'RECOMMENDED BY':dict['recomended_by']})
        return

    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'STOCK NAME':dict['stock_name'], 'BUY PRICE':dict['cr'], 'TARGET':dict['target'], 'EXPECTED PROFIT':dict['unrealized_profit'], 'DATE':dict['date_time'], 'COMMENT':dict['comment'], 'RECOMMENDED BY':dict['recomended_by']})


def date_time():
    dt  = datetime.datetime.now()  
    return dt.strftime ("%Y-%m-%d %H:%M:%S" )

def main(): 
    cr = float(input("CURRENT RATE: "))
    target = float(input("TARGET: "))
    diff=target-cr
    p=(diff*100)/cr 
    unrealized_profit = format(p,".2f")+"%"
    print("unrealized profit is: ", unrealized_profit)
    r = input("Do you want to save it: " )
    if r.lower() == 'y':
        stock_name=input("STOCK NAME?: ")
        comment=input("ANY COMMENT?: ")
        recomemded_by=input("RECOMMENDED BY?: ")
        dt = date_time()
        dict = {
            'cr':cr, 
            'target':target, 
            'unrealized_profit': unrealized_profit,
            'date_time':dt,
            'comment':comment,
            'recomended_by':recomemded_by,
            'stock_name': stock_name}
        save_data_to_file(dict)

while True:
    try: 
        main()
        c = input("DO YOU WANT TO CONTINUE(n/N): ")
        if(c.lower() == 'n'):
            break;
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")




