notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

def calcular_promedio(notas):
    return sum(notas) / len(notas)

promedios_estudiantes = {}
for estudiante, notas in notas_estudiantes.items():
    promedio = calcular_promedio(notas)
    promedios_estudiantes[estudiante] = promedio

for estudiante, promedio in promedios_estudiantes.items():
    print(f"{estudiante}: Promedio = {promedio:.2f}")