# Section 6 note
<p align="center" style="display: none;">
    <img src="" width="0" />
</p>

## Restricted Boltzmann Machine (RBM) for Recommender Systems

- We can consider RBM as a neural network with one hidden layer.
    - I can calculate the visible layer $v$ by using the hidden layer $h$
    - I can calculate the hidden layer $h$ by using the visible layer $v$
    - $v \rightarrow h$ and $h \rightarrow v$

### Bernoulli RBM
- Bernoulli RBM: Visible and hidden layers are binary
    - $v_i \in \{0, 1\}$
    - $h_j \in \{0, 1\}$

#### $v \rightarrow h$
- $\sigma$: Sigmoid function
- $W$: Shared weight matrix

$$ p(h = 1 | v) = \sigma(W^T v + c) $$

$$ p(h_j = 1 | v) = \sigma(\sum_{i=1}^D W_{ij} v_i + c_j) $$

$$ i = 1 \cdots D, j=1 \cdots M, \text{len}(v) = D, \text{len}(h) = M $$

#### $h \rightarrow v$

$$ p(v = 1 | h) = \sigma(W h + b) $$

$$ p(v_i = 1 | h) = \sigma(\sum_{j=1}^M W_{ij} h_j + b_i) $$

##### Using $p(h=1 | v)$ as a input for $p(v=1 | h)$

$$ \tilde{h} = p(h = 1 | v) $$
$$ p(v' = 1 | h) = \sigma(W \tilde{h} + b) $$

- With this characteristic, we can calculate the visible layer $v$ by using the hidden layer $h$ and vice versa.
    - This resembles the autoencoder.

- $ v \rightarrow h \rightarrow v' $

$$ h = \sigma(W^T v + c) $$
$$ v' = \sigma(W h + b) $$

-----

### Intuition of Boltzmann Machine
- It connects to everything
- High energy to low energy
    - High energy: High probability
    - Low energy: Low probability

#### Energy of a Boltzmann Machine

$$ E = - \left ( \sum_{i, j} W_{ij} s_i s_j + \sum_i b_i s_i \right ) $$

#### Training a Boltzmann Machine
- It only works on trivial problems.

$$ G = \sum_v P^+ (v) \ln \left ( \frac{P^+ (v)}{P^- (v)} \right ) $$

### Comparison Boltzmann Machine and Restricted Boltzmann Machine

- Boltzmann Machine: Fully connected
- Restricted Boltzmann Machine: Not fully connected
    - It is restricted to have no connections between hidden units and visible units.

#### Energy of a Restricted Boltzmann Machine

$$ E(v, h) = - \left ( \sum_{i, j} W_{ij} v_i h_j + \sum_i b_i v_i + \sum_j c_j h_j \right ) $$

$$ E(v, h) = - \left ( v^T W h - b^T v - c^T h \right ) $$

### Probability of a Restricted Boltzmann Machine

$$ p(v, h) \propto e^{-E(v, h)} $$

$$ p(v, h) = \frac{1}{Z} e^{-E(v, h)} \text{, } Z = \sum_v \sum_h e^{-E(v, h)} $$

$$ \sum_v \sum_h p(v, h) = 1 $$


-----

### Bayes rules for RBM

$$ p(v | h) = \frac{p(v, h)}{p(h)} $$
$$ p(h | v) = \frac{p(v, h)}{p(v)} $$

- $ p(v) = \sum_h p(v, h) $
- $ p(h) = \sum_v p(v, h) $

$$ p(v, h) = \frac{1}{Z} \exp \left ( v^T W h - b^T v - c^T h \right ) $$
$$ p(v) = \sum_h \frac{1}{Z} \exp \left ( v^T W h - b^T v - c^T h \right ) $$

$$ p(h | v) = \frac{p(v, h)}{p(v)} = \frac{\exp \left ( v^T W h - b^T v - c^T h \right )}{\sum_h \exp \left ( v^T W h - b^T v - c^T h \right )} $$

- $Z$ is canceled out.

$$ p(h | v) = \frac{1}{Z'} \exp \left ( v^T W h - b^T v - c^T h \right ) $$

- Simplify the denominator as $Z'$

$$ p(h | v) = \frac{1}{Z'} \exp \left ( \sum_{i=1}^D \sum_{j=1}^M W_{ij} v_i h_j + \sum_{i=1}^D b_i v_i + \sum_{j=1}^M c_j h_j \right ) $$

- Exponent of the sum can be changed to the product of the exponentials.

$$ p(h | v) = \frac{1}{Z'} \exp \left ( \sum_{i=1}^D b_i v_i \right ) \prod_{j=1}^M \exp \left ( \sum_{i=1}^D W_{ij} v_i h_j + c_j h_j \right ) $$

- $b_i v_i$ is independent of $h_j$, so it can be absorbed into $Z''$.

$$ p(h | v) = \frac{1}{Z''} \prod_{j=1}^M \exp \left ( \sum_{i=1}^D W_{ij} v_i h_j + c_j h_j \right ) $$

- $h_j$ is in every term, so it can be separated.

$$ p(h | v) = \frac{1}{Z''} \prod_{j=1}^M \exp \left ( h_j \left \\{ \sum_{i=1}^D W_{ij} v_i + c_j \right \\} \right ) $$

- $p(h_j | v)$ is independent of the others.

$$ p(h_j | v) = \frac{1}{Z'''} \exp \left ( h_j \left \\{ \sum_{i=1}^D W_{ij} v_i + c_j \right \\} \right ) $$

$$ p(h_j = 1 | v) = \frac{1}{Z'''} \exp \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right ) $$

$$ p(h_j = 0 | v) = \frac{1}{Z'''} \exp (0) = \frac{1}{Z'''} $$


- Solving $Z'''$

$$ p(h_j = 1 | v) + p(h_j = 0 | v) = 1 $$

$$ \frac{1}{Z'''} \exp \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right ) + \frac{1}{Z'''} = 1 $$

$$ Z''' = 1 + \exp \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right ) $$

- Finally, we can get the probability of $h_j$ given $v$.

$$ p(h_j = 1 | v) = \frac{\exp \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right )}{1 + \exp \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right )} = \sigma \left ( \sum_{i=1}^D W_{ij} v_i + c_j \right) $$

$$ p(h = 1 | v) = \sigma(W^T v + c) $$

-----

### Training a Restricted Boltzmann Machine
- Theoratically, it's almost impossible to train a Boltzmann Machine due to the intractable partition function.
- We neeed to use a approximation method to train a RBM.


#### Maximum Likelihood Estimation

$$ \text{Maximize } p(v) \text{ wrt } W, b, c $$

$$ W, b, c = \arg \max_{W, b, c} p(v; W, b, c) = \arg \max_{W, b, c} \log p(v; W, b, c) $$

##### Example of $\mu$ and $\sigma^2$

$$ \mu, \sigma^2 = \arg \max_{\mu, \sigma^2} \log \mathcal{N}(x; \mu, \sigma^2) $$

$$ \mu = \frac{1}{N} \sum_{i=1}^N x_i $$
$$ \sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2 $$


