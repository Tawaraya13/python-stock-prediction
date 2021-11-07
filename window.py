import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import get as gt
import AI as ai
import numpy as np
matplotlib.use('TkAgg')

InputField = [
    [
        sg.Text("Input Company code"),
        sg.In(size=(5, 1), enable_events=True, key="-COMCODE-"),
        sg.OK(key="-OK1-"),
    ],
    [
        sg.Text("Input Cryptourrency"),
        sg.In(size=(5, 1), enable_events=True, key="-coin-"),
        sg.OK(key="-OK2-"),
    ]
]

CHARTCompany = [
    [sg.Text("Company Plot test")],
    [sg.Canvas(key="-COMPANYCANVAS-")],
]

CHARTPrediction = [
    [sg.Text("Prediction Plot test")],
    [sg.Canvas(key="-PREDICTIONCANVAS-")],
]

#Helper to draw plot
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

#delete figure
def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')

layout = [
    [
        sg.Column(InputField),
        sg.VSeperator(),
        sg.Column(CHARTCompany),
        sg.VSeperator(),
        sg.Column(CHARTPrediction)
    ]
]

# Create the window
window = sg.Window("Stock Predict v.01", layout, finalize=True)

fig_agg = None
fig_agg2 = None
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == "-OK1-" :
        COMCODE = values["-COMCODE-"]
        try:
            CompanyData = gt.getdataAlpha(COMCODE)
            predictData = ai.predict(CompanyData)
        except:
            print("fail to get data")
        try:
            CompanyPlot = gt.plotStockData(CompanyData)
            #predictData = ai.predict(CompanyData)
        except:
            print("fail to Plot data")
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        fig_agg = draw_figure(window['-COMPANYCANVAS-'].TKCanvas, CompanyData)
        fig_agg2 = draw_figure(window['-PREDICTIONCANVAS-'].TKCanvas, predictData)
    if event == "-OK2-" :
        COINCODE = values["-coin-"]
        try:
            COINData = gt.getcryptoAlpha(COINCODE)
        except:
            print("fail to get data")
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        fig_agg = draw_figure(window['-COMPANYCANVAS-'].TKCanvas, COINData)

window.close()

