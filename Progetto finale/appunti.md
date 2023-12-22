# 1. Yahoo Answers
[Link kaggle](https://www.kaggle.com/datasets/thedevastator/yahoo-answers-topics-dataset)

uso di csp come filtering di risposte date dal modello ML,

input modello ML: question title, question content 

output modello ML: best anwers, o topics

input csp: variabili booleane tante quante sono quelle dell'output ML

output csp: variabili a 1 filtrate per pertinenza

constraints: (tutti opzionali)
>variabile della risposta deve essere di un topic, o categoria di topic

>la best answer deve contenere le parole chiave della domanda (inserite in input all'inizio opzionalmente)

>la best answer deve almeno essere di una determinata lunghezza di caratteri

>la best answer deve essere almeno di un determinato numero di parole

# 2. AskReddit Questions and Answers

[Link kaggle](https://www.kaggle.com/datasets/rodmcn/askreddit-questions-and-answers?select=reddit_questions.csv)

uso di csp come filtering di risposte date dal modello ML,

input modello ML: 
> se question:
> - question text
> - question date
> - question votes

> se answer:
> - answer text
> - answer date (periodo di tempo in cui avresti preso i voti) (opzionale)

output modello ML: 

> se input=question:
> - answer text
> - answer date
> - answer votes

> se input=answer:
> - answer votes
> - answer date (periodo di tempo in cui avresti preso i voti)

se nell'input si specifica la data, una sola risposta, altrimenti lista di risposte ordinate per data (intervallate di un mese)

input csp: 
> se input=question:
> - variabili booleane tante quante sono quelle dell'output ML

> se input=answer:  
> - variabili booleane tante quante sono quelle dell'output ML


output csp: variabili a 1 filtrate per pertinenza

constraints: (tutti opzionali)

### se input=question:

>la answer deve contenere le parole chiave della domanda (inserite in input all'inizio opzionalmente)

>la best answer deve almeno essere di una determinata lunghezza di caratteri

>la best answer deve essere almeno di un determinato numero di parole

>la best answer deve essere almeno di un determinato numero di voti

### se input=answer:

nessun constraint

# Altre idee:
1. [Food.com Recipes and Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions/data)
2. [Food Images](https://www.kaggle.com/datasets/kmader/food41)
3. Unire i primi 2 punti e creare una AI unica, applicare il csp solo alla seconda parte