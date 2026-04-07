# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:48:00 2026

@author: gueno
"""

import numpy as np
from scipy.linalg import expm

class QuantumSimulator:
    def __init__(self, taux_erreur=0.025):
        self.I = np.eye(2, dtype=complex)
        self.X = np.array([[0, 1], [1, 0]], dtype=complex)
        self.Z = np.array([[1, 0], [0, -1]], dtype=complex)
        self.taux_erreur = taux_erreur

    @staticmethod
    def calcul_purete(rho):
        return np.real(np.trace(rho @ rho))

    def simulate_cycle(self, steps, gain):
        rho_std = np.array([[1, 0], [0, 0]], dtype=complex)
        rho_lq = rho_std.copy()
        f_std, f_lq = [], []

        for _ in range(steps):
            # Évolution Standard (Décohérence)
            rho_std = (1 - self.taux_erreur) * rho_std + self.taux_erreur * (self.I / 2.0)
            rho_std /= np.trace(rho_std)

            # Évolution LorentzQ (Boost)
            rho_lq = (1 - self.taux_erreur) * rho_lq + self.taux_erreur * (self.I / 2.0)
            
            x3 = np.real(np.trace(rho_lq @ self.Z))
            x0 = np.real(np.trace(rho_lq @ self.I))
            s2 = x0**2 - x3**2

            if s2 > 0.0001:
                eta = np.arctanh(min(0.999, 1 - s2))
                boost = expm(eta * gain * self.Z)
                rho_lq = boost @ rho_lq @ boost.conj().T
                rho_lq /= np.trace(rho_lq)

            f_std.append(self.calcul_purete(rho_std))
            f_lq.append(self.calcul_purete(rho_lq))
            
        return f_std, f_lq