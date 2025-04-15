import sys
import os
from csv import DictReader
from modules.library import Transaction, TransactionCollection


def read_csv(path_to_csv: str) -> TransactionCollection:
    """
    Genera un objeto de la clase TransactionCollection a partir de un archivo CSV.

    Esta función procesa un archivo CSV, valida que los encabezados sean los esperados, y crea
    una colección de transacciones a partir de los datos contenidos en el archivo. Cada transacción
    es representada por un objeto `Transaction` y se almacena dentro de un objeto `TransactionCollection`.
    Si alguna de las validaciones falla, se lanzan errores apropiados.

    El archivo CSV debe contener los encabezados necesarios, como 'id', 'tipo' y 'monto'. Los valores
    del archivo son procesados y convertidos a los tipos adecuados para ser utilizados en el objeto de
    la clase `Transaction`. Las transacciones cuyo tipo y/o monto no pueden ser obtenidos se ignoran
    en la carga hacia el objeto TransactionCollection.

    :param path_to_csv: Ruta al archivo CSV (relativa o absoluta) que contiene las transacciones.
    :type path_to_csv: str
    :param desired_headers: Conjunto de encabezados esperados en el archivo CSV. Si los encabezados
                             del archivo no coinciden con este conjunto, se lanza un error.
    :type desired_headers: set
    :return: Un objeto `TransactionCollection` que contiene todas las transacciones procesadas.
    :rtype: TransactionCollection
    :raises FileNotFoundError: Si el archivo no existe en la ruta especificada.
    :raises ValueError: Si el archivo tiene una codificación incorrecta, formato inválido.
    :raises ValueError: Si el archivo tiene encabezados incorrectos.
    """

    # Header necesarios del archivo CSV
    desired_headers: set[str] = {"id", "tipo", "monto"}

    try:
        with open(path_to_csv, encoding="utf-8", mode="r") as csv_file:
            # Iterador de archivo CSV.
            csv_reader: DictReader = DictReader(csv_file, delimiter=",")
            # Obtiene encabezados de CSV.
            csv_headers = csv_reader.fieldnames
            # Comprueba si existen los encabezados deseados.
            if csv_headers is None or not desired_headers.issubset(csv_headers):
                raise ValueError(
                    "El archivo CSV no contiene encabezados válidos o esperados."
                )

            transactions = TransactionCollection()
            # Comprueba cada entrada y las agrega al objeto transactions.
            for entry in csv_reader:
                try:
                    id: int = int(entry["id"])
                    amount: float = float(entry["monto"])
                except TypeError:
                    print(f"No se pudo procesar la transacción de ID: {entry["id"]}.")
                    continue

                type: str = entry["tipo"]

                transactions.add_transaction(Transaction(id, type, amount))

            return transactions
    # Excepciones
    except FileNotFoundError:
        raise FileNotFoundError("Archivo no encontrado en la ruta especificada.")
    except UnicodeDecodeError:
        raise ValueError("Tipo de archivo o codificación incorrecta.")


if __name__ == "__main__":
    # Comprueba si se ha brindado la ruta del archivo CSV.
    if len(sys.argv) != 2:
        print("No se proporcionó la ruta del archivo CSV.")
        print(f'Ejemplo: python {os.path.basename(__file__)} "ruta/a/transacciones.csv"')
        sys.exit(1)

    csv_path: str = sys.argv[1]

    # Ejecuta la función read_csv() e imprime reporte
    transactions: TransactionCollection = read_csv(csv_path)
    print(transactions.generate_report())
