import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Logging config (ONLY ONCE)
logging.basicConfig(
# filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()   # logs to docker logs
    ]
)

@app.route("/")
def home():
    return "Flask App Running"

#@app.route("/table/<int:number>")
#def table(number):
#    logging.info(f"Table requested for {number}")
#
#    result = [f"{number} x {i} = {number * i}" for i in range(1,11)]
#    
#    single_row = " | ".join(result)
#    return jsonify(single_row)
#    logging.info("Table generated successfully")
#return jsonify(result)

@app.route("/table/html/<int:number>")
def table_html(number):
    logging.info(f"Table requested for {number}")
    result = [f"{number} x {i} = {number*i}" for i in range(1, 11)]
    return "<br>".join(result)
    logging.info("Table generated successfully")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

