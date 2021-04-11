from main import app, mongo
from bson.objectid import ObjectId
from flask import render_template, request, redirect, url_for

# route to the main page
@app.route('/') 
def home():
    commands = mongo.db.commands.find({})
    print(commands)
    return render_template('index.html',commands=commands)
    
# route to search a particular command using keywords
@app.route('/search')
def search():
    if not request.args.get('keyword') or 'keyword' not in request.args or not request.args:
        return redirect(url_for('home'))
    else:
        keyword = request.args.get('keyword')
        commands = mongo.db.commands.find({ '$or': [{'Description': {'$regex': keyword}}, {'Command': {'$regex': keyword}}] })
        return render_template('index.html',commands=commands)

# route to store the command 
@app.route('/saveCommand')
def store_command():
    mongo.db.commands.insert({'Description':request.args.get('description'), 'Command': request.args.get('command')})
    commands = mongo.db.commands.find({})
    return redirect(url_for('home'))

#  route to delete a specfic command
@app.route('/deleteCommand/<id>')
def delete_command(id):
    mongo.db.commands.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('home'))

