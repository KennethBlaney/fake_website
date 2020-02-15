import random

from flask import render_template
from flask import Flask
from faker import Faker
fake = Faker()
app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/random_company', methods=['GET'])
def hello_person():
    co_name = fake.company()
    ceo_name = fake.name()
    fact_list = []
    if random.random() > .5:
        fact_list.append("CFO: {}".format(fake.name()))
    if random.random() > .5:
        fact_list.append("Address: {}".format(fake.address()))
    if random.random() > .5:
        fact_list.append("CTO: {}".format(fake.name()))
    if random.random() > .5:
        fact_list.append("Advisor: {}".format(fake.name()))
    if random.random() > .5:
        fact_list.append("Investment Round: {}".format(random.choice(["A", "B", "C", "Seed", "IPO", "Acquired"])))
    fact_list.append("Purpose: {} for {}".format(fake.catch_phrase(), fake.bs()))
    random.shuffle(fact_list)

    return render_template('index.html', company=co_name, ceo=ceo_name, facts=fact_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
