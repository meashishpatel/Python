import requests

def get_stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data:
        stock_data = data["data"]
        name = stock_data["Name"]
        price = stock_data["CurrentPrice"]
        return name, price
    else:
        raise Exception("Failed to get stock data")
    
def main():
    try:
        name, price = get_stocks()
        print(f"Stock: {name}, Price: {price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__": 
    main()