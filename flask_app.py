from flask import Flask, render_template, request
import pickle


model = pickle.load(open('trained_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def Energy():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        temperature = float(request.form.get('temperature'))
        humidity = float(request.form.get('humidity'))
        squarefootage = float(request.form.get('squarefootage'))
        occupancy = int(request.form.get('occupancy'))
        hvacusage = int(request.form.get('hvacusage'))
        lightingusage = int(request.form.get('lightingusage'))
        renewableenergy = float(request.form.get('renewableenergy'))
        dayofweek = int(request.form.get('dayofweek'))
        holiday = int(request.form.get('holiday'))

        energyc_arr = model.predict([[temperature , humidity , squarefootage , occupancy , hvacusage , lightingusage , renewableenergy , dayofweek , holiday  ]])
        energy = energyc_arr[0]
        return render_template('result.html' , energy_value= energy)


if __name__ == '__main__':
    app.run(debug=True)
