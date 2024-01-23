from flask import Flask, request, render_template

app = Flask(__name__)

# Define a route to display the contact form
@app.route('/')
def contact_form():
    return render_template('contact_form.html')

# Define a route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a string to represent the submitted data
        submitted_data = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"

        try:
            # Write the data to a text file in sequential order
            with open('submitted_responses.txt', 'a') as file:
                file.write(submitted_data + '\n')
        except Exception as e:
            return f"Error: {str(e)}"

        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
