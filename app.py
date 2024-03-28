from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        "id" : 1,
        "title" : "Software Engineer",
        "location" : "Kuala Lumpur",
        "salary" : "MYR 10,000"
    },
    {
        "id" : 2,
        "title" : "Penetration Tester",
        "location" : "Los Angeles, California, USA",
        "salary" : "MYR 8,000"
    },
    {
        "id" : 3,
        "title" : "Software Tester",
        "location" : "Cyberjaya, Selangor",
        "salary" : "MYR 12,000"
    },
]

@app.route("/")
def hello():
    return render_template('index.html',
                           jobs=JOBS,
                           company_name="Jovial")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)