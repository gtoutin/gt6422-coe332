from flask import Flask
import json


app = Flask(__name__)


def get_data():
    with open("animals.json", "r") as json_file:
        userdata1 = json.load(json_file)
    return userdata1


# information
@app.route('/', methods=['GET'])
def info():
    return "Hi! You have reached the front page of Gabrielle's Flask app.\n\nRoutes:\n\n/hello\nSays hello\n\n/hello/<name>\nPersonalized hello\n\n/animals\nAll animals\n\n/animals/<part>/<kind>\nAll animals with value <kind> of attribute <part>\n\n/animals/contains/<word>\nAll animals that contain a certain string\n\nBe kind to pigeons.\n\n"


# hello world!
@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello world!\n"

# hello <name>!
@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return "Hello {}!\n".format(name)

# all Moreau animals
@app.route('/animals', methods=['GET'])
def get_anims_all():
    anims = get_data()
    return json.dumps(anims['animals']) # extract the string of list of animals

# returns animals with value <kind> of attribute <part>
@app.route('/animals/<part>/<kind>', methods=['GET']) 
def get_anims_cust(part,kind):
    anims = get_data()
    anims = anims['animals']
    output = [x for x in anims if str(x[part]) == kind]
    return json.dumps(output)

# returns animals with strings in head or body containing <word>
@app.route('/animals/contains/<word>', methods=['GET'])
def get_anims_word(word):
    anims = get_data()
    anims = anims['animals']
    output = [x for x in anims if ( word in x['head'] or word in x['body'] ) ]
    return json.dumps(output)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
