Here are the extracted definitions from the lecture notes:

**Definitions**

*   **Ordinary Differential Equation (ODE)**
    An ordinary differential equation (ODE) is an equation that contains one or more derivatives of an unknown function, usually denoted by \(y(x)\) (or \(y(t)\) when time \(t\) is the independent variable).

*   **Order of an ODE**
    An ODE is said to be of order \(n\) if the \(n^{th}\) derivative of the unknown function \(y\) is the highest derivative of \(y\) in the equation.

*   **Implicit form of a First-Order ODE**
    A first-order ODE can be expressed in implicit form as \(F(x, y, y') = 0\).

*   **Explicit form of a First-Order ODE**
    A first-order ODE can be expressed in explicit form as \(y' = f(x, y)\).

*   **Solution of an ODE**
    A function \(y = h(x)\) is called a solution of \(F(x, y, y') = 0\) on \(a < x < b\) if:
    *   \(h\) is differentiable on \((a, b)\),
    *   substitution of \(y = h(x)\), \(y' = h'(x)\) gives an identity.

*   **Solution Curve (or Integral Curve)**
    The graph of a function \(h\) (which is a solution) is called a solution curve or integral curve.

*   **Particular Solution**
    A particular solution is obtained from the general solution using an initial condition \(y(x_0) = y_0\), which determines the constant C.

*   **Initial Value Problem (IVP)**
    An ODE \(y' = f(x, y)\) together with an initial condition \(y(x_0) = y_0\) is called an initial value problem (IVP).

*   **Homogeneous Function**
    A function \(f(x,y)\) is called homogeneous of degree \(n\) if \(f(tx,ty) = t^n f(x,y)\).

*   **Homogeneous Differential Equation**
    An ordinary differential equation \(M(x,y)dx + N(x,y)dy = 0\) is called a homogeneous differential equation if \(M(x,y)\) and \(N(x,y)\) are homogeneous functions of the same degree. Equivalently, a first-order ODE \(y' = f(x,y)\) is homogeneous if \(f(x,y)\) is a homogeneous function of degree 0, which implies it can be written as \(f(x,y) = F(y/x)\).

*   **Exact Differential Equation**
    An ODE \(M(x,y)dx + N(x,y)dy = 0\) is called an exact differential equation if there exists a function \(u(x,y)\) (often called a potential function) such that its total differential \(du\) is equal to \(M(x,y)dx + N(x,y)dy\). This implies that \(\frac{\partial u}{\partial x} = M(x,y)\) and \(\frac{\partial u}{\partial y} = N(x,y)\).