import matplotlib.pyplot as plt

def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    salida = []
    salida.append(f"Diferencia: {diferencia}")
    salida.append(f"Error absoluto: {error_abs}")
    salida.append(f"Error relativo: {error_rel}")
    salida.append(f"Error porcentual: {error_pct}%")
    return diferencia, error_abs, error_rel, salida

valores = [
    (1.0000001, 1.0000000, 0.0000001),
    (1.000000000000001, 1.000000000000000, 0.000000000000001)
]

panel = []
resultados = []

for x, y, real in valores:
    panel.append(f"\nPara x={x}, y={y}:")
    diferencia, error_abs, error_rel, salida = calcular_errores(x, y, real)
    panel.extend(salida)
    resultados.append((x, y, diferencia, error_abs, error_rel))

panel.append("\n--- Análisis del impacto de la precisión numérica ---")
for i, (x, y, diferencia, error_abs, error_rel) in enumerate(resultados, 1):
    panel.append(f"Caso {i}: x={x}, y={y}")
    panel.append(f"  Diferencia obtenida: {diferencia}")
    panel.append(f"  Error absoluto: {error_abs}")
    panel.append(f"  Error relativo: {error_rel}")
    if error_abs == 0:
        panel.append("  → La precisión fue suficiente para representar correctamente la resta.")
    else:
        panel.append("  → Se observa pérdida de precisión debido a las limitaciones de punto flotante.")

# --- Mostrar en una pantalla aparte con matplotlib ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")  # ocultar ejes
texto = "\n".join(panel)
ax.text(0.01, 0.99, texto, va="top", ha="left", fontsize=10, wrap=True)

plt.title("Resultados del Ejercicio 3: Errores en operaciones numéricas", fontsize=12, weight="bold")
plt.show()

# --- Gráfica comparativa de errores ---
labels = ["Caso 1", "Caso 2"]
error_abs_values = [r[3] for r in resultados]

plt.bar(labels, error_abs_values, color=["skyblue", "salmon"])
plt.title("Comparación de Error Absoluto en cada caso")
plt.ylabel("Error absoluto")
plt.show()
