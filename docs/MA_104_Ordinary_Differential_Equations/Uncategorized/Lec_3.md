Here are the extracted Definitions and Theorems from the lecture notes:

---

### **Lecture 3: Ordinary Differential Equations**

#### **Definitions and Forms of First-Order ODEs**

**Definition: Linear First-Order ODE**
A first-order ODE \( y' = f(x,y) \) is called **linear** if \( f(x,y) \) depends linearly on the variable \( y \), i.e., \( f(x,y) = a(x)y + b(x) \).

**Definition: Standard form of a Linear First-Order ODE**
The standard form of a linear 1st order ODE is:
\[ y' + p(x)y = r(x) \]

**Definition: Integrating Factor**
For a linear 1st order ODE \( y' + p(x)y = r(x) \), a function \( \mu(x) \) which transforms the left-hand side into a derivative of a product, specifically \( \frac{d}{dx}(\mu(x)y) \), is called an **integrating factor**.

#### **Theorems for Linear First-Order ODEs**

**Theorem: Formula for the Integrating Factor**
For a linear first-order ODE \( y' + p(x)y = r(x) \), the integrating factor \( \mu(x) \) is given by:
\[ \mu(x) = e^{\int p(x) dx} \]

**Theorem: General Solution of a Linear First Order ODE**
For a linear first-order ODE \( y' + p(x)y = r(x) \), the general solution is given by:
\[ y = e^{-\int p(x)dx} \left[ \int r(x) \left(e^{\int p(x)dx}\right) dx + C \right] \]

#### **Bernoulli Equation**

**Definition: Bernoulli Equation**
An equation of the form \( y' + Q(x)y = R(x) y^\alpha \), for a given fixed real number \( \alpha \), is called a **Bernoulli Differential Equation**.
*Note:* If \( \alpha = 0 \) or \( \alpha = 1 \), the Bernoulli equation is linear.

**Theorem: Transformation of Bernoulli Equation to Linear Form**
Let \( \alpha \neq 0, 1 \). The transformation \( u = y^{1-\alpha} \) reduces the Bernoulli equation \( y' + Q(x)y = R(x) y^\alpha \) to a linear equation in \( u \).
*Proof:*
Given \( u = y^{1-\alpha} \), differentiating with respect to \( x \) gives \( u' = (1-\alpha)y^{-\alpha}y' \).
Multiply the Bernoulli equation by \( (1-\alpha)y^{-\alpha} \):
\( (1-\alpha)y^{-\alpha}y' + (1-\alpha)Q(x)y^{-\alpha}y = (1-\alpha)R(x)y^{-\alpha}y^\alpha \)
\( (1-\alpha)y^{-\alpha}y' + (1-\alpha)Q(x)y^{1-\alpha} = (1-\alpha)R(x) \)
Substitute \( u \) and \( u' \):
\( u' + (1-\alpha)Q(x)u = (1-\alpha)R(x) \)
This is a linear ODE in \( u \).

#### **Existence and Uniqueness for 1st Order IVP**

**Conclusion: Behavior of solutions for a first-order IVP**
A first-order Initial Value Problem (IVP) \( y' = f(x,y) \) with \( y(x_0)=y_0 \) may have no solution, a unique solution, or infinitely many solutions.

**Theorem: Existence Theorem for 1st order IVP**
Consider a 1st order IVP: \( y'(x) = f(x,y) \) with \( y(x_0)=y_0 \).
Suppose the function \( f(x,y) \) is continuous for all points \( (x,y) \) in some rectangle \( D: |x-x_0| \leq a, |y-y_0| \leq b \) and bounded in \( D \), i.e., there exists \( K > 0 \) such that \( |f(x,y)| \leq K \) for all \( (x,y) \in D \).
Then the IVP has at least one solution \( y(x) \).
*Remark:* This solution exists at least for all \( x \) with \( |x-x_0| < \alpha \), where \( \alpha = \min\{a, b/K\} \).

**Theorem: Uniqueness Theorem for 1st order IVP**
Consider a 1st order IVP: \( y'(x) = f(x,y) \) with \( y(x_0)=y_0 \).
Let \( f \) and its partial derivative \( \frac{\partial f}{\partial y} \) be continuous for all \( (x,y) \) in some rectangle \( D: |x-x_0| \leq a, |y-y_0| \leq b \) and bounded, i.e., \( |f(x,y)| \leq K \) and \( \left|\frac{\partial f}{\partial y}(x,y)\right| \leq M \) for all \( (x,y) \in D \).
Then the IVP has at most one solution (and hence precisely one solution due to the Existence Theorem).

**Definition: Lipschitz Condition**
A function \( f(x,y) \) satisfies a **Lipschitz condition** with respect to \( y \) on a domain \( D \) if there exists a constant \( M>0 \) such that for any \( (x, y_1), (x, y_2) \in D \),
\[ |f(x,y_2) - f(x,y_1)| \leq M |y_2 - y_1| \]
*Note:* The condition \( \left|\frac{\partial f}{\partial y}(x,y)\right| \leq M \) can be replaced by this weaker Lipschitz condition for uniqueness.

**Theorem: Existence and Uniqueness for Linear First Order IVP**
Consider the differential equation \( y' + a(x)y = b(x) \), along with the initial value condition \( y(x_0)=y_0 \).
Let \( a(x) \) and \( b(x) \) be continuous functions for all \( x \) with \( |x-x_0| \leq a \).
Then the differential equation has a unique solution \( y \) on the interval \( (x_0-a, x_0+a) \).

**Remark: Continuity of \( f(x,y) \) is not sufficient for uniqueness**
The continuity of \( f(x,y) \) alone is not enough to guarantee the uniqueness of the solution for an IVP. Conditions on \( \frac{\partial f}{\partial y} \) (or the Lipschitz condition) are also required for uniqueness.

#### **Orthogonal Trajectories**

**Definition: Orthogonal Trajectories**
A new family of curves that intersect a given family of curves at right angles are called **orthogonal trajectories** of the given curves.

**Definition: Angle of Intersection of Curves**
The angle of intersection between two curves is defined to be the angle between the tangents of the curves at their intersection point.

**Definition: One-Parameter Family of Curves**
A **one-parameter family of curves** is a collection of curves defined by a single equation with one arbitrary constant (parameter).

**Method: Finding the Differential Equation of a Family of Curves**
Given a family of curves defined by \( f(x,y,c)=0 \):
1.  Differentiate \( f(x,y,c)=0 \) with respect to \( x \) to obtain an equation involving \( x, y, y', c \).
2.  Eliminate the constant \( c \) from the original equation and the differentiated equation.
The resulting equation, \( F(x, y, y') = 0 \), is the desired differential equation of the family.

**Method: Finding Orthogonal Trajectories**
To find the orthogonal trajectories for a given family of curves:
1.  Find the differential equation \( y' = f(x,y) \) for the given family of curves.
2.  The differential equation for the orthogonal trajectories, denoted \( \tilde{y}' \), is given by \( \tilde{y}' = -\frac{1}{f(x,\tilde{y})} \).
3.  Solve this new ODE \( \frac{d\tilde{y}}{dx} = -\frac{1}{f(x,\tilde{y})} \) to find the family of orthogonal trajectories.

---