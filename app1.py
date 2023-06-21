from flask import Flask, render_template, request
import math

def calculate_p0(rho):
    summation = sum([(2*rho)**m/math.factorial(m)for m in range (2)])
    p0= 1/(summation + ((2*rho)**2/math.factorial(2))*(1-rho))
    return p0

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tab='mm2')

@app.route('/mm2', methods=['GET', 'POST'])
def mm2():
    if request.method == 'POST':
        arrival_rate = float(request.form['arrival_rate'])
        service_rate = float(request.form['service_rate'])
        
        utilization = arrival_rate / service_rate
        p0 = 1 / (1 + utilization)
        lq = utilization**2 / (1 - utilization)
        wq = lq / arrival_rate
        w = wq + (1/ service_rate)
        l = arrival_rate * w
        
        results = {
            'Utilization': utilization,
            'Probability of zero customers': p0,
            'Average number of customers in the system': l,
            'Average number of customers in the queue': lq,
            'Average waiting time in the system': w,
            'Average waiting time in the queue': wq
        }

        return render_template('index.html', tab='mm2', results=results)

    return render_template('index.html', tab='mm2')

@app.route('/mg2', methods=['GET', 'POST'])
def mg2():
    if request.method == 'POST':
        arrival_rate = float(request.form['arrival_rate'])
        mean_service_time = float(request.form['mean_service_time'])
        variance_service_time = float(request.form['variance_service_time'])
        
        utilization = arrival_rate/(2*mean_service_time)
        p0 = calculate_p0(utilization)
        lq = (p0*utilization*(arrival_rate/mean_service_time)**2)/(2*(1-utilization)**2)
        wq = lq / arrival_rate
        w = wq +(1/mean_service_time)
        l = arrival_rate * w
        
        results = {
            'Utilization': utilization,
            'Probability of zero customers': p0,
            'Average number of customers in the system': l,
            'Average number of customers in the queue': lq,
            'Average waiting time in the system': w,
            'Average waiting time in the queue': wq
        }

        return render_template('index.html', tab='mg2', results=results)

    return render_template('index.html', tab='mg2')

@app.route('/gg2', methods=['GET', 'POST'])
def gg2():
    if request.method == 'POST':
        arrival_rate = float(request.form['arrival_rate'])
        service_rate = float(request.form['service_rate'])
        var_arrival_time = float(request.form['var_arrival_time'])
        var_service_time = float(request.form['var_service_time'])

        utilization = arrival_rate / service_rate
        p0 = calculate_p0(utilization)
        lq = utilization**2 * (var_arrival_time + var_service_time) / (2 * service_rate**2 * (1 - utilization)**2)
        wq = lq / arrival_rate
        w = wq + (1 / service_rate)
        l = arrival_rate * w

        results = {
            'Utilization': utilization,
            'Probability of zero customers': p0,
            'Average number of customers in the system': l,
            'Average number of customers in the queue': lq,
            'Average waiting time in the system': w,
            'Average waiting time in the queue': wq
        }

        return render_template('index.html', tab='gg2', results=results)

    return render_template('index.html', tab='gg2')

if __name__ == '__main__':
    app.run(debug=True)
