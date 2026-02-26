Here are the extracted definitions and theorems from the lecture notes:

**Definition (Directional Derivative).**
Let \( f: R^2 \rightarrow R \), \( (a, b) \in R^2 \) and let \( U := (u, v) \in R^2 \) be a unit vector, i.e., \( ||U|| = \sqrt{u^2 + v^2} = 1 \). The directional derivative of \( f \) at \( (a, b) \) in the direction \( U \) is defined by (provided the limit exists)
\[ D_{(a,b)} f(U) := \lim_{h \rightarrow 0} \frac{f((a,b)+h(u,v))-f(a,b)}{h} = \lim_{h \rightarrow 0} \frac{f(a+hu,b+hv)-f(a,b)}{h} \]
In particular, \( D_{(a,b)}f(e_1) = f_x(a, b) \) and \( D_{(a,b)}f(e_2) = f_y(a, b) \), where \( e_1 = (1, 0) \) and \( e_2 = (0, 1) \).

**Definition (Partial Derivative with respect to x).**
The partial derivative of \( f(x, y) \) with respect to \( x \) at the point \( (x_0, y_0) \) is
\[ \frac{\partial f}{\partial x}\Big|_{(x_0, y_0)} = \lim_{h \rightarrow 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h} \]
provided the limit exists.

**Definition (Partial Derivative with respect to y).**
The partial derivative of \( f(x, y) \) with respect to \( y \) at the point \( (x_0, y_0) \) is
\[ \frac{\partial f}{\partial y}\Big|_{(x_0, y_0)} = \lim_{h \rightarrow 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h} \]
provided the limit exists.

**Theorem (Mixed Derivative Theorem).**
If \( f(x, y) \) and its partial derivatives \( f_x, f_y, f_{xy}, \) and \( f_{yx} \) are defined throughout an open region containing a point \( (a, b) \) and are all continuous at \( (a, b) \), then
\[ f_{xy}(a, b) = f_{yx}(a, b). \]

**Theorem (Chain Rule for Functions of One Independent Variable and Two Intermediate Variables).**
If \( z = f(x, y) \) is differentiable and \( x \) and \( y \) are differentiable functions of \( t \), then \( z \) is a differentiable function of \( t \) and
\[ \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}. \]

**Definition (Total Differential).**
Let \( F: R^2 \rightarrow R \) be a two-variable function that admits continuous first-order partial derivatives in a region \( D \). The total differential, denoted by \( dF \), is defined as
\[ dF = \frac{\partial F}{\partial x} dx + \frac{\partial F}{\partial y} dy. \]

**Definition (Exact Differential Equation).**
An ordinary differential equation of the form \( M(x, y) dx + N(x, y) dy = 0 \) is called an exact differential equation if there exists a function \( u(x, y) \) such that \( \frac{\partial u}{\partial x} = M(x, y) \) and \( \frac{\partial u}{\partial y} = N(x, y) \).

**Theorem (Condition for Exactness).**
Let the functions \( M(x, y) \), \( N(x, y) \) and their partial derivatives \( \frac{\partial M}{\partial y} \) and \( \frac{\partial N}{\partial x} \) be continuous in a rectangular region \( R = (\alpha, \beta) \times (\gamma, \delta) \). Then the differential equation \( M(x, y) dx + N(x, y) dy = 0 \) is exact in \( R \) if and only if
\[ \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \]
throughout \( R \).

**Definition (Integrating Factor).**
A function \( \mu(x, y) \) is called an integrating factor for the ordinary differential equation \( M(x, y) dx + N(x, y) dy = 0 \) if the new equation obtained by multiplying by \( \mu \), i.e., \( \mu(x, y) M(x, y) dx + \mu(x, y) N(x, y) dy = 0 \), is an exact differential equation.

**Theorem (Integrating Factor dependent on x alone).**
If \( \frac{1}{N} \left( \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} \right) = P(x) \), which is a function of \( x \) alone, then \( \mu(x) = e^{\int P(x) dx} \) is an integrating factor for the differential equation \( M(x, y) dx + N(x, y) dy = 0 \).

**Theorem (Integrating Factor dependent on y alone).**
If \( -\frac{1}{M} \left( \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} \right) = Q(y) \), which is a function of \( y \) alone, then \( \mu(y) = e^{\int Q(y) dy} \) is an integrating factor for the differential equation \( M(x, y) dx + N(x, y) dy = 0 \).