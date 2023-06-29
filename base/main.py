# TODO completa la suma
def sum(a, b):
    return a + b

# TODO prepara una función que multiplica dos números que recibe por argumento
def mult(a, b):
    return a * b

# TODO prepara una función que genere números dentro de una lista
def generate_numbers():
    numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    # TODO llama a la función suma y printa el resultado por pantalla
    result_sum = sum(3, 4)
    print("Resultado de la suma:", result_sum)

    # TODO llama la función multiplicar y printa el resultado por pantalla
    result_mult = mult(5, 6)
    print("Resultado de la multiplicación:", result_mult)

    # TODO llama a la función de generar números y printa la lista generada
    numbers_list = generate_numbers()
    print("Lista generada:", numbers_list)



