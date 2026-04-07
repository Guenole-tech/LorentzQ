# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:48:38 2026

@author: gueno
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class LorentzVisualizer:
    def __init__(self, steps):
        plt.style.use('dark_background')
        self.steps = steps
        self.fig, self.ax = plt.subplots(figsize=(12, 7))
        
        self.line_std, = self.ax.plot([], [], color='#ff4b4b', linestyle='--', label='STANDARD')
        self.line_lq, = self.ax.plot([], [], color='#00d1ff', linewidth=3, label='LORENTZQ')
        
        self.text_gain = self.ax.text(105, 0.55, '', fontsize=12, color='white', 
                                      bbox={'facecolor': '#333333', 'alpha': 0.8})
        self._setup_ax()

    def _setup_ax(self):
        self.ax.set_xlim(0, self.steps)
        self.ax.set_ylim(0.45, 1.05)
        self.ax.set_title("LorentzQ : Restauration de la Pureté", fontsize=16)
        self.ax.legend(loc='lower left')
        self.ax.grid(color='gray', linestyle='--', alpha=0.2)

    def update_frame(self, frame, simulator):
        gain = frame * 0.003
        f_std, f_lq = simulator.simulate_cycle(self.steps, gain)
        
        self.line_std.set_data(range(self.steps), f_std)
        self.line_lq.set_data(range(self.steps), f_lq)
        
        eff = ((f_lq[-1]-0.5)/0.5)*100
        self.text_gain.set_text(f"BOOST : {gain:.3f}\nEFFICACITÉ : {eff:.1f}%")
        
        return self.line_std, self.line_lq, self.text_gain

    def animate(self, simulator, frames=100):
        return FuncAnimation(self.fig, self.update_frame, fargs=(simulator,), 
                             frames=frames, interval=50, blit=True)