from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')
    priority = db.Column(db.String(20), default='medium')

# Create DB
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Backend is running"

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201

# Get Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "priority": t.priority
        } for t in tasks
    ])

# Update Task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json

    task.status = data.get('status', task.status)
    task.priority = data.get('priority', task.priority)

    db.session.commit()

    return jsonify({"message": "Task updated"})

# Delete Task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)