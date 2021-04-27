from flask import Flask, request
import json
import datetime
import redis
import os


redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()

rd = redis.StrictRedis(host=redis_ip, port=6379, db=11)



app = Flask(__name__)

# DONE get animals from the redis db FINE
def get_data():
    userdata = []
    for key in rd.keys():
        userdata.append(str(rd.hgetall(key)))
    return userdata

# DONE load data from json to db
@app.route('/animals/loaddata', methods=['GET'])
def load_data():
    with open('animals.json', 'r') as f:
        animals = json.load(f)
    for animal in animals:
        rd.hmset(animal['uid'], animal) # add to db
    return "success"

# DONE convert animal dict full of binary strings to one with regular strings
def bintoregular(anims):
    output = []
    for anim in anims:  # destring the animals
        animdict = eval(anim)  # turn into a dictionary per animal
        animdictdecode = {}
        for thing in animdict:  # convert binary to regular string
            animdictdecode[thing.decode('ascii')] = animdict[thing].decode('ascii') # convert each key:value to regular strings
        output.append(animdictdecode)
    return output

# information
@app.route('/', methods=['GET'])
def info():
    return "Hi! You have reached the front page of Gabrielle's Flask app.\n\nRoutes:\n\n/hello\nSays hello\n\n/hello/<name>\nPersonalized hello\n\n/animals\nAll animals\n\n/animals/<part>/<kind>\nAll animals with value <kind> of attribute <part>\n\n/animals/contains/<word>\nAll animals that contain a certain string\n\n/animals/count\nReturns count of animals\n\n/animals/uuid/<uuid>\nReturns the selected animal with a matching <uuid>\n\n/animals/avglegs\nReturns the average number of legs an animal has\n\n/animals/edit/<uuid>?<part>=<value>\nSelects the animal matching <uuid> and edits its <part> to <value>. <part> can be head, legs, body, arms, or tail\n\n/animals/dates/<date1>/<date2>\nReturns all animals created between or on the start <date1> and end <date2>\n\n/animals/delete/<date1>/<date2>\nDeletes all animals between or on <date1> and <date2>. Returns the uids of those deleted.\n\n/animals/loaddata\nLoads animals into the Redis DB from an animals.json file. Useful for initializing animals. Returns 'success' when completed.\n\n"


# hello world!
@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello world!\n"

# hello <name>!
@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return "Hello {}!\n".format(name)

# DONE all Moreau animals
@app.route('/animals', methods=['GET'])
def get_anims_all():
    anims = get_data()
    return json.dumps(bintoregular(anims)) # extract the string of list of animals

# DONE returns animals with value <kind> of attribute <part>
@app.route('/animals/<part>/<kind>', methods=['GET']) 
def get_anims_cust(part,kind):
    anims = get_data()

    output = []

    goodanims = bintoregular(anims) # convert to regular strings

    output = [x for x in goodanims if str(x[str(part)]) == str(kind)]
    return json.dumps(output)

# DONE returns animals with strings in head or body containing <word>
@app.route('/animals/contains/<word>', methods=['GET'])
def get_anims_word(word):
    anims = get_data()
    output = [x for x in bintoregular(anims) if ( word in x['head'] or word in x['body'] ) ]
    return json.dumps(output)

# DONE returns a count of the total number of animals
@app.route('/animals/count', methods=['GET'])
def count_anims():
    anims = get_data()
    return str(len(bintoregular(anims)))

# DONE returns a creature matching the UUID
@app.route('/animals/uuid/<id>', methods=['GET'])
def get_anim_tag(id):
    anims = get_data()
    output = [x for x in bintoregular(anims) if (x['uid'] == id) ]
    return json.dumps(output)

# DONE returns the average number of legs of all the animals
@app.route('/animals/avglegs', methods=['GET'])
def get_avglegs():
    anims = get_data()
    output = [ int(x['legs']) for x in bintoregular(anims) ] # create list of all legs
    output = sum(output)/len(output)
    return str(output)

# DONE finds the animal with that uuid and edits it according to the query parameters
@app.route('/animals/edit/<id>', methods=['GET'])
def edit_anim(id):
    arms = request.args.get('arms') # if the user queried a new value for arms, get it
    legs = request.args.get('legs')
    tail = request.args.get('tail')
    head = request.args.get('head')
    body = request.args.get('body')
    created_on = request.args.get('created_on')
    stuffdict = {'arms':arms, 'legs':legs, 'tail':tail, 'head':head, 'body':body, 'created_on':created_on}
    # now edit it those that don't have None (weren't assigned)
    for attrib in stuffdict: # change every relevant attribute
        # get the animal with that UUID
        if stuffdict[attrib] != None:
            # change the attribute for that one animal
            rd.hset(id, attrib, stuffdict[attrib])
    return json.dumps(bintoregular([str(rd.hgetall(id))]))

# DONE returns the animals created within a date range. user must provide dates in correct form
@app.route('/animals/dates/<date1>/<date2>', methods=['GET'])
def date_anim(date1, date2):
    anims = get_data()
    anims = bintoregular(anims)
    # create objects for start and end dates
    start_date_obj = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S.%f')
    end_date_obj = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S.%f')
    output = [] # will contain all the animals in the range
    for anim in anims: # loop through all animals
        animdate = datetime.datetime.strptime(anim['created_on'], '%Y-%m-%d %H:%M:%S.%f') # get animal creation date
        if animdate >= start_date_obj and animdate <= end_date_obj: # animal is in the range
            output.append(anim)
    return json.dumps(output)

# DONE delete animals within a date range. user must provide dates in YYYY-MM-DD form
@app.route('/animals/delete/<date1>/<date2>', methods=['GET'])
def delete_anims(date1, date2):
    anims = get_data()
    anims = bintoregular(anims)
    # create start and end dates
    start_date_obj = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S.%f')
    end_date_obj = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S.%f')
    destroyed = [] # seek and destroy
    for anim in anims:
        animdate = datetime.datetime.strptime(anim['created_on'], '%Y-%m-%d %H:%M:%S.%f') # get animal creation date
        if animdate >= start_date_obj and animdate <= end_date_obj: # animal is in the range
            # delete the animal
            deleteduid = anim['uid']
            destroyed.append(deleteduid)
            rd.hdel(deleteduid,*anim.keys())
    return json.dumps(destroyed) # return uids of all that were destroyed



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
