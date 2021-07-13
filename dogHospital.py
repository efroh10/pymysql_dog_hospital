import pymysql
from flask import Flask, request, render_template

app = Flask(__name__)

key = 0

db = pymysql.connect(
    host='freetrainer.cryiqqx3x1ub.us-west-2.rds.amazonaws.com',
    user='elijah',
    password='changeme'
)

cursor = db.cursor()


@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')


@app.route('/universal_search', methods=['POST'])
def universalSearch():
    term = request.form['term']
    name = request.form['name']
    sql = f"SELECT * FROM e_froh.{term}_table WHERE {term}_name = '{name}'"
    cursor.execute(sql)
    value = cursor.fetchall()
    return render_template('searchResults.html', value=value)


@app.route('/dog_search_results', methods=['POST'])
def dogSearchResults():
    term = request.form['term']
    dog = request.form['dog']
    sql = f"SELECT * FROM e_froh.dog_table WHERE dog_{term} = '{dog}'"
    cursor.execute(sql)
    value = cursor.fetchall()
    return render_template('searchResults.html', value=value)


@app.route('/add_dogtor', methods=['POST'])
def addDogtor():
    dogtor_title = request.form['title']
    dogtor_name = request.form['name']
    sql = f"""
        INSERT INTO e_froh.dogtor_table
            ( dogtor_title, dogtor_name )
        VALUES
            ('{dogtor_title}', '{dogtor_name}');
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('addition.html')
    except:
        db.rollback()
        return render_template('error.html')


@app.route('/add_dog', methods=['POST'])
def addDog():
    name = request.form['name']
    age = request.form['age']
    weight = request.form['weight']
    breed = request.form['breed']
    dogtor_id = request.form['dogtor_id']
    malady_id = request.form['malady_id']
    sql = f"""
        INSERT INTO e_froh.dog_table
            ( dog_name, dog_age, dog_weight, dog_breed, dogtor_id, malady_id )
        VALUES
            ('{name}', {age}, {weight}, '{breed}', {dogtor_id}, {malady_id});
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('addition.html')
    except:
        db.rollback()
        return render_template('error.html')


@app.route('/add_malady', methods=['POST'])
def addMalady():
    name = request.form['name']
    supply_id = request.form['supply_id']
    sql = f"""
        INSERT INTO e_froh.malady_table
            ( malady_name, supply_id )
        VALUES
            ('{name}', {supply_id});
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('addition.html')
    except:
        db.rollback()
        return render_template('error.html')


@app.route('/delete_item', methods=['POST'])
def deleteItem():
    term = request.form['term']
    name = request.form['name']
    sql = f"""
        DELETE FROM e_froh.{term}_table
        WHERE {term}_name = '{name}';
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('deletion.html')
    except:
        db.rollback()
        return render_template('error.html')


@app.route('/update_dogtor', methods=['POST'])
def updateDogtor():
    dogtor_id = request.form['id']
    title = request.form['title']
    name = request.form['name']
    sql = f"""
        UPDATE e_froh.dogtor_table
        SET dogtor_title = '{title}', dogtor_name = '{name}'
        WHERE dogtor_id = {dogtor_id};
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('update.html')
    except:
        db.rollback()
        return render_template('error.html')


@app.route('/update_dog', methods=['POST'])
def updateDog():
    dog_id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    weight = request.form['weight']
    breed = request.form['breed']
    dogtor_id = request.form['dogtor_id']
    malady_id = request.form['malady_id']
    sql = f"""
    UPDATE e_froh.dog_table
    SET
        dog_name = '{name}',
        dog_age = {age},
        dog_weight = {weight},
        dog_breed = '{breed}',
        dogtor_id = {dogtor_id},
        malady_id = {malady_id}
    WHERE dog_id = {dog_id};
    """
    try:
        cursor.execute(sql)
        db.commit()
        return render_template('update.html')
    except:
        db.rollback()
        return render_template('error.html')
