import array as arr
import numpy as np

#
# Um array deve ser instanciado como feito abaixo.
# Primeiro deve-se indicar de que tipo serão os objetos presentes no array. No exemplo abaixo o tipo 'd'
# indica que o array conterá números de ponto flutuante.
# Em seguida deve ser passada uma lista de objetos do tipo especificado ou pelo menos um valor que possa ser
# convertido para o tipo especificado. No exemplo abaixo o inteiro 1 pode ser convertido para o número real
# 1.0
#
arr.array = ('d', [1, 3.5])


#
# O Numpy é uma biblioteca do Python volta para cálculos matemáticos complexos e ela oferece sua própria versão
# de array. O array criado anteriormente no Numpy seria criado conforme abaixo. Arrays criados com Numpy tem um
# desempenho muito melhor.
#
array_numpy = np.array([1, 3.5])
print(array_numpy)

array_numpy += 3 # Soma 3 a cada um dos elementos presentes no array
print(array_numpy)

