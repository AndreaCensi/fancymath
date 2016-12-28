# -*- coding: utf-8 -*-

__all__ = ['get_table']

def get_table():
    return list(parse_table(symbols))

def parse_table(data):
    """ Returns a sequence of (unicode char, latex string) """
    data = unicode(data,'utf-8')
    data = data.strip()
    lines = data.split('\n')
    for l in lines:
        if '#' in l:
            l = l[:l.index('#')]
        if not l.strip(): continue

        i = l.index(' ')
        sa = l[:i].strip()
        sb = l[i:].strip()
        yield sa, sb



symbols = r"""
⊗      \otimes
⊔      \sqcup

# use long arrows ⟶ instead of  →
⟶     \to  # same as rightarrow
⟶     \rightarrow
⟶     -->
# use short arrow → instead of ⟶
# →     \to  # same as rightarrow
# →     \rightarrow # same as to
# →     --> # same as to
⟼     \mapsto
⟨     \langle
⟩     \rangle
≤     \leq
≥     \geq
₁     _{1}
₂     _{2}
ₐ     _{a}
ₐ     _{a}
₂     _{b}
ₙ     _{n}
₊     _{+}
ℝ     \mathbb{R}
ℕ     \mathbb{N}
×     \times
∞     \infty
∈     \in
⟦     \llbracket
⟧     \rrbracket
≐     \doteq
⊆     \subseteq
⊇     \supseteq
±     \pm
…     \dots
↑     \uparrow
↓     \downarrow
∩     \cap
○     \circ
∪     \bigcup
≼     \posleq
≺     \poslt
≽     \posgeq
≻     \posgt
⊤     \top
⊥     \bot
≡     \equiv
ξ     \xi
Χ     \Chi
ζ     \zeta
Ν     \Nu
Ψ     \Psi
Σ     \Sigma
Δ     \Delta
Υ     \Upsilon
π     \pi
ι     \iota
ψ     \psi
Κ     \Kappa
ε     \epsilon
δ     \delta
υ     \upsilon
Λ     \Lambda
Τ     \Tau
Ξ     \Xi
κ     \kappa
μ     \mu
Ε     \Epsilon
Ζ     \Zeta
τ     \tau
Θ     \Theta
Π     \Pi
Ι     \Iota
Φ     \Phi
Ο     \Omicron
Ρ     \Rho
θ     \theta
Ω     \Omega
ν     \nu
φ     \phi
ο     \omicron
Μ     \Mu
β     \beta
Η     \Eta
ρ     \rho
α     \alpha
ω     \omega
Γ     \Gamma
η     \eta
χ     \chi
σ     \sigma
γ     \gamma
λ     \lambda
"""
