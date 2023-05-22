{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from scipy.stats import beta\
import numpy as np\
from math import lgamma\
import matplotlib.pyplot as plt\
\
\
def f(a, b, c, d):\
    num = lgamma(a + c) + lgamma(b + d) + lgamma(a + b) + lgamma(c + d)\
    den = lgamma(a) + lgamma(b) + lgamma(c) + lgamma(d) + lgamma(a + b + c + d)\
    return np.exp(num - den)\
\
\
def f_iter(a, b, c, d):\
    while d > 1:\
        d -= 1\
        yield f(a, b, c, d) / d\
        \
        \
def g0(a, b, c):    \
    return np.exp(lgamma(a + b) + lgamma(a + c) - (lgamma(a + b + c) + lgamma(a)))\
\
def g(a, b, c, d):\
    return g0(a, b, c) + sum(f_iter(a, b, c, d))\
\
\
\
def calc_prob(beta1, beta2):\
    return g(beta1.args[0], beta1.args[1], beta2.args[0], beta2.args[1])\
    \
    \
\
def pico(a, b):\
    return (a-1)/(a+b-2)\
\
\
\
def plot(betas, names, linf=0, lsup=0.006):\
    x=np.linspace(linf, lsup, 100)\
    for f, n in zip(betas, names):\
        y=f.pdf(x)\
        y_pico=pico(f.args[0], f.args[1])\
        y_var=f.var()\
        plt.plot(x, y, label='\{\}, tasa de conv: \{:.6f\} $\\pm$ \{:.10f\}'.format(n, y_pico, y_var))\
        plt.yticks([])\
    plt.legend()\
    plt.show();}