$\wedge$  $\vee$

# Esercizio 1

a ← b ∧ c.

a ← e ∧ f. 

b ← d.

b ← f ∧ h.

c ← e. 

d ← h.

e.

f ← g.  

g ← c. 

**1) model of the knowledge base** 
```
un modello per la knowledge base data può essere:
Definita funzione modello A(x) dove x è un atomo:
A(a) = true
A(b) = true
A(c) = true
A(d) = true 
A(e) = true
A(f) = true
A(g) = true
A(h) = true 
```

**2) interpretation that is not a model of the knowledge base**
```
un'interpretazione che non sia un modello della knowledge base può essere una intepretazione dove una o più proposizioni di suddetta KB hanno esito falso:
definita funzione interpretazione B(x) dove x è un atomo:
B(a) = true
B(b) = false
B(c) = false
B(d) = true
B(e) = true
B(f) = true
B(g) = true
B(h) = true
```

**3) 2 atomi che siano conseguenza logica della Knowledge Base**
```
applicando l'algoritmo di bottom-up proof abbiamo trovato che gli atomi {e, c, g, f, a} comportano KB
(gli atomi elencati sono conzeguenza logica di KB)
```
Ad esempio:
>KB $\models$ e
>
>KB $\models$ c

**4) 2 atomi che non siano conseguenza logica della KB**

```
Dalla lista di atomi trovata nel punto 3) possiamo dedurre che:
```
> KB $\not\models$ b
>
> KB $\not\models$ d
>
> KB $\not\models$ h

# Esercizio 2
numeriamo le proposizioni della KB per farne riferimento durante la bottom-up proof.
1.  *a ← b ∧ c.*

2. *b ← d.*

3. *b ← e.*

4. *c.*

5. *d ← h.*

6. *e.*

7. *f ← g ∧ b.*

8. *g ← c ∧ k.*

9. *j ← a ∧ b.*

**1) Mostrare come la procedura di bottom-up proof funziona per questo esempio. Elencare tutte le conseguenze logiche di KB**
```
{}
{c} per 4.
{c,e} per 6.
{c,e,b} per 3.
{c,e,b,a} per 1.
{c,e,b,a,j} per 9.
```
KB $\models$ c, e, b, a, j

**2) f non è una conseguenza logica di KB. Dare un modello nel quale f è falsa**
```
Un modello in cui f è falsa è:

a = false
b = false
c = true
d = false
e = true
f = false
g = false
h = false
j = false
k = false
```


**3) a è una conseguenza logica di KB. Dare una derivazione top-down per la query ask ```a```**

>yes $\leftarrow$ ```a```
>
>derivo ```a``` in 1.
>
>yes $\leftarrow$ ```b``` $\wedge$ ```c```
>
>derivo ```b``` in 2.
>
>yes $\leftarrow$ ```d``` $\wedge$ ```c```
>
>derivo ```d``` in 5.
>
>yes $\leftarrow$ ```h``` $\wedge$ ```c```

proof fail, ```h``` non è in testa ad alcuna produzione

Riprovo derivando ```b``` in 3. invece che in 2:

>yes $\leftarrow$ ```b``` $\wedge$ ```c```
>
>derivo ```b``` in 3.
>
>yes $\leftarrow$ ```e``` $\wedge$ ```c```
>
>derivo ```e``` in 6.
>
>yes $\leftarrow$ ```c```
>
>derivo ```c``` in 4.
>
>yes $\leftarrow$ 

procedura proof finita

# Esercizio 3

*goto_forest ← walking.*

*get_gun ← hunting.*

*goto_forest ← hunting.*

*get_gun ← robbing.*

*goto_bank ← robbing.*

*goto_bank ← banking.*

*fill_withdrawal_form ← banking.*

*false ← banking ∧ robbing.*

*false ← wearing_good_shoes ∧ goto_forest.*

*assumable walking,hunting,robbing,banking*

**1) Supponi che ```get_gun``` è osservato. Quali sono tutte le spiegazioni minimali per questa osservazione?**

Dato che ```get_gun``` è osservato, vediamo in quale produzione è in testa:

```
get_gun ← hunting.

get_gun ← robbing.
```

per mantenere get_gun a true ci sono 2 modi:

o ```hunting``` o ```robbing``` devono essere assunti ad essere true.

```get_gun``` non è specificato da nessuna altra parte, quindi ci sono 2 spiegazioni minimali:
>{```hunting```} e {```robbing```}.

**2) Supponi che ```get_gun``` $\wedge$ ```goto_bank``` è osservato. Quali sono tutte le spiegazioni minimali per questa osservazione?**


Per mantenere ```get_gun``` a true si applica lo stesso procedimento sopra, con spiegazioni al momento {```hunting```} e {```robbing```}

in quanto a goto_bank abbiamo le 2 produzioni:

```
goto_bank ← robbing.

goto_bank ← banking.
```

visto che ```robbing``` è il corpo anche di una proposizione con in testa ```get_gun```
una spiegazione minimale rimane al momento {```robbing```}

nell'altro caso abbiamo ```banking```, quindi la spiegazione minimale {```hunting```} la uniamo con ```banking```
= {```hunting```, ```banking```}

{```robbing```, ```banking```} **non** può essere una spiegazione poiché la proposizione:

```
false ← banking ∧ robbing
```

impedisce che entrambi gli atomi siano assumibili.

**In conclusione** le spiegazioni minimali per l'osservazione ```get_gun``` $\wedge$ ```goto_bank``` sono 2:
>{```robbing```} and {```hunting```, ```banking```}



**3) C'è qualcosa che può essere osservato per rimuovere una di queste come una spiegazione minimale?**
**Cosa deve essere aggiunto per rendere possibile spiegarlo?**

per rimuovere una spiegazione minimale si può rendere osservabile ```fill_withdrawal_form```, tale atomo è in testa a ```banking```, quindi in ogni spiegazione minima ```banking``` deve essere true, questo genera un conflitto con ```robbing``` per la proposizione:

```
false ← banking ∧ robbing
```
quindi {```robbing```} non può più essere una spiegazione minimale, rimarrebbe:
>{```hunting```, ```banking```}

aggiungendo 

```
fill_withdrawal_form ← robbing
```
renderebbe {```robbing```} spiegabile minimalmente, in quanto sarebbe nel corpo di tutti e tre degli atomi osservati (```get_gun```, ```goto_bank```, ```fill_withdrawal_form```)

**4) Supponi che ```goto_bank``` è osservato. Quali sono tutte le spiegazioni minimali per questa osservazione?**

Le spiegazioni minimali per ```goto_bank``` sono : 

>{```robbing```}, {```banking```}


**5) Supponi che ```goto_bank``` ∧ ```get_gun``` ∧ ```fill_withdrawal_form``` è osservato. Quali sono tutte le spiegazioni minimali per questa osservazione?**

La spiegazione minimale per ```goto_bank``` ∧ ```get_gun``` ∧ ```fill_withdrawal_form``` è una:

>{```hunting```, ```banking```}















