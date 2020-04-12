Getting Started With Inferno: Forest Completion and Tree Density
=======================================================================

In this introductory tutorial, we are going to show how to use Inferno to look at the relationship between **tree density**, and **completion**, for a simple square-lattice
based forest, and a simple cellular-automation simulator. [1]

First, let's go over a few definitions. To start, a **forest** is defined as some graph, :math:`G = (V, E)`. Each node corresponds to some spatial position within the forest, and the edges specify 
how fire is allowed to spread over the nodes. For our simulation, we will be considering a very basic graph called a **square lattice**. We define a square lattice as follows: given some number :math:`N`, which we call the length of our lattice, we define a set :math:`N ` linear graphs, :math:`H`, each :math:`N` nodes such that for :math:`G \ \in \ H`, we have:

.. centered:: :math:`E(G) \ = \ \{(v_n, v_{n+1}) \ | \ v_i \ \in \ V\}`

Let's index the elements of :math:`H` by :math:`i`, where :math:`G_i \ \in \ H`. We define the vertex set, :math:`V_{\ell}^N`, of our lattice graph to be:

.. centered:: :math:`V_{\ell}^N \ = \ \displaystyle\bigcup_{i = 1}^{N} V(G_i)`

Continuing on, we define :math:`v_{i_{n}}` to be the :math:`n`-th vertex of the :math:`i`-th linear graph. We define the edge-set of our lattice graph, :math:`E_{\ell}^N`, to be:

.. centered:: :math:`E_{\ell}^N \ = \ \Big( \displaystyle\bigcup_{i = 1}^{N} E(G_i) \Big) \ \cup \ \{ (v_{i_n}, v_{(i + 1)_n}) \ | \ v_{k_n} \ \in \ V_{\ell} \}`

Thus, our square lattice graph of length :math:`N` is given by :math:`G_{\ell}^{N} \ = \ (V_{\ell}^N, E_{\ell}^N)` looks something like this:

.. centered:: PUT IMAGE HERE

So as you can see, our forest graph resembles a grid, with nodes being connected to each other in square cycles. We can do this fairly easily in Inferno, as a square lattice is one of the built-in graphs::

    import inferno

    # Creates the grid
    lattice_graph = inferno.sgraph.SquareLatticeGraph(length=num)

For our forest, we define a **state function**, :math:`\delta(v, t)`, for some :math:`v \in V(G)`, and some time-step :math:`t` of our simulation. The
state function is able to map each vertex in the forest to either :math:`1` or :math:`0`. If the state function maps a vertex to :math:`1`, we say that at time :math:`t`, the node contains a tree. 

For the purposes of this simple simulation, we will assume that :math:`\delta(v, 0) = \delta(v, t)`, for all :math:`t`. Basically, we assume that no new trees are growing (or somehow appearing) in our forest during the simulation. This simplifies our model greatly. Now, let's consider what the values of :math:`\delta(v, t)` will be for each :math:`v \ \in \ V_{\ell}`. It is possible to manualy specify the exact value of the function at every node, but for large graphs, this becomes cumbersome. Thus, Inferno allows us to **randomize** placement of trees onto our graph. Specifically, for some arbitrary forest, :math:`V`, we know that the total number of trees in this forest will be given as :math:`\rho`, with:

.. centered:: :math:`\rho \ = \ \displaystyle\sum_{n} \delta(v_n)`

For all :math:`v_n \ \in \ V`. We can thus choose some number :math:`\rho`, and randomly assign :math:`\delta(v_n) \ = \ 1` for :math:`\rho` vertices :math:`v_n`. Behind the scenes, the way that Inferno does this is by generating :math:`\rho` pseudo-random coordinates, :math:`(x, \ y)`, with :math:`1 \ \leq \ x, y \ \leq \ N`, and set :math:`\delta(v_{x_y}) \ = \ 1` for all these number pairs. We define the **tree density**, :math:`\sigma`, of our graph as "another way" to write the total number of trees, as it is just the number of trees divided by the number of nodes:

.. centered:: :math:`\sigma \ = \ \dfrac{\rho}{|V(G)|}`

This is the number that we will be feeding into our state function, which will be used in the simulation. In addition to the state function, we also must define an **update function** which is another function :math:`\beta: V \ \times \ T \ \rightarrow \ \{0, \ 1\}`, which tells us at some time :math:`t`, whether some vertex :math:`v` has been "burned" by the simulation. Note that for some vertex :math:`w`, it can only be true that :math:`\beta(w, \ t) \ = \ 1` if :math:`\delta(w,  \ t) \ = \ 1` (basically, a vertex can only "burn" at time :math:`t` if it contains a tree at time :math:`t`). In the simulation of our algorithm, we are going to implement a "cellular-automata-like" update rule, where for some :math:`w \ \in \ V`, if :math:`\beta(w, \ t) \ = \ 1`, then :math:`\beta(x, \ t + 1) \ = \ 1` for all :math:`x \ \in \ (w)`. We then define:

.. centered:: :math:`U(w) \ = \ \{x \ | \ x \ \in \ N(w), \ \delta(x, \ t + 1) \ = \ 1\}`

Where :math:`N(w)` is defined to be the neighbourhood of :math:`w`:

.. centered:: :math:`N(w) \ = \ \{v \ | \ v \ \in \ V(G), \ (w, \ v) \ \in \ E(G)\}`

In simpler language, fire can spread from a burning vertex to another vertex that is connected to the burning vertex, if the other vertex contains a tree. This is similar to the idea of a cellular-automaton spreading to grid squares that are a taxicab distance of :math:`1` away from the original square (the Von Neumann neighbourhood of the original square). Thus, we call this particular function the Von Neumann cellular-automaton update function (this function is built-into Inferno as well).
