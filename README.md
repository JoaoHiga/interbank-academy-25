<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">Reto Técnico Cobol - Interbank Academy 2025</h3>

  <p align="center">
    Aplicación de línea de comandos (CLI) para procesar transacciones bancarias desde archivos CSV, desarrollada como parte del proceso de selección de Codeable para Interbank.
    <br />
    <a href="https://github.com/JoaoHiga/interbank-academy-25"><strong>Explora la documentación »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
  ## índice de contenido
  <ol>
    <li>
      <a href="#about-the-project">🎯 Introducción</a>
      <ul>
        <li><a href="#built-with">🛠 Tecnologías usadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">🚀 Comenzando</a>
      <ul>
        <li><a href="#prerequisites">📋 Prerrequisitos</a></li>
        <li><a href="#installation">⚙️ Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usage">🖥️ Uso</a></li>       
    <li><a href="#solution">🧠 Enfoque y Solución</a></li>
    <li><a href="#structure">📂 Estructura del Proyecto</a></li>
    <li><a href="#contributing">🤝 Contribuciones</a></li>
    <li><a href="#contact">📞 Contacto</a></li>
  </ol>


<!-- ABOUT THE PROJECT -->
<a id="about-the-project"></a>
## 🎯 Introducción
### 📌 Objetivo:  
Desarrollar una aplicación CLI en Python para procesar transacciones bancarias desde un CSV y generar un reporte con:  
- ✅ Balance final (Créditos - Débitos)  
- 🔍 Transacción de mayor monto  
- 📊 Conteo de transacciones por tipo  

<a id="built-with"></a>
### 🛠 Tecnologías usadas

* [![Python][Next.js]][Next-url]

<a id="getting-started"></a>
<!-- GETTING STARTED -->
## 🚀 Comenzando

<a id="prerequisites"></a>
### 📋 Prerequisitos
- Tener instalado Python 3.8 o superior en tu computadora.
- Archivo CSV con encabezados: id, tipo, monto.

<a id="installation"></a>
### ⚙️ Instalación
1. Clonar el repositorio
   ```sh
   git clone https://github.com/JoaoHiga/interbank-academy-25
   ```
2. Ubícate en la carpeta
   ```sh
   cd interbank-academy-25
   ```
<a id="usage"></a>
<!-- USAGE EXAMPLES -->
## 🖥️ Uso
1. Ejecuta el comando
   </br>
   En Windows
   ```sh
   python csv_to_report.py "ruta/a/tu/archivo.csv"
   ```

   En Mac/Linux
   ```sh
   python3 csv_to_report.py "ruta/a/tu/archivo.csv"
   ```
<a id="solution"></a>
## 🧠 Enfoque y Solución

### 🔍 Problema Central
Procesar transacciones bancarias desde archivos CSV para generar reportes con:

- Balance final (Créditos - Débitos).
- Identificación de la transacción con mayor monto.
- Conteo de transacciones por tipo.

**1. Diseño de Clases**
```python
class Transaction:
    """Modela una transacción individual con validación implícita"""
    def __init__(self, id: int, type: str, amount: float):
        self.id: int = id
        self.type: str = type
        self.amount: float = amount
```
```python
class TransactionCollection:
    """Gestiona lógica de agregación y reportes"""
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
```

**2. Procesamiento del CSV**
- Validación estricta:
```python
desired_headers = {"id", "tipo", "monto"}  # 🔐 Encabezados obligatorios
if csv_headers is None or not desired_headers.issubset(csv_headers):
    raise ValueError("Encabezados inválidos")
```
- Manejo de errores:
  - `FileNotFoundError`: Archivo inexistente.
  - `UnicodeDecodeError`: Codificación incorrecta.
  - `ValueError`: Datos faltantes o tipos incorrectos o archivo en formato incorrecto.

