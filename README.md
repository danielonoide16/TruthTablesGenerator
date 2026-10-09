# Truth Tables Generator

Aplicación de escritorio en Python para practicar lógica proposicional de forma interactiva.
El proyecto combina un **generador de expresiones lógicas** con un **minijuego de deducción**, usando una interfaz gráfica simple con Tkinter.

## 🎯 Resumen ejecutivo

**Truth Tables Generator** es un proyecto educativo que demuestra habilidades de desarrollo en Python, diseño de interfaz, modelado lógico y experiencia de usuario.
Permite trabajar con operadores proposicionales en dos modos:

1. **Tablas/Resultados de verdad**: transforma proposiciones en lenguaje natural y evalúa su resultado lógico.
2. **Minijuego**: reta al usuario a deducir operadores ocultos a partir de resultados booleanos.

> Ideal como proyecto de portafolio para mostrar fundamentos sólidos en programación, lógica y desarrollo de aplicaciones desktop.

## 🚀 Tecnologías usadas

- **Python 3**
- **Tkinter** (GUI nativa)
- Programación funcional básica (uso de funciones/lambdas para operadores lógicos)

## 🧠 Habilidades técnicas demostradas

- Diseño de aplicaciones con interfaz gráfica (Tkinter)
- Modelado de reglas de lógica proposicional
- Estructuración modular del código
- Manejo de estado en UI (dropdowns, labels, temporizador, eventos)
- Validaciones de interacción de usuario
- Resolución de problemas con enfoque educativo/gamificado

## 🧩 Funcionalidades principales

### 1) Menú principal

- Navegación entre módulos:
  - **Mini Juego**
  - **Tablas de Verdad**

### 2) Módulo de tabla de valores (`truth_values.py`)

- Entrada de proposiciones `p` y `q` en texto.
- Selección de valores de verdad (`V`/`F`).
- Generación de resultados en:
  - **Formato textual** (frases lógicas)
  - **Formato de evaluación** (`V`/`F`)
- Operadores soportados:
  - Conjunción `∧`
  - Disyunción `∨`
  - Negación `¬`
  - Condicional `→`
  - Bicondicional `↔`
  - XOR `⊕`

### 3) Minijuego lógico (`minigame.py`)

- Jugador 1 define operadores ocultos en una expresión compuesta.
- Jugador 2 intenta deducirlos observando resultados.
- Sistema de intentos y temporizador.
- Interacción dinámica de componentes en tiempo real.

## 🏗️ Estructura del proyecto

```bash
TruthTablesGenerator/
├── main.py           # Punto de entrada y navegación principal
├── truth_values.py   # Generador/evaluador de expresiones lógicas
├── minigame.py       # Minijuego de deducción lógica
└── .gitignore
```

## ▶️ Cómo ejecutar

1. Tener Python 3 instalado.
2. Clonar el repositorio.
3. Ejecutar:

```bash
python main.py
```

No requiere dependencias externas adicionales.

## 💼 Valor para reclutadores

Este proyecto evidencia capacidad para:

- Traducir teoría (lógica proposicional) a producto funcional.
- Construir interfaces usables sin frameworks pesados.
- Diseñar experiencias interactivas con restricciones de tiempo y validaciones.
- Organizar código por módulos para facilitar mantenimiento y escalabilidad.

## 🔮 Mejoras potenciales (roadmap)

- Soporte para más variables y expresiones complejas.
- Historial de partidas y puntajes.
- Tests automatizados para operadores lógicos.
- Empaquetado ejecutable (Windows/macOS/Linux).
- Mejora visual/UX del minijuego.

## 👤 Autor

Proyecto desarrollado por **Daniel Onoide** como parte de su portafolio técnico en lógica y desarrollo Python.
