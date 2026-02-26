Here are the extracted Definitions and Theorems:

### Definitions

**Integral over an Infinite Interval** (Page 3)
If \(f\) is integrable over the interval \([a,T]\) for every \(T > a\), then the integral of \(f\) over \([a, \infty)\) is defined as
\[ \int_a^\infty f(t) dt := \lim_{T \to \infty} \int_a^T f(t) dt. \]
We say that the integral **converges** if the limit exists and is finite. Otherwise, we say the integral **diverges** or fails to exist.

**Laplace Transform** (Page 5)
Let \(f(t)\) be given for \(t > 0\). Suppose that \(f\) satisfies "certain conditions". Then the Laplace transform of \(f\), denoted by \(\mathcal{L}\{f(t)\}\) or \(F(s)\), is defined by the equation
\[ \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt, \]
whenever this improper integral converges.

**Piecewise Continuous Function** (Page 6)
A function \(f: [a,b] \to \mathbb{R}\) is said to be **piecewise continuous** if
1.  \(\exists a = t_0 < t_1 < \dots < t_{n+1} = b\) s.t. \(f\) is continuous on \((t_i, t_{i+1}) \forall i\).
2.  \(f(t_i^+)\) and \(f(t_i^-)\) exist and are finite for \(i = 0, \dots, n+1\).

A function \(f: [a, \infty) \to \mathbb{R}\) is called **piecewise continuous** if it is piecewise continuous on \([a,T] \forall T > a\).

**Functions of Exponential Order** (Page 8)
A function \(f\) is of **exponential order** if \(\exists \alpha \in \mathbb{R}, t_0 \in \mathbb{R}\) and \(M > 0\) s.t. \(\forall t \geq t_0, |f(t)| \leq Me^{\alpha t}\).

**Gamma Function** (Page 10)
The Gamma function is defined as
\[ \Gamma(z) = \int_0^\infty e^{-t} t^{z-1} dt, \]
for all complex numbers \(z\) with \(\text{Re}(z) > 0\).

**Inverse Laplace Transform** (Page 15)
The inverse Laplace transform of \(F\), denoted by \(\mathcal{L}^{-1}(F)\), is defined as \(\mathcal{L}^{-1}(F)(t) = f(t)\), where \(\mathcal{L}\{f\}(s) = F(s)\).
It follows that \(\mathcal{L}(\mathcal{L}\{f\}) = f\) and \(\mathcal{L}^{-1}(\mathcal{L}\{f\}) = f\). Similarly, \(\mathcal{L}^{-1}(F) = F\) and \(\mathcal{L}(\mathcal{L}^{-1}(F)) = F\).

### Theorems

**Existence Theorem for Laplace Transform** (Page 9)
**Theorem:** If \(f\) is a piecewise continuous function on \([0, \infty)\) and of exponential order, say \(\alpha\), then the Laplace transform is defined \(\forall s > \alpha\).

**Proof:**
Assume \(|f(t)| \leq Me^{\alpha t} \forall t \geq t_0\). Now note that
\[ \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt = \int_0^{t_0} e^{-st} f(t) dt + \int_{t_0}^\infty e^{-st} f(t) dt. \]
The first integral exists, as \(f\) is piecewise continuous on \([0, t_0]\). Now consider the second integral:
\[ \left| \int_{t_0}^\infty e^{-st} f(t) dt \right| \leq \int_{t_0}^\infty |e^{-st} f(t)| dt \leq \int_{t_0}^\infty Me^{-st} e^{\alpha t} dt = \int_{t_0}^\infty Me^{-(s-\alpha)t} dt. \]
\[ \lim_{T \to \infty} \int_{t_0}^T Me^{-(s-\alpha)t} dt = \lim_{T \to \infty} \left[ \frac{Me^{-(s-\alpha)t}}{-(s-\alpha)} \right]_{t_0}^T = \lim_{T \to \infty} \left( \frac{Me^{-(s-\alpha)t_0}}{s-\alpha} - \frac{Me^{-(s-\alpha)T}}{s-\alpha} \right). \]
This limit converges to \(\frac{Me^{-(s-\alpha)t_0}}{s-\alpha}\) if \(s-\alpha > 0\), i.e., \(s > \alpha\).
So by the comparison test, the second integral \(\int_{t_0}^\infty e^{-st} f(t) dt\) exists if \(s > \alpha\).

**Linearity of Laplace Transform** (Page 12)
**Theorem:** The Laplace transform is linear, i.e.,
\[ \mathcal{L}\{c_1f_1 + c_2f_2\} = c_1\mathcal{L}\{f_1\} + c_2\mathcal{L}\{f_2\}. \]

**First Shifting Theorem** (Page 13)
**Theorem:** If the Laplace transform of \(f\) exists for \(s > \alpha\), then for any given \(a \in \mathbb{R}\),
\[ \mathcal{L}\{e^{at}f\}(s) = \mathcal{L}\{f\}(s-a) \quad \forall s > a + \alpha. \]

**Proof:**
\[ \mathcal{L}\{e^{at}f\}(s) = \int_0^\infty e^{-st} e^{at} f(t) dt = \int_0^\infty e^{-(s-a)t} f(t) dt = \mathcal{L}\{f\}(s-a). \]
This is defined as long as \(s-a > \alpha\), i.e., \(s > a + \alpha\).

**Linearity of Inverse Laplace Transform** (Page 15)
**Property:** If \(F_1\) and \(F_2\) are the Laplace transforms of \(f_1\) and \(f_2\), i.e., \(\mathcal{L}^{-1}(F_i) = f_i\), then for \(c_i \in \mathbb{R}\),
\[ \mathcal{L}^{-1}(c_1F_1 + c_2F_2) = c_1\mathcal{L}^{-1}(F_1) + c_2\mathcal{L}^{-1}(F_2). \]

**Uniqueness of Continuous Inverse Laplace Transform** (Page 16)
**Theorem:** Let \(f(t)\) and \(g(t)\) be two functions such that \(F(s) = G(s) \forall s > \alpha\). Then \(f(t) = g(t) \forall t\), where both \(f\) and \(g\) are continuous.
Alternatively, if a continuous inverse transform exists for \(F\), then it has a unique continuous inverse transform.