# Section 4 note
<p align="center" style="display: none;">
    <img src="" width="0" />
</p>

## Introduction
### Ratings matrix

- Ratings matrix: $R \in \mathbb{R}^{N \times M}$, where $N$ is the number of users and $M$ is the number of items.

Example:

| User | Item1 | Item2 | Item3 | Item4 | Item5 | Item 6 |
|------|-------|-------|-------|-------|-------|--------|
| 1    | 0     | **3** | 0     | **3** | 0     | 0      |
| 2    | **4** | 0     | 0     | **2** | 0     | 0      |
| 3    | 0     | 0     | **3** | 0     | 0     | **5**  |
| 4    | 0     | 0     | 0     | 0     | **3** | 0      |
| 5    | **4** | 0     | 0     | **4** | 0     | 0      |

- N = 5, M = 6

## Matrix factorization

- Matrix factorization: $\hat{R} = WU^T$
    - $\hat{R}$: Approximation of $R$, which is the ratings matrix.
    - $W$ and $U$ should be much smaller than $R$

- $W (N \times K)$: User matrix
- $U (M \times K)$: Item matrix
- $K$: Number of latent factors (practically 10 ~ 100)


- **Problem**: $R$ or $WU^T$ are too large to store in memory
    - Single prediction is just dot product of two vectors

$$ \hat r_{ij} = w_i^T u_j = \hat{R}[i,j] $$
$$ w_i = W[i], u_j = U[j] $$


### Singular Value Decomposition (SVD)

$$ X = USV^T $$

- $X$: Matrix to factorize
- $U$: Left singular vectors ($N \times K$)
- $S$: Singular values ($K \times K$)
- $V$: Right singular vectors ($M \times K$)

**Note** If we multiply $U$ and $S$ together, we get $W$ in matrix factorization.


### Interpretation

- Each of the $K$ elements in $w_i$ and $u_j$ is a feature.
- Let’s suppose $K=5$, and they are:
  - Action / Adventure, Comedy, Romance, Horror, Animation
  - Note that these genres are not necessarily the real case, it can be anything.

- $w_i(1)$ is how much user $i$ likes action.
- $w_i(2)$ is how much user $i$ likes comedy, etc.
- $u_j(1)$ is how much movie $j$ contains action.
- $u_j(2)$ is how much movie $j$ contains comedy, etc.

$$ w_i^T u_j = ||w_i|| \cdot ||u_j|| \cdot \cos(\theta) \propto \text{sim}(i,j) $$

## Training matrix factorization

- How do we approximat $R$ where $ R \approx \hat{R} = WU^T $

### Loss function

$$ J = \sum_{i,j \in \Omega} (r_{ij} - \hat r_{ij})^2 = \sum_{i,j \in \Omega} (r_{ij} - w_i^T u_j)^2 $$

- $\Omega$: Set of pairs $(i, j)$ where user $i$ rated item $j$

#### Solving for $W$

$$ \frac{\partial J}{\partial w_i} = -2 \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j) (-u_j) = 0 $$

- $\Psi_i$: Set of items rated by user $i$

$$ \sum_{j \in \Psi_i} r_{ij} u_j = \sum_{j \in \Psi_i} (w_i^T u_j)u_j = \sum_{j \in \Psi_i} u_j(u_j^T w_i) = \sum_{j \in \Psi_i} u_j u_j^T w_i = w_i^T \left ( \sum_{j \in \Psi_i} u_j u_j^T \right )$$

$$ w_i = \left ( \sum_{j \in \Psi_i} u_j u_j^T \right )^{-1} \sum_{j \in \Psi_i} r_{ij} u_j $$


#### Solving for $U$

$$ \frac{\partial J}{\partial u_j} = -2 \sum_{i \in \Gamma_j} (r_{ij} - w_i^T u_j) (-w_i) = 0 $$

- $\Gamma_j$: Set of users who rated item $j$

$$ u_j = \left ( \sum_{i \in \Gamma_j} w_i w_i^T \right )^{-1} \sum_{i \in \Gamma_j} r_{ij} w_i $$


### Training process

