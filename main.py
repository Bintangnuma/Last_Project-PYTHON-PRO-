# Impor
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, areas, vehicles):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    home_coef = 50
    area_coef = 3
    vehicle_coef = 1
    return size * home_coef + areas * area_coef + vehicles * vehicle_coef 

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                            'area.html', 
                            size=size
                           )

# Halaman ketiga
@app.route('/<size>/<areas>')
def electronics(size, areas):
    return render_template(
                            'vehicle.html',                           
                            size = size, 
                            areas = areas                          
                           )           
                           

# Perhitungan
@app.route('/<size>/<areas>/<vehicles>')
def end(size, areas, vehicles):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(areas), 
                                                    int(vehicles)
                                                    )
                          )

# Formulir
@app.route('/form')
def form():
    return render_template('form.html')

#Hasil formulir
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendeklarasikan variabel untuk pengumpulan data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Anda dapat menyimpan data Anda dan mengirimkannya melalui email
    with open('form.txt', 'a',) as f:
        f.write(name + '\n')
        f.write(email + '\n')
        f.write(address + '\n')
        f.write(date + '\n')
    return render_template('form_result.html', 
                           # Tempatkan variabel di sini
                           name=name,
                           email=email,
                           address=address,
                           date=date
                           )

app.run(debug=True)