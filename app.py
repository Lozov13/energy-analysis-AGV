from flask import Flask, render_template
import plotly
import json

# Import analiz
from analysis.efektywnosc import analyze_efektywnosc
from analysis.tryby import analyze_tryby
from analysis.optymalizacja import analyze_optymalizacja
from analysis.bateria import analyze_bateria
from analysis.normy import analyze_normy

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/efektywnosc')
def efektywnosc():
    result = analyze_efektywnosc()
    plotly_json = json.dumps(result['fig'], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'efektywnosc.html',
        avg_energy=result['avg_energy'],
        total_energy_mWh=result['total_energy_mWh'],
        plotly_json=plotly_json
    )

@app.route('/tryby')
def tryby():
    result = analyze_tryby()
    plotly_json = json.dumps(result['fig'], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'tryby.html',
        avg_energies=result['avg_energies'],
        plotly_json=plotly_json
    )

@app.route('/optymalizacja')
def optymalizacja():
    result = analyze_optymalizacja()
    plotly_json = json.dumps(result['fig'], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'optymalizacja.html',
        avg_acc=result['avg_acc'],
        avg_cruise=result['avg_cruise'],
        plotly_json=plotly_json
    )

@app.route('/bateria')
def bateria():
    result = analyze_bateria()
    fig_voltage_json = json.dumps(result['fig_voltage'], cls=plotly.utils.PlotlyJSONEncoder)
    fig_soc_json = json.dumps(result['fig_soc'], cls=plotly.utils.PlotlyJSONEncoder) if result['fig_soc'] else None
    return render_template(
        'bateria.html',
        avg_voltage=result['avg_voltage'],
        min_voltage=result['min_voltage'],
        fig_voltage_json=fig_voltage_json,
        fig_soc_json=fig_soc_json
    )

@app.route('/normy')
def normy():
    params = analyze_normy()
    return render_template(
        'normy.html',
        params=params
    )

if __name__ == '__main__':
    app.run(debug=True)
