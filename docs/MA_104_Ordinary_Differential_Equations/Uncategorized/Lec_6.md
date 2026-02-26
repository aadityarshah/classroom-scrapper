Here are the extracted definitions and theorems from the lecture notes:

**Definitions**

*   **Wronskian**
    For given functions \(y_1, y_2 \in C^1(I)\), the Wronskian is a function of \(x\) defined by:
    \[ W(y_1, y_2)(x) = \begin{vmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \end{vmatrix} = y_1(x)y_2'(x) - y_2(x)y_1'(x) \]
    It can be viewed as a map \(W(y_1, y_2): I \rightarrow \mathbb{R}\).

*   **Linear Differential Operator**
    For \(n \ge 1\), consider the vector space \(C^n(I) = \{f: I \rightarrow \mathbb{R} \mid f, f', \dots, f^{(n-1)} \text{ are contn}\}\). Given a 2nd order linear homogeneous ODE: \(y'' + P(x)y' + q(x)y = 0\), where \(P(x)\) and \(q(x)\) are continuous functions on \(I\), we can define a map \(L: C^2(I) \rightarrow C(I)\) as:
    \[ L(f) := \frac{d^2f}{dx^2} + P(x)\frac{df}{dx} + q(x)f = f'' + P(x)f' + q(x)f \]
    The map \(L\) is often denoted by \(D^2 + P(x)D + q(x)\), so \(Ly = (D^2 + P(x)D + q(x))y\).

*   **Annihilator**
    An annihilator of a function \(f\) is a differential map \(A\) such that \(Af = 0\).
    (Examples of annihilators for common functions include: \(A=D-m\) for \(f=e^{mx}\), \(A=D^{n+1}\) for \(f=x^n\), \(A=D^2+a^2\) for \(f=\sin(ax+b)\) or \(\cos(ax+b)\), and \(A=(D-m)^{n+1}\) for \(f=x^n e^{mx}\).)

**Theorems**

*   **Theorem: Wronskian and Linear Independence (Part 1)**
    Suppose \(y_1(x)\) and \(y_2(x)\) are linearly dependent (L.D.) and differentiable on \(I=(a,b)\). Then \(W(y_1, y_2)(x) = 0 \ \forall x \in I\).

    *Proof:*
    If \(y_1\) and \(y_2\) are L.D., then there exist constants \(c_1, c_2\), not both zero, such that \(c_1 y_1 + c_2 y_2 = 0\). Differentiating this gives \(c_1 y_1' + c_2 y_2' = 0\). This system can be written in matrix form:
    \[ \begin{pmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \]
    Since not both \(c_1, c_2\) are zero, the determinant of the coefficient matrix must be zero. This determinant is precisely the Wronskian \(W(y_1, y_2)(x)\). Thus, \(W(y_1, y_2)(x) = 0 \ \forall x \in I\).

*   **Note on Wronskian and Linear Independence**
    If \(W(y_1, y_2)(x) \neq 0\) for some \(x \in I\), then \(y_1\) and \(y_2\) are linearly independent (L.I.).

*   **Theorem: Vanishing Property of Wronskian (Abel's Theorem)**
    Suppose that \(y_1\) and \(y_2\) are two solutions of the 2nd order linear homogeneous ODE \(y'' + P(x)y' + q(x)y = 0\) on an interval \(I\). Moreover, assume both \(P(x)\) and \(q(x)\) are continuous on \(I\). Then the Wronskian \(W(y_1, y_2)(x)\) is given by:
    \[ W(y_1, y_2)(x) = c e^{-\int P(x) dx} \]
    where the constant \(c\) depends on \(y_1\) and \(y_2\), but not on \(x\).

    *Proof:*
    The Wronskian is \(W = y_1 y_2' - y_1' y_2\). Differentiating with respect to \(x\):
    \(W' = (y_1 y_2'' + y_1' y_2') - (y_1' y_2' + y_1'' y_2) = y_1 y_2'' - y_1'' y_2\).
    Since \(y_1\) and \(y_2\) are solutions to \(y'' + P(x)y' + q(x)y = 0\), we have:
    \(y_1'' = -P(x)y_1' - q(x)y_1\)
    \(y_2'' = -P(x)y_2' - q(x)y_2\)
    Substitute these into the expression for \(W'\):
    \(W' = y_1(-P(x)y_2' - q(x)y_2) - y_2(-P(x)y_1' - q(x)y_1)\)
    \(W' = -P(x)y_1 y_2' - q(x)y_1 y_2 + P(x)y_1' y_2 + q(x)y_1 y_2\)
    \(W' = -P(x)(y_1 y_2' - y_1' y_2)\)
    \(W' = -P(x)W\)
    This is a first-order linear ODE: \(\frac{dW}{dx} + P(x)W = 0\). Separating variables and integrating:
    \(\frac{dW}{W} = -P(x)dx\)
    \(\ln|W| = -\int P(x)dx + C_0\)
    \(W(x) = e^{-\int P(x)dx + C_0} = e^{C_0} e^{-\int P(x)dx}\)
    Let \(c = e^{C_0}\). Then \(W(y_1, y_2)(x) = c e^{-\int P(x)dx}\).

*   **Remarks on Abel's Theorem:**
    *   Either \(W(y_1, y_2)(x) = 0 \ \forall x \in I\) (when \(c=0\)) or \(W(y_1, y_2)(x) \neq 0 \ \forall x \in I\) (when \(c \neq 0\)). It is sufficient to evaluate \(W(x_0)\) at any convenient point \(x_0 \in I\).
    *   If \(\{y_1, y_2\}\) and \(\{\tilde{y}_1, \tilde{y}_2\}\) are two fundamental sets of solutions, then \(W(y_1, y_2) = \tilde{c} \cdot W(\tilde{y}_1, \tilde{y}_2)\), meaning the Wronskian is determined up to a multiplicative constant.

*   **Theorem: Converse for L.I. Solutions**
    Suppose that \(y_1\) and \(y_2\) are solutions of \(y'' + P(x)y' + q(x)y=0\). Then \(y_1\) and \(y_2\) are L.D. if and only if \(W(y_1, y_2)=0\).

    *Proof:*
    The direction (\(\Rightarrow\)) that L.D. implies \(W=0\) was proven above.
    For the direction (\(\Leftarrow\)) that \(W=0\) implies L.D.:
    Assume \(W(y_1, y_2)(x) = y_1(x)y_2'(x) - y_1'(x)y_2(x) = 0\) for all \(x \in I\).
    If \(y_1(x)=0\) for all \(x\), then \(y_1\) and \(y_2\) are L.D. (take \(c_1=1, c_2=0\)).
    Assume \(y_1(x_0) \neq 0\) for some \(x_0 \in I\). Since \(y_1\) is continuous, there is an open interval \(J \subseteq I\) containing \(x_0\) where \(y_1(x) \neq 0\).
    On \(J\), we can divide \(W(y_1, y_2)(x)=0\) by \(y_1(x)^2\):
    \[ \frac{y_1(x)y_2'(x) - y_1'(x)y_2(x)}{y_1(x)^2} = 0 \]
    The left side is the derivative of the quotient \(\left(\frac{y_2}{y_1}\right)'\).
    So, \(\left(\frac{y_2}{y_1}\right)' = 0\), which implies \(\frac{y_2(x)}{y_1(x)} = k\) for some constant \(k\) on \(J\).
    Thus, \(y_2(x) = k y_1(x)\) on \(J\), meaning \(y_1\) and \(y_2\) are L.D. on \(J\).
    To extend this to the entire interval \(I\), consider the initial value problem (IVP): \(y'' + P(x)y' + q(x)y = 0\) with \(y(x_0)=y_2(x_0)\) and \(y'(x_0)=y_2'(x_0)\).
    We know that \(y_2(x)\) is a solution to this IVP.
    Also, consider \(k y_1(x)\). At \(x_0\), \(k y_1(x_0) = y_2(x_0)\).
    Since \(W(y_1, y_2)(x_0) = 0\) and \(y_1(x_0) \neq 0\), we have \(y_2'(x_0) = \frac{y_1'(x_0)y_2(x_0)}{y_1(x_0)} = k y_1'(x_0)\).
    So, \(k y_1(x)\) also satisfies the same IVP as \(y_2(x)\) at \(x_0\). By the uniqueness theorem for solutions of ODEs (assuming \(P(x)\) and \(q(x)\) are continuous), we must have \(y_2(x) = k y_1(x)\) for all \(x \in I\). Therefore, \(y_1\) and \(y_2\) are L.D. on \(I\).

*   **Property of L.I. Solutions**
    Consider an ODE \(y'' + P(x)y' + q(x)y=0\). If \(y_1\) and \(y_2\) are linearly independent solutions on \(I\), then for any \(x_0 \in I\):
    1.  Both \(y_1(x_0)\) and \(y_2(x_0)\) cannot be zero.
    2.  Both \(y_1'(x_0)\) and \(y_2'(x_0)\) cannot be zero.

*   **Theorem: Structure of General Solution for Nonhomogeneous ODEs**
    A general solution of the nonhomogeneous ODE \(y'' + P(x)y' + q(x)y = r(x)\) on an open interval \(I\) is of the form \(y(x) = y_p(x) + y_h(x)\), where \(y_h = c_1y_1 + c_2y_2\) is a general solution of the associated homogeneous ODE \(y'' + P(x)y' + q(x)y = 0\) on \(I\), and \(y_p\) is any particular solution of the nonhomogeneous ODE on \(I\) containing no arbitrary constants.

*   **Method of Undetermined Coefficients Rules**
    For an ODE \(y'' + py' + qy = r(x)\) with constant coefficients \(p\) and \(q\):

    *   **(a) Basic Rule:** If \(r(x)\) is a function type listed in a standard table for this method (e.g., \(k e^{\gamma x}\), \(k x^n\), \(k \cos(\omega x)\), \(k \sin(\omega x)\), \(k e^{\alpha x} \cos(\omega x)\), \(k e^{\alpha x} \sin(\omega x)\)), choose \(y_p\) from the corresponding form in the table and determine its undetermined coefficients by substituting \(y_p\) and its derivatives into the ODE.

    *   **(b) Modification Rule:** If a term in your initial choice for \(y_p\) (based on the basic rule) happens to be a solution of the homogeneous ODE \(y'' + py' + qy = 0\), multiply this term by \(x\) (or by \(x^2\) if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).

    *   **(c) Sum Rule:** If \(r(x)\) is a sum of functions (e.g., \(r(x) = r_1(x) + r_2(x)\)), choose for \(y_p\) the sum of the particular solutions corresponding to each \(r_i(x)\) separately (i.e., \(y_p = y_{p_1} + y_{p_2}\)).

*   **Principle of Annihilator Method**
    Given an inhomogeneous ODE \(L y = r(x)\), if \(r(x)\) admits an annihilator \(A\) (i.e., \(A r(x) = 0\)), then any solution \(y\) of \(L y = r(x)\) is also a solution of the 'new' homogeneous ODE \((A \circ L)(y) = A(L(y)) = 0\). This new ODE is generally of higher order than \(L\).