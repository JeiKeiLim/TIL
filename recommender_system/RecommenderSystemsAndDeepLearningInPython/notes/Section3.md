# Section 3 note

## Notation

<p align="center">
<img src="" width="0" />
</p>

$$ s(j) = \frac{\sum_{i \in \Omega_j} r_{ij}}{|\Omega_j|} $$

- $\Omega_j$: set of all users who rated item $j$
- $r_{ij}$: rating of user $i$ on item $j$
- $R_{N \times M}$: user - item rating matrix


### Persnoalized score

$$ s(i, j) = \frac{\sum_{i' \in \Omega_j} r_{i'j}}{|\Omega_j|} $$

- $i$ = $1 \cdots N$ users

------

## Predicted deviation
- $\bar{r}(i)$: average rating of user $i$

$$ dev(i, j) = r(i, j) - \bar{r}(i) $$

$$ \hat{dev}(i, j) = \frac{\sum_{i' \in \Omega_j} dev(i', j)}{|\Omega_j|} $$
$$ s(i, j) = \bar{r}(i) + \hat{dev}(i, j) $$

### With weights
- $w_{ii'}$: similarity(weight) between users $i$ and $i'$
$$ s(i, j) = \bar r_j + \frac{\sum_{i' \in \Omega_j} w_{ii'} \\{ r_{i'j} - \bar r_{i'} \\}}{\sum_{i' \in \Omega_j} |w_{ii'}|} $$

#### Pearson correlation coefficient

$$ Q_{xy} = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^N (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^N (y_i - \bar{y})^2}} $$

- Problem: We have a sparse matrix, so we can't calculate the correlation coefficient for all users. We need to find the most similar users to user $i$.

#### Calculate weights

$$ w_{ii'} = \frac{\sum_{j \in \Psi {ii'}} (r_{ij} - \bar r_i)(r_{i'j} - \bar r_{i'})}{\sqrt{\sum_{j \in \Psi_{ii'}} (r_{ij} - \bar r_i)^2} \sqrt{\sum_{j \in \Psi_{ii'}} (r_{i'j} - \bar r_{i'})^2}} $$

- $\Psi_{i}$: set of items rated by user $i$
- $\Psi_{ii'}$: set of items rated by both users $i$ and $i'$
- $\Psi_{ii'} = \Psi_{i} \cap \Psi_{i'}$


### Cosine similarity

$$ \cos{\theta} = \frac{x^Ty}{|x||y|} = \frac{\sum_{i=1}^N x_iy_i}{\sqrt{\sum_{i=1}^N x_i^2} \sqrt{\sum_{i=1}^N y_i^2}} $$

- It's just same as Pearson correlation coefficient, but without mean normalization.
- However, we are interested working with deviation, so we need to normalize the vectors.


### Neighbourhood-based collaborative filtering
- Take the top $k$ most similar users to user $i$ and calculate the predicted score.
- $k$ is typically 20-50.



