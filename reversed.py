from flask import Flask ,request , render_template

app = Flask(__name__, template_folder= 'template')

@app.route("/" , methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text=request.form.get('text')

        chars = list(text)
        reversed_chars = []

        for i in range(len(chars)-1, -1, -1):
            reversed_chars.append(chars[i])

        reversed_text = "".join(reversed_chars)

        return reversed_text   

if __name__ == '__main__':
    app.run(debug=True)
