from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        location = request.form['location']
        skills = request.form['skills']
        # Save data or process further (e.g., save to a file or database)
        return f"Registered {name} from {location} with skills: {skills}"
    return render_template('register.html')

# Search route
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        location = request.form['location']
        # Perform search logic here
        return f"Search results for maids in {location}"
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=False)
