from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reminder", methods=["POST"])
def reminder():
    medicine = request.form.get("medicine")
    time = request.form.get("time")
    return f"Reminder set for {medicine} at {time}"

if __name__ == "__main__":
    app.run(debug=True)
    