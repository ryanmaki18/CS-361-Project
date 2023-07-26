import requests

def run():
    url = "http://127.0.0.1:5000/get_ratios"

    data = {
        "returns": [0.01, 0.02, -0.01, 0.03, -0.02],
        "risk_free_rate": 0.001,
        "beta": 1.2,
        "max_drawdown": 0.2
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        ratios = response.json()
        print("Sharpe Ratio:", ratios["sharpe_ratio"])
        print("Treynor Ratio:", ratios["treynor_ratio"])
        print("Calmar Ratio:", ratios["calmar_ratio"])
    else:
        print("Error: ", response.status_code)
    
if __name__ == "__main__":
    run()