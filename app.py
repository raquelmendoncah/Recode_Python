from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):

            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            opc = request.form["opc"]

            if(opc == "soma"):
                return {"Resultado": str(num1 + num2)}
            if(opc == "subt"):
                return {"Resultado": str(num1 - num2)}
            if(opc == "mult"):
                return {"Resultado": str(num1 * num2)}
            if(opc == "divi"):
                return {"Resultado": str(num1 // num2)}
            if(opc == "expo"):
                return {"Resultado": str(num1 ** num2)}

        else:
            return "informe um valor valido"


@app.errorhandler(404)
def not_found(error):
    return "Erro 404 - Esta página não existe!"


app.run(port=3000, debug=True)
