# Quiz Generator

## installation

pip install -r requirements.txt

## Usage

### Run the server

```bash
uvicorn main:app --reload
```

### Generate quiz questions

Pour générer des questions de quiz, faites une requête GET au point de terminaison /generate avec le paramètre de requête cours. Le paramètre cours doit être une chaîne contenant le contenu du cours.

curl "<http://localhost:8080/generate?cours=VotreContenuDeCours>"

La réponse sera un tableau JSON de questions de quiz. Chaque question est représentée par un objet JSON avec des champs question, options et answer.

### explain questions

Pour obtenir des explications sur les questions de quiz, faites une requête GET au point de terminaison /explain avec le paramètre de requête question. Le paramètre question doit être une chaîne contenant le contenu de la question.

curl "<http://localhost:8080/explain?question=VotreQuestion&answer=VotreReponse>"


## License

[MIT](https://choosealicense.com/licenses/mit/)

