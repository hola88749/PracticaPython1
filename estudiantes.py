def ingresar_datos():
    estudiantes = {}
    cantidad = int(input("¿Cuántos estudiantes quieres ingresar?: "))
    for _ in range(cantidad):
        nombre = input("Nombre del estudiante: ")
        calificaciones = list(map(float, input("Ingresa las calificaciones separadas por espacio: ").split()))
        estudiantes[nombre] = calificaciones
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, calificaciones in estudiantes.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedios[nombre] = promedio
    return promedios

def estudiante_destacado(promedios):
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_nombre, mejor_promedio):
    with open("resultados.txt", "w") as f:
        for nombre in estudiantes:
            f.write(f"{nombre}: {estudiantes[nombre]} -> Promedio: {promedios[nombre]:.2f}\n")
        f.write(f"\nEstudiante con mejor promedio: {mejor_nombre} -> {mejor_promedio:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor_nombre, mejor_promedio = estudiante_destacado(promedios)
    guardar_resultados(estudiantes, promedios, mejor_nombre, mejor_promedio)
    print("Datos guardados en resultados.txt")

if __name__ == "__main__":
    main()

