Here are the extracted definitions and theorems from the lecture notes:

---

### **Theorem (Existence and Uniqueness Theorem for IVPs)**
Given an Initial Value Problem (IVP): \(y' = f(x,y)\), with \(y(x_0)=y_0\).
If \(f(x,y)\) and its partial derivative \(\frac{\partial f}{\partial y}\) are continuous in a rectangle \(D: |\tilde{x}| \le \alpha\) and \(|\tilde{y}| \le b\) (where \(\tilde{x}=x-x_0\) and \(\tilde{y}=y-y_0\)), then there exists a unique solution \(y=\phi(x)\) of the IVP in some interval \(|\tilde{x}| \le \alpha\).

### **Definition (Integral Equation)**
An equation that contains an integral of the unknown function is called an integral equation. For an IVP \(y'=f(x,y)\) with \(y(0)=0\), its equivalent integral equation is given by:
\[ \phi(x) = \int_0^x f(\tilde{x}, \phi(\tilde{x})) d\tilde{x} \]

### **Theorem (Equivalence of IVP and Integral Equation)**
The Initial Value Problem (IVP) \(y'=f(x,y)\) with \(y(0)=0\) and its corresponding integral equation \(\phi(x) = \int_0^x f(\tilde{x}, \phi(\tilde{x})) d\tilde{x}\) are equivalent; they have the same set of solutions.

### **Definition (Picard's Iteration Method)**
For an IVP \(y'=f(x,y)\) with \(y(0)=0\), Picard's iteration method generates a sequence of successive approximations \(\{\phi_k(x)\}\) as follows:
1.  Choose an initial approximation \(\phi_0(x)\) such that \(\phi_0(0)=0\). The simplest choice is \(\phi_0(x)=0\).
2.  The k-th approximation \(\phi_k(x)\) is then given by the integral:
    \[ \phi_k(x) = \int_0^x f(\tilde{x}, \phi_{k-1}(\tilde{x})) d\tilde{x} \]

### **Theorem (Convergence of Picard Iterates)**
Under suitable conditions (specifically, if \(f(x,y)\) and \(\frac{\partial f}{\partial y}\) are continuous in a rectangle), the sequence of Picard iterates \(\{\phi_n(x)\}\) converges to a function \(\phi(x)\). This limit function \(\phi(x)\) is a solution of the given Initial Value Problem.

### **Fundamental Proof (Uniqueness of Solution)**
To prove the uniqueness of the solution to an IVP \(y'=f(x,y)\) with \(y(0)=0\):
1.  **Assumption:** Assume there are two distinct solutions, \(\phi(x)\) and \(\psi(x)\), satisfying the IVP and thus its equivalent integral equation:
    \[ \phi(x) = \int_0^x f(\tilde{x}, \phi(\tilde{x})) d\tilde{x} \quad \text{and} \quad \psi(x) = \int_0^x f(\tilde{x}, \psi(\tilde{x})) d\tilde{x} \]
2.  **Difference Equation:** Subtracting the two equations and taking absolute values:
    \[ |\phi(x) - \psi(x)| = \left| \int_0^x [f(\tilde{x}, \phi(\tilde{x})) - f(\tilde{x}, \psi(\tilde{x}))] d\tilde{x} \right| \le \int_0^x |f(\tilde{x}, \phi(\tilde{x})) - f(\tilde{x}, \psi(\tilde{x}))| d\tilde{x} \]
3.  **Lipschitz Condition:** Since \(\frac{\partial f}{\partial y}\) is continuous, \(f(x,y)\) satisfies a Lipschitz condition in the rectangle \(D\):
    \[ |f(x,y_2) - f(x,y_1)| \le K |y_2 - y_1| \]
    for some constant \(K\). Applying this to the inequality:
    \[ |\phi(x) - \psi(x)| \le \int_0^x K |\phi(\tilde{x}) - \psi(\tilde{x})| d\tilde{x} \]
4.  **Applying Gronwall's Lemma (or direct integration):** Let \(u(x) = \int_0^x |\phi(\tilde{x}) - \psi(\tilde{x})| d\tilde{x}\). Then \(u(0)=0\) and \(u'(x) = |\phi(x) - \psi(x)|\). The inequality becomes \(u'(x) \le K u(x)\).
    This can be rewritten as \(u'(x) - K u(x) \le 0\). Multiplying by \(e^{-Kx}\), we get \(\frac{d}{dx} [e^{-Kx} u(x)] \le 0\).
    Integrating from \(0\) to \(x\): \(e^{-Kx} u(x) - e^0 u(0) \le 0\). Since \(u(0)=0\), this simplifies to \(e^{-Kx} u(x) \le 0\).
5.  **Conclusion:** As \(e^{-Kx} > 0\) and \(u(x) \ge 0\) (being an integral of an absolute value), the only way for \(e^{-Kx} u(x) \le 0\) to hold is if \(u(x) = 0\).
    If \(u(x) = 0\), then \(u'(x) = |\phi(x) - \psi(x)| = 0\), which implies \(\phi(x) = \psi(x)\). Therefore, the solution to the IVP is unique.