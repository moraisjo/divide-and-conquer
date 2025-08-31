# Algoritmo MaxMin Select (Divisão e Conquista)
Este projeto implementa em **Python** o algoritmo de **seleção simultânea** do menor e maior elemento de uma sequência (MaxMin Select), utilizando a técnica de **Divisão e Conquista**.  

## ▶️ Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado.  
   Verifique com:  
   ```code
   python3 --version

2. Clone este repositório ou copie o arquivo main.py para o seu computador.

3. No terminal, dentro da pasta do projeto, execute:
```code
python3 main.py
``` 

📝 Exemplo de saída:
Dada a sequência:
[7, 2, 9, 4, 1, 6, 10, 3, 152, 8, 5]
O programa exibirá:
```code
Sequência: [7, 2, 9, 4, 1, 6, 10, 3, 152, 8, 5]
Menor elemento: 1
Maior elemento: 152
```

## 📌 Lógica do algoritmo

1. **Divisão**: a sequência é dividida em duas partes.  
2. **Conquista**: de forma recursiva, encontra-se o menor e o maior elemento de cada metade.  
3. **Combinação**: compara-se apenas os resultados parciais para determinar o menor e o maior globais.  

Essa estratégia diminui o número de comparações, tornando o processo mais eficiente.

**Explicação da lógica (linha a linha):**
Define a função maxmin_select que recebe:
```code
def maxmin_select(arr, left, right):
``` 

`arr`: lista de números <br>
`left`: índice inicial do subarray<br>
`right`: índice final do subarray<br>

```code
    if left == right:
        return arr[left], arr[left]
```

Caso base 1: o subarray tem apenas um elemento.
Neste caso, o único elemento é tanto o mínimo quanto o máximo.
Retorna `(arr[left], arr[left])`.

```code
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
```
Caso base 2: o subarray tem dois elementos. Compara os dois elementos: o menor vai para mínimo; o maior vai para máximo. Retorna a tupla (mínimo, máximo). Esse passo garante apenas 1 comparação, sendo eficiente.

```code
    mid = (left + right) // 2
``` 

Calcula o índice do meio do subarray. Divide o array em duas metades: esquerda: left até mid; direita: mid + 1 até right, parte fundamental da técnica divisão e conquista.

```code
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
```

Chamadas recursivas para cada metade: `min1, max1` → mínimo e máximo da metade esquerda. `min2, max2` → mínimo e máximo da metade direita

Cada chamada segue os mesmos passos recursivos até atingir os casos base.

```code
    # Combinação dos resultados
    return min(min1, min2), max(max1, max2)
```

Após obter mínimo e máximo de cada metade:

`min(min1, min2)` → mínimo global do subarray<br>
`max(max1, max2)` → máximo global do subarray

Essa etapa combina os resultados usando apenas 2 comparações.<br>

---
