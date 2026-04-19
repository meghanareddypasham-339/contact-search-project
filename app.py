from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

contacts = []

# Linear Search
def linear_search(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None


# Binary Search
def binary_search(name):
    sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())

    low, high = 0, len(sorted_contacts) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_contacts[mid]['name'].lower() == name.lower():
            return sorted_contacts[mid]

        elif sorted_contacts[mid]['name'].lower() < name.lower():
            low = mid + 1

        else:
            high = mid - 1

    return None


@app.route('/')
def home():
    return render_template('index.html')


# Add Contact
@app.route('/add', methods=['POST'])
def add_contact():
    data = request.json

    contacts.append({
        "name": data['name'],
        "phone": data['phone']
    })

    return jsonify({
        "message": "Contact added successfully!"
    })


# Search Contact
@app.route('/search', methods=['POST'])
def search():
    name = request.json['name']

    # Linear Search Time
    start = time.time()
    linear_result = linear_search(name)
    linear_time = time.time() - start

    # Binary Search Time
    start = time.time()
    binary_result = binary_search(name)
    binary_time = time.time() - start

    result = linear_result if linear_result else None

    faster = "Linear Search" if linear_time < binary_time else "Binary Search"

    return jsonify({
        "result": result,
        "linear_time": linear_time,
        "binary_time": binary_time,
        "faster": faster
    })


if __name__ == '__main__':
    app.run(debug=True)
