**Theorem (Uniqueness Theorem)**

Consider the Initial Value Problem (IVP):
\[ y' = f(x,y) \quad \text{with} \quad y(x_0)=y_0 \]
Suppose that \(f\) and its partial derivative \(\frac{\partial f}{\partial y}\) are continuous (\(^{\ast}\)) with respect to \((x,y)\) in a domain \(D\), defined by \(|x-x_0|<a\) and \(|y-y_0|<b\). Furthermore, suppose they are bounded on \(D\), i.e.,
\[ |f(x,y)| \le K \quad \text{and} \quad \left|\frac{\partial f}{\partial y}\right| \le M \quad \forall (x,y) \in D \]
Then the IVP has at most one solution \(y(x)\) for \(x\) with \(|x-x_0|<\alpha\), where \(\alpha = \min \{a, b/K\}\).