from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import pickle
import nltk


#desde aqui





#asta aqui

def home(request):
    peliculas = Pelicula.objects.all()
    print(peliculas)
    contexto = {'peliculas': peliculas}
    return render(request, "index.html", contexto)

# Extract features from the input list of words
def extract_features(words):
    return dict([(word, True) for word in words])



def addComment(request, pk):
    input_reviews = []
    # pelicula = Pelicula.objects.get(pk=pk)
    pelicula = get_object_or_404(Pelicula, pk=pk)
    comentario = comententario.objects.filter(movie=pelicula.id).order_by('id').reverse()
    print("Probabilidad de comentario y la pelicula")
    print(pelicula)
    print(comentario)
    #contexto = {'pelicula': pelicula}

    if request.method == 'POST':
        comment = request.POST['comment']
        #-------------------
        f = open(r'datos/classifier.pickle', 'rb')
        classifier = pickle.load(f)
        print(classifier)
        f.close()

        # Test input movie reviews
        input_reviews.append(comment)

        probabilidad = 0
        prediccionSentimental = ""

        print("\nMovie review predictions:")
        for review in input_reviews:
            print("\nReview:", review)

            # Compute the probabilities
            probabilities = classifier.prob_classify(extract_features(review.split()))


            # Pick the maximum value
            predicted_sentiment = probabilities.max()
            prediccionSentimental = predicted_sentiment
            probabilidad = round(probabilities.prob(predicted_sentiment), 2)
            # Print outputs
            print("Predicted sentiment:", predicted_sentiment)
            print("Probability:", round(probabilities.prob(predicted_sentiment), 2))
        # -------------------

        print(comment)
        #comentariosInput.append(comment)

        comentarioModel = comententario()

        comentarioModel.comments = comment
        comentarioModel.clasePredecida = prediccionSentimental
        comentarioModel.probabiliad = probabilidad
        comentarioModel.movie = pelicula

        comentarioModel.save()
        print(comentarioModel.save())

        #return redirect('crearComentario/'+str(pk)+'/')
        #return HttpResponseRedirect('/crearComentario/'+str(pk)+'/')

    return render(request, 'crearComentario.html', {'pelicula': pelicula, 'comentario': comentario})
