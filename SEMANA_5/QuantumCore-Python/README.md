# Quantum Core - Python

## Descripción

**Quantum Core** es un proyecto académico desarrollado para el núcleo **Fundamentos de Software** de la Fundación Universitaria CEIPA. Su propósito es construir progresivamente un sistema para el procesamiento de transacciones financieras aplicando buenas prácticas de desarrollo de software, programación orientada a objetos y control de versiones.

Durante las diferentes actividades del curso se incorporaron mejoras que fortalecen la calidad, mantenibilidad y escalabilidad de la solución, siguiendo una evolución incremental del proyecto.

---

## Objetivos del Proyecto

- Aplicar los fundamentos de Programación Orientada a Objetos (POO).
- Implementar encapsulamiento, herencia y polimorfismo.
- Aplicar los principios SOLID para mejorar el diseño del software.
- Implementar manejo robusto de excepciones mediante `try-except`.
- Incorporar persistencia de información utilizando JSON.
- Gestionar el código fuente mediante Git y GitHub.
- Construir una estructura organizada y profesional del proyecto.

---

## Tecnologías Utilizadas

- Python 3
- Git
- GitHub
- JSON
- Visual Studio Code

---

## Evolución del Proyecto

### Actividad 3 – Programación Orientada a Objetos

- Diseño de clases.
- Encapsulamiento mediante propiedades.
- Herencia.
- Polimorfismo.
- Creación de diferentes tipos de transacciones.

### Actividad 3 – Principios SOLID

Se analizaron las responsabilidades del sistema para aplicar:

- SRP (Single Responsibility Principle)
- OCP (Open/Closed Principle)

Se propuso una arquitectura más flexible y fácil de mantener.

### Actividad 4 – Manejo Robusto de Excepciones

Se implementó:

- Validación de datos.
- Captura de errores mediante try-except.
- Continuidad del procesamiento aun cuando existen registros inválidos.
- Mensajes descriptivos para facilitar la depuración.

### Actividad 4 – Persistencia con JSON

Se incorporó el proceso de:

- Serialización de objetos.
- Deserialización.
- Persistencia de información utilizando archivos JSON.

### Actividad 5 – Control de Versiones

Se configuró el proyecto utilizando:

- Git
- GitHub
- Commits
- Repositorio remoto
- Organización profesional del proyecto

---

## Estructura del Proyecto

```
QuantumCore-Python
│
├── src
│   ├── modelos
│   ├── servicios
│   ├── persistencia
│   ├── excepciones
│   └── main.py
│
├── data
│   ├── transacciones.txt
│   ├── transacciones_corruptas.txt
│   └── transacciones.json
│
├── docs
│   ├── Actividad_3_SOLID.pdf
│   ├── Semana_4_JSON.pdf
│   └── Actividad_5_Git_GitHub.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Flujo General del Sistema

```
Archivo de Transacciones
           │
           ▼
 Lectura de Datos
           │
           ▼
 Validación
           │
           ▼
 Creación de Objetos
           │
           ▼
 Procesamiento
           │
           ▼
 Manejo de Excepciones
           │
           ▼
 Persistencia JSON
           │
           ▼
 Reporte Final
```

---

## Competencias Desarrolladas

- Programación Orientada a Objetos.
- Diseño de software.
- Principios SOLID.
- Persistencia de datos.
- Manejo de excepciones.
- Serialización.
- Control de versiones.
- Organización profesional de proyectos.

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio.

```
git clone https://github.com/TU-USUARIO/QuantumCore-Python.git
```

2. Entrar al proyecto.

```
cd QuantumCore-Python
```

3. Ejecutar el programa.

```
python src/main.py
```

---

## Autor

**Guillermo León Ríos Franco**

Ingeniería de Sistemas

Fundación Universitaria CEIPA

2026

## Historial de Evolución

| Versión | Descripción |
|---------|-------------|
| v1.0 | Diseño inicial de las clases del sistema |
| v2.0 | Implementación de Programación Orientada a Objetos |
| v3.0 | Aplicación de los principios SOLID |
| v4.0 | Manejo robusto de excepciones |
| v5.0 | Persistencia mediante JSON |
| v6.0 | Organización del proyecto y control de versiones con Git y GitHub |