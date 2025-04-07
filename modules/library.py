class Transaction:
    """
    Clase que representa una transacción financiera individual.

    Esta clase almacena los detalles esenciales de una transacción, como el identificador único,
    el tipo de transacción (por ejemplo, 'Crédito' o 'Débito') y el monto asociado. El propósito de
    esta clase es facilitar la manipulación y el análisis de transacciones dentro de una colección o
    sistema de registros financieros.

    Atributos:
        id (int): Identificador único de la transacción.
        type (str): Tipo de transacción, como 'Crédito' o 'Débito'.
        amount (float): Monto de la transacción.

    Métodos:
        __init__(self, id: int, type: str, amount: float) -> None:
            Inicializa una nueva transacción con los valores proporcionados para el identificador,
            tipo y monto.

    :param id: Identificador único de la transacción.
    :type id: int
    :param type: Tipo de transacción, por ejemplo, 'Crédito' o 'Débito'.
    :type type: str
    :param amount: Monto asociado a la transacción.
    :type amount: float
    :ivar id: Identificador único de la transacción.
    :ivar type: Tipo de la transacción.
    :ivar amount: Monto de la transacción.
    """

    def __init__(self, id: int, type: str, amount: float):
        self.id: int = id
        self.type: str = type
        self.amount: float = amount


class TransactionCollection:
    """
    Clase que representa una colección de transacciones.

    Esta clase gestiona un conjunto de transacciones y proporciona métodos para agregar transacciones,
    realizar cálculos como la suma total de los montos, y generar reportes basados en los datos de las
    transacciones almacenadas.

    Atributos:
        transactions (list[Transaction]): Lista de objetos de tipo `Transaction` que representan las
                                          transacciones almacenadas en la colección.

    Métodos:
        __init__(self) -> None:
            Inicializa una nueva colección vacía de transacciones.

        __iter__(self) -> iter:
            Devuelve un iterador sobre las transacciones de la colección.

        add_transaction(self, transaction: Transaction) -> None:
            Agrega una transacción a la colección.

        generate_balance(self) -> float:
            Calcula y retorna la diferencia entre la suma del monto de transacciones de tipo "Crédido"
            y la suma del monto de transacciones tipo "Débito".

        max_transaction(self) -> Transaction:
            Retorna la transacción con el monto máximo de la colección.

        total_debit_transactions(self) -> int:
            Retorna el número total de transacciones de tipo "Débito" en la colección.

        total_credit_transactions(self) -> int:
            Retorna el número total de transacciones de tipo "Crédito" en la colección.

        generate_report(self) -> str:
            Genera un reporte con el balance final, la transacción de mayor monto y el conteo de
            transacciones de tipo "Crédito" y "Débito".

    :param transactions: Lista de objetos de la clase `Transaction` que representa las transacciones
                         en la colección.
    :type transactions: list[Transaction]
    :return: Ninguno
    :rtype: None
    """

    def __init__(self):
        self.transactions: list[Transaction] = []

    def __iter__(self):
        return iter(self.transactions)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def generate_balance(self) -> float:
        sum_credit: float = sum(
            t.amount for t in self.transactions if t.type == "Crédito"
        )
        sum_debit: float = sum(
            t.amount for t in self.transactions if t.type == "Débito"
        )
        return round((sum_credit - sum_debit), 2)

    def max_transaction(self) -> Transaction:
        return max(self, key=lambda t: t.amount)

    def total_debit_transactions(self) -> int:
        return len(list(filter(lambda t: t.type == "Crédito", self)))

    def total_credit_transactions(self) -> int:
        return len(list(filter(lambda t: t.type == "Débito", self)))

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
