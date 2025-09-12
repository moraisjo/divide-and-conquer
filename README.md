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

## Cálculo da complexidade assintótica
* Operações básicas:
`if left == right` → comparação constante, 1 operação<br>
return arr[left], arr[left] → retorno constante, 1 operação<br>
if right == left + 1 → comparação constante, 1 operação<br>
`mid = (left + right) // 2` → constante, 1 operação<br>
`return min(min1, min2), max(max1, max2)` → constantes, 1 operação<br>
<br>
* Caso base:
Caso 1: `left == right` → retorna um único valor → custo O(1).
Caso 2: `right == left + 1` → faz apenas uma comparação e um retorno → também custo O(1).

* Identificar as chamadas recursivas
```code
min1, max1 = maxmin_select(arr, left, mid)  
min2, max2 = maxmin_select(arr, mid + 1, right)
```

Conclusão:<br>
Número de chamadas recursivas: 2
Tamanho de cada subproblema: n/2

* Montar a recorrência

Agora montamos a equação:

𝑇(𝑛)=2𝑇(𝑛2)+𝑂(1)$$ <br>
T(n) = 2T (2n) + O(1)

T(n/2) → duas chamadas recursivas.
+ O(1)$$ → custo fixo fora das chamadas.

<br><br>
I. Identifique os valores de a, b e f(n) na fórmula: T(n)=a⋅T(n/b)+f(n)
Comparando a recorrência do algoritmo com a forma geral do Teorema Mestre, podemos identificar os seguintes valores:

a=2: Este é o número de subproblemas em que o problema principal é dividido. O algoritmo faz duas chamadas recursivas (maxmin_select(arr, left, mid) e maxmin_select(arr, mid + 1, right)).

b=2: Este é o fator pelo qual o tamanho da entrada é reduzido para cada subproblema. O array é dividido ao meio a cada chamada (mid = (left + right) // 2).

f(n)=O(1): Esta é a complexidade do trabalho realizado fora das chamadas recursivas. Neste caso, envolve apenas algumas comparações (min(min1, min2) e max(max1, max2)), que levam tempo constante.

II. Calcule log para determinar o valor de p:
 a =log (base2) 2 = 1

III. Determinando o caso do Teorema Mestre
Comparando 𝑓(𝑛) = 𝑂(1) com 𝑛^(log𝑏𝑎) = 𝑛¹:

𝑓(𝑛) = 𝑂(1) = 𝑂(𝑛^(log𝑏𝑎 - ε)) para ε = 1 (pois 𝑛^(1-1) = 𝑛⁰ = 1).
Portanto, estamos no Caso 1 do Teorema Mestre.

IV. Solução assintótica
No Caso 1, a solução é:
𝑇(𝑛) = Θ(𝑛^(log𝑏𝑎)) = Θ(𝑛¹) = Θ(𝑛)

Conclusão
A complexidade assintótica do algoritmo maxmin_select é Θ(𝑛).