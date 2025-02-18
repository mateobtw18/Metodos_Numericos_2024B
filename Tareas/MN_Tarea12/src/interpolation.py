import numpy as np
import matplotlib.pyplot as plt


def ajuste_polinomio(xs, ys, grado, tipo):
    coeficientes = np.polyfit(xs, ys, grado)
    polinomio = np.poly1d(coeficientes)
    ys_pred = polinomio(xs)
    mse = np.mean((ys - ys_pred) ** 2)

    # Crear la representación del polinomio como texto
    polinomio_texto = " + ".join(
        f"{coef:.3f}x^{grado - i}" if grado - i > 0 else f"{coef:.3f}"
        for i, coef in enumerate(coeficientes)
    )

    plt.scatter(xs, ys, label="Datos originales", color="blue")
    x_graf = np.linspace(min(xs), max(xs), 100)
    plt.plot(
        x_graf,
        polinomio(x_graf),
        label=f"Polinomio de {grado}º grado\n$ y = {polinomio_texto}$",
        color="red",
    )
    plt.title(f"Ajuste {tipo} por Mínimos Cuadrados\nMSE: {mse:.6f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

    return coeficientes


def ajuste_exponencial(xs, ys):
    log_ys = np.log(ys)

    coeficientes = np.polyfit(xs, log_ys, 1)
    a = coeficientes[0]
    B = coeficientes[1]
    b = np.exp(B)

    ys_pred = b * np.exp(a * xs)

    mse = np.mean((ys - ys_pred) ** 2)

    plt.scatter(xs, ys, color="blue", label="Datos originales")
    plt.plot(
        xs, ys_pred, color="red", label=f"Modelo ajustado: $y = {b:.3f}e^{{{a:.3f}x}}$"
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Ajuste Exponencial ($be^{{ax}}$) por Mínimos Cuadrados\nMSE: {mse:.6f}")
    plt.legend()
    plt.grid()
    plt.show()

    return a, b


def f_lineal_interpolate(a, b, x):
    return a * x + b
