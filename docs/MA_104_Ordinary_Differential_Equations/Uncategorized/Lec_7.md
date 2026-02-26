Here are the extracted definitions and theorems from the lecture notes:

---

### Definitions

1.  **n-th Order Linear ODE**
    An n-th order linear Ordinary Differential Equation (ODE) is an equation of the form
    \[ P_n(x) y^{(n)} + P_{n-1}(x)y^{(n-1)}+ \dots + P_1(x)y' + P_0(x) y=r(x) \]
    An ODE is said to be **homogeneous** if \(r(x)=0\), and **non-homogeneous** otherwise.
    In standard form, it is given by
    \[ y^{(n)} + P_{n-1}(x)y^{(n-1)} + \dots + P_1(x)y' + P_0(x) y=r(x) \]

2.  **Solution of an ODE**
    A solution of an n-th order linear ODE on some open interval \(I\) is a function \(y=h(x)\) that is defined and n times differentiable, and becomes an identity if we replace \(y\) and its derivatives \(y^{(i)}\) in the ODE by \(h(x)\) and its derivatives.

3.  **Linearly Independent/Dependent Functions**
    Consider n functions \(y_1(x), \dots, y_n(x)\) defined on some interval \(I\). These functions are called **linearly independent** on \(I\) if the equation
    \[ c_1y_1(x) + c_2y_2(x)+ \dots + c_n y_n(x) = 0 \]
    on \(I\) implies that all \(c_1, \dots, c_n\) are zero. They are called **linearly dependent** otherwise.

4.  **Basis (or Fundamental System) of Solutions**
    A basis (or fundamental system) of solutions on an interval \(I\) for an n-th order homogeneous linear ODE consists of n linearly independent solutions \(y_1, \dots, y_n\).

5.  **General Solution of Homogeneous ODE**
    A general solution of an n-th order homogeneous linear ODE is a linear combination of its basis solutions, i.e., \(y = c_1y_1 + \dots + c_n y_n\), where \(c_1, \dots, c_n\) are arbitrary constants.

6.  **General Solution of Non-homogeneous ODE**
    A general solution of a non-homogeneous ODE on an interval \(I\) is of the form \(y=y_p + y_h\), where \(y_p\) is a particular solution of the non-homogeneous ODE and \(y_h = c_1y_1 + \dots + c_n y_n\) is the general solution of the corresponding homogeneous ODE.

7.  **Initial Value Problem (IVP)**
    An initial value problem for an n-th order linear homogeneous or non-homogeneous ODE consists of the respective ODE and n initial conditions: \(y(x_0) = y_0, y'(x_0)=y_1, \dots, y^{(n-1)}(x_0) = y_{n-1}\).

8.  **Null Space of a Linear Operator**
    Given a linear operator \(L(y) := y^{(n)} + P_{n-1}(x)y^{(n-1)} + \dots + P_1(x)y' + P_0(x)y\), which can be viewed as a linear map \(L: C^n(I) \to C(I)\), the null space of L is defined as \(N(L) := \{y \in C^n(I) \mid L(y)=0\}\).

9.  **Wronskian**
    Let \(y_1, \dots, y_n \in C^{n-1}(I)\). Their Wronskian, denoted \(W(y_1, \dots, y_n)(x)\), is defined as the determinant of the matrix:
    \[
    W(y_1, \dots, y_n)(x) = \begin{vmatrix}
    y_1(x) & y_2(x) & \dots & y_n(x) \\
    y_1'(x) & y_2'(x) & \dots & y_n'(x) \\
    \vdots & \vdots & \ddots & \vdots \\
    y_1^{(n-1)}(x) & y_2^{(n-1)}(x) & \dots & y_n^{(n-1)}(x)
    \end{vmatrix}
    \]

---

### Theorems

1.  **Method of Variation of Parameters (for Second-Order ODEs)**
    Given a nonhomogeneous linear second-order ordinary differential equation
    \[ y'' + P(x)y' + q(x)y = r(x) \]
    and two linearly independent solutions \(y_1(x)\) and \(y_2(x)\) to the associated homogeneous equation \(y'' + P(x)y' + q(x)y = 0\), a particular solution \(y_p(x)\) to the nonhomogeneous equation can be found using the form \(y_p(x) = v_1(x)y_1(x) + v_2(x)y_2(x)\), where \(v_1(x)\) and \(v_2(x)\) are given by:
    \[ v_1 = -\int \frac{y_2(x)r(x)}{W(y_1, y_2)} dx \]
    \[ v_2 = \int \frac{y_1(x)r(x)}{W(y_1, y_2)} dx \]
    and \(W(y_1, y_2) = y_1 y_2' - y_1' y_2\) is the Wronskian of \(y_1\) and \(y_2\).

2.  **Fundamental Theorem for Homogeneous Linear ODEs (Linearity Principle)**
    For a homogeneous linear ODE, sums and constant multiples of solutions on some open interval \(I\) are again solutions on \(I\).

3.  **Existence & Uniqueness Theorem for IVP**
    If the coefficients \(P_0(x), \dots, P_{n-1}(x)\) of the standard form n-th order linear ODE (i.e., \(y^{(n)} + P_{n-1}(x)y^{(n-1)} + \dots + P_1(x)y' + P_0(x)y=r(x)\)) are continuous on some open interval \(I\) and \(x_0\) is in \(I\), then the Initial Value Problem with initial conditions at \(x_0\) has a unique solution \(y(x)\) on \(I\).

4.  **Theorem (Linear Dependence & Independence of Solutions via Wronskian)**
    Let the homogeneous ODE \(y^{(n)} + P_{n-1}(x)y^{(n-1)} + \dots + P_1(x)y' + P_0(x)y=0\) have continuous coefficients \(P_0(x), \dots, P_{n-1}(x)\) on an open interval \(I\). Then its n solutions \(y_1, \dots, y_n\) are linearly dependent on \(I\) if and only if their Wronskian \(W(y_1, \dots, y_n)(x)\) is zero for some \(x=x_0\) on \(I\). Furthermore, if \(W\) is zero for some \(x=x_0\), then \(W\) is identically zero on \(I\).
    *Remark:* If there is an \(x_0 \in I\) at which \(W(y_1, \dots, y_n)(x_0) \neq 0\), then \(y_1, \dots, y_n\) are linearly independent on \(I\), and thus they form a basis of solutions for the homogeneous ODE on \(I\).

5.  **Existence of a General Solution for Homogeneous ODEs**
    If the coefficients \(P_0(x), \dots, P_{n-1}(x)\) of the homogeneous ODE are continuous on some open interval \(I\), then the homogeneous ODE has a general solution on \(I\).
    *Proof Sketch (Fundamental):* By the existence and uniqueness theorem, for each \(k=0,1,\dots,n-1\), a unique solution \(y_{k+1}(x)\) exists for the IVP with \(y^{(k)}(x_0)=1\) and \(y^{(j)}(x_0)=0\) for \(j \neq k\). The Wronskian of these solutions at \(x_0\) is
    \[
    W(y_1, \dots, y_n)(x_0) = \begin{vmatrix}
    y_1(x_0) & \dots & y_n(x_0) \\
    \vdots & \ddots & \vdots \\
    y_1^{(n-1)}(x_0) & \dots & y_n^{(n-1)}(x_0)
    \end{vmatrix} = \begin{vmatrix}
    1 & 0 & \dots & 0 \\
    0 & 1 & \dots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \dots & 1
    \end{vmatrix} = 1 \neq 0
    \]
    Since the Wronskian is non-zero at \(x_0\), these \(n\) solutions are linearly independent and thus form a basis, leading to a general solution.

6.  **Rules for Homogeneous Linear ODEs with Constant Coefficients**
    Consider the homogeneous ODE \(y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_1y' + a_0y = 0\).
    By substituting \(y=e^{\lambda x}\), we obtain the **characteristic equation**:
    \[ \lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0 = 0 \]
    If \(\lambda_0\) is a root of this equation, then \(e^{\lambda_0 x}\) is a solution of the ODE. The form of linearly independent solutions depends on the nature of the roots:
    *   **Distinct Real Roots:** If \(\lambda_1, \dots, \lambda_n\) are distinct real roots, then \(e^{\lambda_1 x}, \dots, e^{\lambda_n x}\) constitute a basis of solutions.
    *   **Simple Complex Roots:** If \(\lambda = \alpha+i\beta\) is a complex root, then its conjugate \(\bar{\lambda} = \alpha-i\beta\) is also a root (since coefficients are real). The two corresponding linearly independent solutions are \(e^{\alpha x} \cos \beta x\) and \(e^{\alpha x} \sin \beta x\).
    *   **Multiple Real Roots:** If \(\lambda_1\) is a real root of order \(m \le n\), then \(m\) corresponding linearly independent solutions are \(e^{\lambda_1 x}, xe^{\lambda_1 x}, x^2e^{\lambda_1 x}, \dots, x^{m-1}e^{\lambda_1 x}\).
        *Proof Idea (Fundamental):* If \(L\) is the differential operator associated with the ODE, then \(L(e^{\lambda x}) = (\lambda-\lambda_1)^m h(\lambda) e^{\lambda x}\). Differentiating with respect to \(\lambda\) shows that \(L(xe^{\lambda x}) = \frac{\partial}{\partial \lambda} L(e^{\lambda x})\). For \(\lambda=\lambda_1\), \(L(e^{\lambda_1 x})=0\), and if \(m \ge 2\), then \(\frac{\partial}{\partial \lambda} L(e^{\lambda x})|_{\lambda=\lambda_1} = 0\), which implies \(L(xe^{\lambda_1 x})=0\). This process continues up to \(m-1\) differentiations, generating the family of solutions.
    *   **Multiple Complex Roots:** If \(\lambda=\alpha+i\beta\) is a complex root of order \(m\), then \(\bar{\lambda}=\alpha-i\beta\) is also a root of order \(m\). The \(2m\) corresponding linearly independent solutions are:
        \(e^{\alpha x} \cos \beta x, e^{\alpha x} \sin \beta x\)
        \(xe^{\alpha x} \cos \beta x, xe^{\alpha x} \sin \beta x\)
        \(\dots\)
        \(x^{m-1}e^{\alpha x} \cos \beta x, x^{m-1}e^{\alpha x} \sin \beta x\)

7.  **Modification Rule for Method of Undetermined Coefficients**
    If a term in the initially chosen form of the particular solution \(y_p(x)\) is also a solution of the corresponding homogeneous equation, then that term must be multiplied by \(x^k\), where \(k\) is the smallest positive integer such that \(x^k \times (\text{original term})\) is *not* a solution of the homogeneous equation.

---