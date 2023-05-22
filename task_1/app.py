from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


tasks = []

@app.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect('/tasks')
    return render_template('create.html')

@app.route('/tasks')
def task_list():
    return render_template('tasks.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect('/tasks')


if __name__ == '__main__':
    app.run(debug=True)
