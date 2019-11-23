from flask import Flask, jsonify, g
import copy
app = Flask(__name__)

@app.before_request
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
        {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
        {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
        {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
        {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
    ]
    g.task_does_not_exist = {"msg":"task does not exist"}

@app.route('/api/tasks')
def get_all_tasks():
    return jsonify(g.data)

@app.route('/api/tasks/<int:task_id>')
def get_task(task_id):
    if task_id>0 and task_id<=len(g.data):
        return jsonify(g.data[task_id])

    else:
        return jsonify(g.task_does_not_exist)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    if task_id>0 and task_id<=len(g.data):
        tmp = copy.deepcopy(g.data[task_id])
        tmp['done'] = True
        return jsonify(tmp)
    else:
        return jsonify(g.task_does_not_exist)

if __name__ == '__main__':
    app.run()