**3. Generación de Reportes**
```python
def generate_report(self) -> str:
  balance: float = self.generate_balance()
  max_transaction: Transaction = self.max_transaction()
  total_credit_transactions = self.total_credit_transactions()
  total_debit_transactions = self.total_debit_transactions()

  return f"""
  Reporte de Transacciones
  ---------------------------------------------
  Balance final: {balance}
  Transacción de mayor monto: ID {max_transaction.id} - {max_transaction.amount}
  Conteo de Transacciones: Crédito: {total_credit_transactions} Débito: {total_debit_transactions}
  """
```

![Demo](https://github.com/JoaoHiga/interbank-academy-25/blob/main/images/demo.png)


## 🔍 Decisiones Clave

| Decisión | Justificación | Impacto |
|----------|---------------|---------|
| **Separación de clases**<br>`Transaction` / `TransactionCollection` | Cumple el principio de responsabilidad única (SOLID). | ✅ Facilita el mantenimiento<br>✅ Permite extender funcionalidades por separado |
| **Validación durante lectura de CSV** | - Verifica encabezados (`id`, `tipo`, `monto`)<br>- Conversión forzada de tipos | 🛡️ Previene errores de procesamiento<br>⚡ Optimiza uso de recursos |
| **Métodos independientes**<br>`sum_amounts()`<br>`max_transaction()` | - Código modular<br>- Single Responsibility Principle | 🧪 Facilita pruebas unitarias<br>♻️ Reutilización en otros contextos |

<a id="structure"></a>
## 📂 Estructura del Proyecto

```sh
interbank-academy-25/
├── 📁 modules/
│   └── 📜 library.py          # 🏛️ Clases Transaction y TransactionCollection
├── 📜 csv_to_report.py        # ⚡ Script principal (CLI)
├── 📄 data.csv                # 🧾 Ejemplo de datos
├── 📜 .gitignore
└── 📜 README.md
```

<a id="contributing"></a>
<!-- CONTRIBUTING -->
## 🤝 Contribuciones

✨ Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Todas tus contribuciones serán enormemente valoradas.

Si tienes una sugerencia para mejorar el proyecto:

1. Haz un fork del repositorio y crea un Pull Request.

2. O simplemente abre un issue con la etiqueta **"mejora"**.
¡No olvides darle una ⭐ al proyecto! ¡Gracias por tu apoyo!

📋 Guía rápida para contribuir:
1. Bifurca el proyecto (fork)
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. **Commitea** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Sube tus cambios (`git push origin feature/AmazingFeature`)
5. Abre a **Pull Request**

<a id="contact"></a>
<!-- CONTACT -->
## 📞Contacto

👨‍💻 Joao Higa - [@joao-higa-caldeira](https://linkedin.com/in/joao-higa-caldeira/) - jopenta21@gmail.com
</br>
Enlace al proyecto: [https://github.com/JoaoHiga/interbank-academy-25](https://github.com/JoaoHiga/interbank-academy-25)

<p align="right">(<a href="#readme-top">Hacia arriba</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JoaoHiga/interbank-academy-25.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/JoaoHiga/interbank-academy-25/contributors
[forks-shield]: https://img.shields.io/github/forks/JoaoHiga/interbank-academy-25.svg?style=for-the-badge
[forks-url]: https://github.com/JoaoHiga/interbank-academy-25/network/members
[stars-shield]: https://img.shields.io/github/stars/JoaoHiga/interbank-academy-25.svg?style=for-the-badge
[stars-url]: https://github.com/JoaoHiga/interbank-academy-25/stargazers
[issues-shield]: https://img.shields.io/github/issues/JoaoHiga/interbank-academy-25.svg?style=for-the-badge
[issues-url]: https://github.com/JoaoHiga/interbank-academy-25/issues
[license-shield]: https://img.shields.io/github/license/JoaoHiga/interbank-academy-25.svg?style=for-the-badge
[license-url]: https://github.com/JoaoHiga/interbank-academy-25/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joao-higa-caldeira/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Next-url]: https://www.python.org/
