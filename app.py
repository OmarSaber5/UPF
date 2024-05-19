from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary containing directions based on the current location
directions = {
    "green hall": {
        "yellow hall": "Walk  straight east to reach 'yellow hall'.",
        "Main restaurant": "Walk south to reach 'Main restaurant'.",
        "red hall": "Walk south to reach 'red hall'.",
        "library": "Walk south to reach 'library'.",
        "CEO": "Walk south to reach 'CEO'.",
        "Student Affairs": "Walk south to reach 'Student Affairs'.",
        "Gate": "Walk south to reach 'Gate'."
    },
    "yellow hall": {
        "green hall": "Walk south to reach 'green hall'.",
        "Main restaurant": "Walk south to reach 'Main restaurant'."
    },
    "Main restaurant": {
        "yellow hall": "Walk north to reach 'yellow hall'.",
        "green hall": "Walk north to reach 'green hall'.",
        "red hall": "Walk south to reach 'red hall'.",
        "library": "Walk south to reach 'library'.",
        "CEO": "Walk south to reach 'CEO'.",
        "Student Affairs": "Walk south to reach 'Student Affairs'.",
        "Gate": "Walk south to reach 'Gate'."
    },
    "red hall": {
        "Main restaurant": "Walk north to reach 'Main restaurant'.",
        "library": "Walk east to reach 'library'.",
        "CEO": "Walk east then north to reach 'CEO'.",
        "Student Affairs": "Walk east to reach 'Student Affairs'.",
        "Gate": "Walk east then south to reach 'Gate'."
    },
    "library": {
        "Main restaurant": "Walk north to reach 'Main restaurant'.",
        "red hall": "Walk west to reach 'red hall'.",
        "CEO": "Walk north to reach 'CEO'.",
        "Student Affairs": "Walk east to reach 'Student Affairs'.",
        "Gate": "Walk south to reach 'Gate'."
    },
    "CEO": {
        "Main restaurant": "Walk south to reach 'Main restaurant'.",
        "red hall": "Walk south then west to reach 'red hall'.",
        "library": "Walk south to reach 'library'.",
        "Student Affairs": "Walk east to reach 'Student Affairs'.",
        "Gate": "Walk south to reach 'Gate'."
    },
    "Student Affairs": {
        "Main restaurant": "Walk south to reach 'Main restaurant'.",
        "red hall": "Walk west to reach 'red hall'.",
        "library": "Walk west to reach 'library'.",
        "CEO": "Walk west then north to reach 'CEO'.",
        "Gate": "Walk south to reach 'Gate'."
    },
    "Gate": {
        "green hall": "Walk north to reach 'green hall'.",
        "yellow hall": "Walk north to reach 'yellow hall'.",
        "Main restaurant": "Walk north to reach 'Main restaurant'.",
        "red hall": "Walk north then west to reach 'red hall'.",
        "library": "Walk north to reach 'library'.",
        "CEO": "Walk north to reach 'CEO'.",
        "Student Affairs": "Walk north to reach 'Student Affairs'."
    }
}

@app.route('/')
def index():
    return render_template('index.html', places=directions.keys())

@app.route('/find', methods=['POST'])
def find():
    current_place = request.form['current_place']
    target_place = request.form['target_place']
    if current_place in directions and target_place in directions[current_place]:
        direction = directions[current_place][target_place]
        return f'To get from "{current_place}" to "{target_place}": {direction}'
    else:
        return 'Sorry, no directions found for this route.'

if __name__ == '__main__':
    app.run(debug=True)
