# fancymath

Write fancy math symbols in your email!

Too many engineers lost their lives to come up with Unicode,
we might just as well use it.

This is a simple LaTeX sequences to Unicode translation for math symbols.


Example:

    $ cat spivak.txt

    When these symbols, \otimes and \sqcup, are used to denote
    morphisms, they indicate a monoidal product. So, you shouldn't
    use it to denote the universal arrow itself.

    In other words, given f:A-->X and g: B-->Y, you can write
       f \sqcup g: A \sqcup B \to X \sqcup Y
    or
       f \otimes g: A\otimes B \to X \otimes Y
    But given f: A-->X and g: B-->X, you shouldn't name the
    universal morphism  A \sqcup B --> X by f\sqcup g ..

    $ fancymath < spivak.txt

    When these symbols, ⊗ and ⊔, are used to denote
    morphisms, they indicate a monoidal product. So, you shouldn't
    use it to denote the universal arrow itself.

    In other words, given f:A⟶X and g: B⟶Y, you can write
       f ⊔ g: A ⊔ B ⟶ X ⊔ Y
    or
       f ⊗ g: A⊗ B ⟶ X ⊗ Y
    But given f: A⟶X and g: B⟶X, you shouldn't name the
    universal morphism  A ⊔ B ⟶ X by f⊔ g ..


### Installation

Simply this:

    $ pip install fancymath

### Installation from source if you want to change the symbols

1. download this repo
2. use this:

   $ python setup.py develop
