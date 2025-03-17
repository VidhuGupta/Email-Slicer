from flask import Flask, request, jsonify

app = Flask(__name__)

def email_slicer(email):
    """Extracts the username and domain from an email address."""
    at_index = email.find('@')
    if at_index == -1:
        return None, None  # Invalid email format

    local_part = email[:at_index]
    domain = email[at_index + 1:]
    return local_part, domain

@app.route('/slice', methods=['POST'])
def slice_email():
    try:
        data = request.get_json()
        email = data.get("email", "").strip()
        if not email:
            return jsonify({"error": "Email is required"}), 400

        local_part, domain = email_slicer(email)
        if local_part is None:
            return jsonify({"error": "Invalid email format"}), 400

        return jsonify({"username": local_part, "domain": domain})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Welcome to the Email Slicer API! Use the /slice endpoint."

if __name__ == '__main__':
    app.run(debug=True)
