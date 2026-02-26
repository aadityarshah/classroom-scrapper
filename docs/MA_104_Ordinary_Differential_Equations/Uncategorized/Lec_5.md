Here are the extracted definitions and theorems from the lecture notes:

---

### Definitions

1.  **Linear and Nonlinear Second-Order Ordinary Differential Equations (ODEs)**
    A second-order ODE is called **linear** if it can be written as
    \[ y'' + p(x)y' + q(x)y = r(x) \quad \text{(1)} \]
    It is called **nonlinear** if it cannot be written in this form.
    Alternatively, a second-order ODE of the form \( \frac{d^2y}{dx^2} = f(x, y, \frac{dy}{dx}) \) is called linear if \( f \) is linear in \( y \) and \( \frac{dy}{dx} \), i.e., \( f(x, y, y') = r(x) - p(x)y' - q(x)y \).

2.  **Homogeneous and Nonhomogeneous Equations**
    If \( r(x)=0 \) in equation (1), then the ODE reduces to
    \[ y'' + p(x)y' + q(x)y = 0 \quad \text{(2)} \]
    Equation (2) is called a **homogeneous equation**. Otherwise, it is called a **nonhomogeneous equation**.

3.  **Initial Value Problem (IVP) for Second-Order Linear ODEs**
    For a homogeneous second-order linear ODE, an Initial Value Problem (IVP) consists of the ODE along with two initial conditions: \( y(x_0)=y_0 \) and \( y'(x_0)=y_1 \).

4.  **General Solution and Basis of Solutions**
    A **general solution** of a homogeneous second-order linear ODE on an open interval \( I \) is a solution of the form \( c_1y_1 + c_2y_2 \), where \( y_1 \) and \( y_2 \) are solutions of the ODE on \( I \) that are not proportional (i.e., linearly independent), and \( c_1, c_2 \) are arbitrary constants. The solutions \( y_1 \) and \( y_2 \) are called a **basis of solutions** of the ODE on \( I \). A **particular solution** is obtained by assigning specific values to \( c_1 \) and \( c_2 \).

5.  **Null Space of a Linear Operator**
    Let \( L[y(x)] := y''(x) + P(x)y'(x) + Q(x)y(x) \). Then \( L: C^2(I) \to C(I) \) can be viewed as a linear map. The **null space** of \( L \) is defined as \( N(I) = \{ y \in C^2(I) : Ly=0 \} \).

6.  **Characteristic Polynomial (for Constant Coefficient ODEs)**
    For a homogeneous linear ODE with constant coefficients \( y'' + Py' + Qy = 0 \), the **characteristic polynomial** is defined as \( \chi(\lambda) = \lambda^2 + P\lambda + Q = 0 \).

7.  **Euler-Cauchy Equation**
    An ODE of the form \( x^2y'' + axy' + by = 0 \) is called an **Euler-Cauchy equation**, where \( a \) and \( b \) are constants.

---

### Theorems

1.  **Superposition Principle for Homogeneous ODEs**
    Suppose that \( y_1(x) \) and \( y_2(x) \) are two solutions of the homogeneous equation \( y'' + p(x)y' + q(x)y = 0 \). Then \( c_1y_1 + c_2y_2 \) is also a solution for any constants \( c_1, c_2 \).
    **Proof (Fundamental):**
    Let \( L[y] = y'' + p(x)y' + q(x)y \). Since \( y_1 \) and \( y_2 \) are solutions, \( L[y_1] = 0 \) and \( L[y_2] = 0 \).
    Then \( L[c_1y_1 + c_2y_2] = (c_1y_1 + c_2y_2)'' + p(x)(c_1y_1 + c_2y_2)' + q(x)(c_1y_1 + c_2y_2) \)
    \( = c_1y_1'' + c_2y_2'' + p(x)(c_1y_1' + c_2y_2') + q(x)(c_1y_1 + c_2y_2) \)
    \( = c_1(y_1'' + p(x)y_1' + q(x)y_1) + c_2(y_2'' + p(x)y_2' + q(x)y_2) \)
    \( = c_1L[y_1] + c_2L[y_2] = c_1(0) + c_2(0) = 0 \).
    Thus, \( c_1y_1 + c_2y_2 \) is also a solution.

2.  **Existence and Uniqueness Theorem for Second-Order Linear IVP**
    Consider the linear second-order IVP: \( y''(x) + P(x)y'(x) + Q(x)y(x) = R(x) \) with initial conditions \( y(x_0)=y_0 \) and \( y'(x_0)=y_1 \).
    If \( P(x) \) and \( Q(x) \) are continuous functions, then this IVP admits a unique solution. Moreover, the null space \( N(I) \) (of the associated homogeneous operator) is a vector space of dimension 2.

3.  **Constructing a Basis and General Solution (Proof Sketch)**
    To show \( N(I) \) has dimension 2, we need to:
    i) Produce two linearly independent solutions \( y_1 \) and \( y_2 \).
    ii) Show any solution is a linear combination of \( y_1 \) and \( y_2 \).

    **i) Existence of a Linearly Independent Basis:**
    By the uniqueness theorem, there exist unique solutions of the following IVPs:
    *   \( y_1 \): \( y'' + P(x)y' + Q(x)y = 0 \), with \( y_1(x_0)=1, y_1'(x_0)=0 \)
    *   \( y_2 \): \( y'' + P(x)y' + Q(x)y = 0 \), with \( y_2(x_0)=0, y_2'(x_0)=1 \)
    To show \( y_1 \) and \( y_2 \) are linearly independent, suppose \( c_1y_1(x) + c_2y_2(x) = 0 \) for all \( x \).
    Then \( c_1y_1'(x) + c_2y_2'(x) = 0 \).
    At \( x=x_0 \):
    \( c_1y_1(x_0) + c_2y_2(x_0) = 0 \implies c_1(1) + c_2(0) = 0 \implies c_1=0 \).
    \( c_1y_1'(x_0) + c_2y_2'(x_0) = 0 \implies c_1(0) + c_2(1) = 0 \implies c_2=0 \).
    Since \( c_1=0 \) and \( c_2=0 \), \( y_1 \) and \( y_2 \) are linearly independent.

    **ii) Any Solution is a Linear Combination:**
    Suppose \( y(x) \) is an arbitrary solution of the given homogeneous ODE. Let \( y(x_0) = Y_0 \) and \( y'(x_0) = Y_1 \).
    Define \( \tilde{y}(x) = Y_0y_1(x) + Y_1y_2(x) \).
    From the Superposition Principle, \( \tilde{y}(x) \) is a solution to the ODE.
    Evaluate \( \tilde{y}(x) \) and \( \tilde{y}'(x) \) at \( x_0 \):
    \( \tilde{y}(x_0) = Y_0y_1(x_0) + Y_1y_2(x_0) = Y_0(1) + Y_1(0) = Y_0 = y(x_0) \).
    \( \tilde{y}'(x_0) = Y_0y_1'(x_0) + Y_1y_2'(x_0) = Y_0(0) + Y_1(1) = Y_1 = y'(x_0) \).
    Since \( y(x) \) and \( \tilde{y}(x) \) are both solutions to the same IVP (same ODE and same initial conditions), by the uniqueness theorem, \( y(x) = \tilde{y}(x) \) for all \( x \).
    Thus, any solution \( y(x) \) can be written as \( y(x) = y(x_0)y_1(x) + y'(x_0)y_2(x) \), which is a linear combination of \( y_1 \) and \( y_2 \).

4.  **Method of Reduction of Order**
    If \( y_1(x) \) is a known non-trivial solution to the homogeneous second-order linear ODE \( y'' + P(x)y' + Q(x)y = 0 \), a second linearly independent solution \( y_2(x) \) can be found using the substitution \( y_2(x) = u(x)y_1(x) \). This leads to the formula:
    \[ y_2(x) = y_1(x) \int \frac{1}{y_1(x)^2} e^{-\int P(x)dx} dx \]

5.  **Solutions for Homogeneous Linear ODEs with Constant Coefficients (\( y'' + Py' + Qy = 0 \))**
    The solutions depend on the roots \( \lambda \) of the characteristic polynomial \( \lambda^2 + P\lambda + Q = 0 \). The roots are given by \( \lambda = \frac{1}{2}(-P \pm \sqrt{P^2-4Q}) \).

    *   **Case I: Distinct Real Roots (\( P^2-4Q > 0 \))**
        If \( \lambda_1 \neq \lambda_2 \) are distinct real roots, then \( \{e^{\lambda_1 x}, e^{\lambda_2 x}\} \) is a basis of solutions, and the general solution is \( y(x) = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x} \).

    *   **Case II: Repeated Real Roots (\( P^2-4Q = 0 \))**
        If \( \lambda_1 = \lambda_2 = \lambda = -P/2 \) is a repeated real root, then \( \{e^{\lambda x}, xe^{\lambda x}\} \) is a basis of solutions, and the general solution is \( y(x) = (c_1 + c_2x)e^{\lambda x} \).

    *   **Case III: Distinct Complex Conjugate Roots (\( P^2-4Q < 0 \))**
        If \( \lambda_1 = \alpha + i\beta \) and \( \lambda_2 = \alpha - i\beta \) are complex conjugate roots (where \( \alpha = -P/2 \) and \( \beta = \sqrt{Q - P^2/4} \)), then \( \{e^{\alpha x}\cos(\beta x), e^{\alpha x}\sin(\beta x)\} \) is a basis of real-valued solutions, and the general solution is \( y(x) = (c_1\cos(\beta x) + c_2\sin(\beta x))e^{\alpha x} \).

6.  **Solutions for Euler-Cauchy Equations (\( x^2y'' + axy' + by = 0 \))**
    The solutions depend on the roots \( n \) of the auxiliary equation \( n^2 + (a-1)n + b = 0 \). If \( y=x^n \) is a solution to the ODE, then \( n \) must be a root of this auxiliary equation.

    *   **Case I: Real Different Roots**
        If \( n_1 \neq n_2 \) are distinct real roots, the general solution is \( y(x) = c_1x^{n_1} + c_2x^{n_2} \).

    *   **Case II: Real Double Roots**
        If \( n_1 = n_2 = n \) is a repeated real root, the general solution is \( y(x) = (c_1 + c_2\ln x)x^n \).

    *   **Case III: Complex Conjugate Roots**
        If \( n_1 = \alpha + i\beta \) and \( n_2 = \alpha - i\beta \) are complex conjugate roots, the general solution is \( y(x) = (c_1\cos(\beta \ln x) + c_2\sin(\beta \ln x))x^\alpha \).

---