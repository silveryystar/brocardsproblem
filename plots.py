import matplotlib.pyplot as plt
import numpy as np
import math


def solution_plot(i_max, s_list):
    plt.scatter(range(0, i_max), s_list)
    plt.title("Solutions per i")
    plt.xlabel("i")
    plt.ylabel("Solutions")
    plt.show()


def fourier_plot(i_max, s_list):
    inverse_fourier = np.fft.ifft(s_list)
    plt.plot(range(0, i_max), inverse_fourier.real, color="blue", label="Real")
    plt.plot(range(0, i_max), inverse_fourier.imag, color="red", label="Complex")
    plt.legend()
    plt.title("Inverse Fourier Transform of Solutions per i")
    plt.xlabel("i (Time Domain)")
    plt.ylabel("Amplitude")
    plt.show()


def nim_plot(n_list, i_list, m_list):
    ax = plt.axes(projection='3d')

    i_list = [0] + [math.log10(i) for i in i_list if i != 0]
    m_list = [math.log10(i) for i in m_list]

    ax.scatter(n_list, i_list, m_list)
    plt.title("(n, i, m) Solutions")
    ax.set_xlabel("n")
    ax.set_ylabel("log(i)")
    ax.set_zlabel("log(m)")
    plt.show()


def get_plots(i_max, s_list, n_list, i_list, m_list):
    solution_plot(i_max, s_list)
    fourier_plot(i_max, s_list)
    nim_plot(n_list, i_list, m_list)
