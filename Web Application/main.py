from fileinput import filename 
from flask import *  
from flask_cors import CORS

# ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)   
CORS(app)  # Enable CORS for all routes in the app


@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        string1 = request.form.get('studentId')
        string2 = request.form.get('courseNum')
        string3 = request.form.get('docText')

        # Process the received strings as needed
        print(string1)
        print(string2)
        print(string3)
        return 'Received strings: {}, {}, {}'.format(string1, string2, string3)
  
if __name__ == '__main__':   
    app.run(debug=True)