```python
W = np.random.rand(N, K)
U = np.random.rand(M, K)

for t in range(T):
    for i in range(N):
        W[i] = np.linalg.solve(np.dot(U.T, U), np.dot(U.T, R[i]))

    for j in range(M):
        U[j] = np.linalg.solve(np.dot(W.T, W), np.dot(W.T, R[:, j]))
```

### Adding bias

$$ \hat r_{ij} = w_i^T u_j + b_i + c_j + \mu $$

- $b_i$: User bias
- $c_j$: Item bias
- $\mu$: Global bias

#### Solving for $W$

$$ \frac{\partial J}{\partial w_i} = -2 \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - b_i - c_j - \mu) (-u_j) = 0 $$

$$ \sum_{j \in \Psi_i} (w_i^T u_j)u_j = \sum_{j \in \Psi_i} ( r_{ij} - b_i - c_j - \mu ) u_j $$

$$ w_i = \left ( \sum_{j \in \Psi_i} u_j u_j^T \right )^{-1} \sum_{j \in \Psi_i} ( r_{ij} - b_i - c_j - \mu ) u_j $$

#### Solving for $U$

$$ u_j = \left ( \sum_{i \in \Gamma_j} w_i w_i^T \right )^{-1} \sum_{i \in \Gamma_j} ( r_{ij} - b_i - c_j - \mu ) w_i $$

#### Solving for $b$

$$ \frac{\partial J}{\partial b_i} = -2 \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - b_i - c_j - \mu)(-1) = 0 $$

$$ b_i = \frac{1}{|\Psi_i|} \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - c_j - \mu) $$

#### Solving for $c$

$$ c_j = \frac{1}{|\Gamma_j|} \sum_{i \in \Gamma_j} (r_{ij} - w_i^T u_j - b_i - \mu) $$


### Regularization
#### Linear regression case

- Model: $\hat{y} = w^T x$
- Loss function: $J = \sum_{i=1}^N (y_i - \hat y_i)^2 + \lambda ||w||_2^2$
- Solution: $w = (\lambda I + X^T X)^{-1} X^T y$

#### Matrix factorization case

$$ J = \sum_{i,j \in \Omega} (r_{ij} - \hat r_{ij})^2 + \lambda \left ( \sum_{i=1}^N ||w_i||^2 + \sum_{j=1}^M ||u_j||^2 + \sum_{i=1}^N b_i^2 + \sum_{j=1}^M c_j^2 \right ) $$

#### Solving for $W$

$$ \frac{\partial J}{\partial w_i} = -2 \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - b_i - c_j - \mu) (-u_j) + 2 \lambda w_i = 0 $$

$$ \sum_{j \in \Psi_i} u_j u_j^T w_i + \lambda w_i = \sum_{j \in \Psi_i} ( r_{ij} - b_i - c_j - \mu ) u_j = \left ( \sum_{j \in \Psi_i} u_j u_j^T + \lambda I \right ) w_i  $$


$$ w_i = \left ( \sum_{j \in \Psi_i} u_j u_j^T + \lambda I \right )^{-1} \sum_{j \in \Psi_i} ( r_{ij} - b_i - c_j - \mu ) u_j $$

#### Solving for $U$

$$ u_j = \left ( \sum_{i \in \Gamma_j} w_i w_i^T + \lambda I \right )^{-1} \sum_{i \in \Gamma_j} ( r_{ij} - b_i - c_j - \mu ) w_i $$

#### Solving for $b$

$$ \frac{\partial J}{\partial b_i} = -2 \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - b_i - c_j - \mu)(-1) + 2 \lambda b_i = 0 $$

$$ \sum_{j \in \Psi_i} b_i + \lambda b_i = \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - c_j - \mu) = \left \\{ \left ( \sum_{j \in \Psi_i} 1 \right ) + \lambda \right \\} b_i $$

$$ b_i = \frac{1}{|\Psi_i| + \lambda} \sum_{j \in \Psi_i} (r_{ij} - w_i^T u_j - c_j - \mu) $$

#### Solving for $c$

$$ c_j = \frac{1}{|\Gamma_j| + \lambda} \sum_{i \in \Gamma_j} (r_{ij} - w_i^T u_j - b_i - \mu) $$


