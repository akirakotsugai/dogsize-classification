# Dog Size Classification

This python program uses the K-Means algorithm 
to classify dogs by size from a database containing their height and weight.
What stands out in this unsupervised algorithm is that given the size groups,
we initialize each group with no real accuracy, but it is able to tweak
the average size value (center) of each group at each iteration.
Firstly, each group's height and weight must be definied (by guessing).
After that, for each dog we must find the closest group by its center and 
add the dog to the group. When all dogs have already been classified, we must
retweak the center of the group, repeating the process until there is
no or very short move of the center compared to its previous position.

### pt-br
Esse programa se utiliza do algoritmo k-medias para à partir de uma base de dados de cães com altura e peso,
definir em qual porte cada cão se enquadra. O diferencial desse algoritmo não supervisionado é que dado os grupos
(neste caso, os portes), iniciamos cada grupo com um valor sem precisão real, mas o algoritmo se encarrega de ajustar
os valores médios de cada grupo.
Primeiramente precisa-se definir o peso e altura médio (pode chutar) dos portes que desejamos encontrar o centro final
e agrupar todos os cachorros. Depois, para cada cachorro encontrar qual grupo (Centro) está mais perto e
incluí-lo ao grupo. Depois que todos elementos (cachorros) já estiverem sidos agrupados, reajustar a posição central
de todos os grupos. Repetir o processo até que haja muito pouco ou nenhum deslocamento do centro comparado à posição anterior.

## Installation
```
sudo apt-get install python3
sudo apt-get install python3-tk
pip3 install matplotlib

```

