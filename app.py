from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': "Learn Python",
        'description': 'Python is used for data science',
        'done': False
    },
    {
        'id': 2,
        'title': "Books",
        'description': 'Books are fun to read',
        'done': False 
    }
]

@app.route("/")


@app.route('/add-data', methods=["POST"])
def Add_Data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)
    task = {
        'id': tasks[-1]["id"] + 1,
        "title": request.json['title'],
        "description": request.json.get('description', ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })

@app.route("/get-data")
def Get_Task():
    return jsonify({
        "data": tasks
    })
    

if __name__ == '__main__':
    app.run()