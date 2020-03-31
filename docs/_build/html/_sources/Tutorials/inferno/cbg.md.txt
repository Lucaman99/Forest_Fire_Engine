Getting Started With Inferno: Cumulative Burn Graphs
=============================================================

In this introductory tutorial, we are going to show how to use Inferno to look at the relationship between **tree density**, and **completion**, for a simple square-lattice
based forest, and a simple cellular-automation simulator. [1]

First, let's go over a few definitions. To start, a **forest** is defined as some graph, :math:`G = (V, E)`. Each node corresponds to some spatial position within the forest, and the edges specify 
how fire is allowed to spread over the nodes. For our simulation, we will be considering a very basic graph called a **square lattice**. We define a square lattice as follows: given some number $N$, which we call the length of our lattice, we define a set $N$ linear graphs, $H$, each $N$ nodes such that for $G \ \in \ H$, we have:

.. centered:: $E(G) \ = \ \{(v_n, v_{n+1}) \ | \ v_i \ \in \ V\}$

Let's index the elements of $H$ by $i$, where $G_i \ \in \ H$. We define the vertex set, $V_{\ell}^N$, of our lattice graph to be:

.. centered:: $V_{\ell}^N \ = \ \displaystyle\bigcup_{i = 1}^{N} V(G_i)$

Continuing on, we define $v_{i_{n}}$ to be the $n$-th vertex of the $i$-th linear graph. We define the edge-set of our lattice graph, $E_{\ell}^N$, to be:

.. centered:: $E_{\ell}^N \ = \ \Big( \displaystyle\bigcup_{i = 1}^{N} E(G_i) \Big) \ \cup \ \{ (v_{i_n}, v_{(i + 1)_n}) \ | \ v_{k_n} \ \in \ V_{\ell} \}$

Thus, our square lattice graph of length $N$ is given by $G_{\ell}^{N} \ = \ (V_{\ell}^N, E_{\ell}^N)$ looks something like this:

.. centered:: PUT IMAGE HERE

So as you can see, our forest graph resembles a grid, with nodes being connected to each other in square cycles.

For our forest, we define a **state function**, :math:`\delta(v, t)`, for some :math:`v \in V(G)`, and some time-step :math:`t` of our simulation. The
state function is able to map each vertex in the forest to either :math:`1` or :math:`0`. If the state function maps a vertex to :math:`1`, we say that at time $t$, the node contains a tree. 

For the purposes of this simple simulation, we will assume that $\delta(v, 0) = \delta(v, t)$, for all $t$. Basically, we assume that no new trees are growing (or somehow appearing) in our forest during the simulation. This simplifies our model greatly. Now, let's consider what the values of $\delta(v, t)$ will be for each $v \ \in \ V_{\ell}$. It is possible to manualy specify the exact value of the function at every node, but for large graphs, this becomes cumbersome. Thus, Inferno allows us to **randomize** placement of trees onto our graph. Specifically, for some arbitrary forest, $V$, we know that the total number of trees in this forest will be given as $\rho$, with:

.. centered:: $\rho \ = \ \displaystyle\sum_{n} \delta(v_n)$

For all $v_n \ \in \ V$. We can thus choose some number $\rho$, and randomly assign $\delta(v_n) \ = \ 1$ for $\rho$ vertices $v_n$. Behind the scenes, the way that Inferno does this is by generating $\rho$ pseudo-random coordinates, $(x, \ y)$, with $1 \ \leq \ x, y \ \leq \ N$, and set $\delta(v_{x_y}) \ = \ 1$ for all these number pairs.
