import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def interactive_graph():
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(left=0.1, bottom=0.35)
    
    mInit = 2
    cInit = 3
    xMinInit = -10
    xMaxInit = 10
    yMinInit = -30
    yMaxInit = 30
    
    x = np.linspace(xMinInit, xMaxInit, 100)
    
    y = mInit * x + cInit
    
    line, = ax.plot(x, y, 'r-', label=f'y = {mInit}x + {cInit}')
    
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Demo of y=mx+c')
    ax.legend()
    
    ax.set_xlim(xMinInit, xMaxInit)
    ax.set_ylim(yMinInit, yMaxInit)
    
    axM = plt.axes([0.25, 0.25, 0.65, 0.03])
    axC = plt.axes([0.25, 0.20, 0.65, 0.03])
    axXRange = plt.axes([0.25, 0.15, 0.65, 0.03])
    axYRange = plt.axes([0.25, 0.10, 0.65, 0.03])
    
    sliderM = Slider(axM, 'Slope (m)', -10.0, 10.0, valinit=mInit, valstep=0.1)
    sliderC = Slider(axC, 'Y-intercept (c)', -50.0, 50.0, valinit=cInit, valstep=0.1)
    sliderXRange = Slider(axXRange, 'X Range', 5, 50, valinit=20, valstep=1)
    sliderYRange = Slider(axYRange, 'Y Range', 5, 100, valinit=60, valstep=5)
    
    def update(val):
        m = sliderM.val
        c = sliderC.val
        xRange = sliderXRange.val / 2
        yRange = sliderYRange.val / 2
        
        x = np.linspace(-xRange, xRange, 100)
        
        line.set_xdata(x)
        line.set_ydata(m * x + c)
        
        ax.set_xlim(-xRange, xRange)
        ax.set_ylim(-yRange, yRange)
        
        
        mDisplay = round(m, 1)
        cDisplay = round(c, 1)
        line.set_label(f'y = {mDisplay}x + {cDisplay}')
        
        ax.legend()
        fig.canvas.draw_idle()
    
    sliderM.on_changed(update)
    sliderC.on_changed(update)
    sliderXRange.on_changed(update)
    sliderYRange.on_changed(update)
    
    plt.show()

interactive_graph()
