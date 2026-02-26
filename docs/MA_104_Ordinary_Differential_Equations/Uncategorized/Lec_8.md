Here are the extracted Definitions and Theorems from the lecture notes:

---

### Definitions

*   **Definition: Power Series**
    A power series is an infinite series of the form
    \[ \sum_{m=0}^\infty a_m (x-x_0)^m = a_0 + a_1(x-x_0) + a_2(x-x_0)^2 + \dots \]
    Here, the constants \(a_0, a_1, \dots\) are called the **coefficients** of the series, and the constant \(x_0\) is called the **center** of the series.

*   **Definition: Convergence of a Power Series**
    A power series \(\sum_{m=0}^\infty a_m (x-x_0)^m\) is said to **converge** at a point \(x\) if the sequence \(\{S_N(x)\}\) of partial sums, defined as \(S_N(x) = \sum_{m=0}^N a_m(x-x_0)^m\), is convergent, i.e., \(\lim_{N\to\infty} S_N(x)\) exists.

*   **Definition: Absolute Convergence**
    The series \(\sum_{m=0}^\infty a_m (x-x_0)^m\) is said to **converge absolutely** at a point \(x\) if the series \(\sum_{m=0}^\infty |a_m (x-x_0)^m| = \sum_{m=0}^\infty |a_m||x-x_0|^m\) converges.

*   **Definition: Radius and Interval of Convergence**
    There exists a positive real number \(P\), called the **radius of convergence**, such that \(\sum_{m=0}^\infty a_m(x-x_0)^m\) converges for \(|x-x_0| < P\) and diverges for \(|x-x_0| > P\). The interval \(|x-x_0| < P\) is called the **interval of convergence**.

*   **Definition: Taylor Series**
    The series \(f(x) = \sum_{n=0}^\infty a_n(x-x_0)^n = \sum_{n=0}^\infty \frac{f^{(n)}(x_0)}{n!} (x-x_0)^n\) is called the **Taylor series** for the function \(f(x)\) about \(x=x_0\). The value of \(a_n\) is given by \(a_n = \frac{f^{(n)}(x_0)}{n!}\).

*   **Definition: Analytic Function**
    A function \(h(x)\) is called **analytic** at a point \(x=x_0\) if it can be represented by a power series (Taylor series) in powers of \(x-x_0\) with a positive radius of convergence.

### Theorems

*   **Theorem: Absolute Convergence Implies Convergence**
    If a series converges absolutely, then the series also converges.

*   **Theorem: Convergence Property of Power Series**
    If a power series \(\sum_{n=0}^\infty a_n (x-x_0)^n\) converges at \(x=x_1\), it converges absolutely for \(|x-x_0| < |x_1-x_0|\). If it diverges at \(x=x_1\), it diverges for \(|x-x_0| > |x_1-x_0|\).

*   **Theorem: Root Test**
    The root test states that a power series \(\sum_{n=0}^\infty a_n(x-x_0)^n\) converges if \(C := \limsup_{n\to\infty} \sqrt[n]{|a_n (x-x_0)^n|} = \limsup_{n\to\infty} (\sqrt[n]{|a_n|}) |x-x_0| < 1\) and diverges if \(C > 1\). The radius of convergence \(P\) is given by \(P = \frac{1}{\limsup_{n\to\infty} \sqrt[n]{|a_n|}}\).

*   **Theorem: Ratio Test**
    The ratio test states that a power series \(\sum_{n=0}^\infty a_n(x-x_0)^n\) converges if \(L := \lim_{n\to\infty} \frac{|a_{n+1} (x-x_0)^{n+1}|}{|a_n (x-x_0)^n|} < 1\) and diverges if \(L > 1\). The radius of convergence \(P\) is given by \(P = \lim_{n\to\infty} \left|\frac{a_n}{a_{n+1}}\right|\).

*   **Theorem: Arithmetic of Power Series**
    Suppose \(\sum_{m=0}^\infty a_m(x-x_0)^m\) and \(\sum_{n=0}^\infty b_n(x-x_0)^n\) converge to \(f(x)\) and \(g(x)\) respectively for \(|x-x_0| < P\), where \(P>0\). Then:
    1.  \(f(x) \pm g(x) = \sum_{n=0}^\infty (a_n \pm b_n) (x-x_0)^n\).
    2.  \(f(x)g(x) = \sum_{n=0}^\infty c_n (x-x_0)^n\), where \(c_n = a_0 b_n + a_1 b_{n-1} + \dots + a_n b_0\).
    Both resulting series converge at least for \(|x-x_0| < P\).

*   **Theorem: Differentiability of Power Series**
    Suppose \(\sum_{n=0}^\infty a_n(x-x_0)^n\) converges to \(f(x)\) for \(|x-x_0| < P\), where \(P \ge 0\). Then the function \(f\) is continuous and has derivatives of all orders for \(|x-x_0| < P\). Moreover, \(f', f'', \dots\) can be computed by differentiating the series term wise:
    \[ f'(x) = \sum_{n=1}^\infty n a_n (x-x_0)^{n-1} \]
    \[ f''(x) = \sum_{n=2}^\infty n(n-1) a_n (x-x_0)^{n-2} \]
    Each differentiated series converges absolutely for \(|x-x_0| < P\).

*   **Theorem: Identity Theorem for Power Series (Vanishing of Coefficients)**
    If \(P > 0\) and \(\sum_{n=0}^\infty a_n(x-x_0)^n = 0\) for all \(x\) such that \(|x-x_0| < P\), then \(a_n = 0\) for all \(n \ge 0\).

*   **Theorem: Existence of Power Series Solutions for ODEs**
    For the ordinary differential equation \(y'' + P(x) y' + Q(x) y = R(x)\) (referred to as (1)), if the functions \(P(x), Q(x), R(x)\) are analytic at \(x=x_0\), then every solution of (1) is analytic at \(x=x_0\) and can thus be represented by a power series in powers of \(x-x_0\) with a radius of convergence \(P > 0\).

---