Król Mateusz 
Zieliński Filip 
## Algorytmy geometryczne 2023/24
# Dokumentacja projektu wieloboki Voronoi
## Spis treści
1. [Część techniczna](#tech)
2. [Część użytkownika](#user)
3. [Sprawozdanie](#report)


# Część techniczna <a name="tech"></a>
Program składa się z następujących modułów:
- importowane biblioteki
    1. ***numpy***
    2. ***bitalg.visualizer.main***
- funkcje umożliwiające wizualizacje
    1. ***draw_tri***
    2. ***draw_voronoi***
- funkcje generujące zbiory danych
    1. ***generate_uniform_points***
- funkcje pomocnicze 
    1. ***orient***
    2. ***collinear***
    3. ***findCircumCenter***
    4. ***checkPosition***
    5. ***obtuseAngle***
- zdefiniowane klasy wykorzystywane przy implementacji algorytmów
    1. ***Point***
    2. ***Edge***
    3. ***Triangle***
- algorytmy
    1. ***Bowyer-Watson algorithm***
- wizualizacja działania algorytmów
- testy do zaimplementowanych algorytmów

Wymagania techniczne:
- zainstalowane narzędzie do wizualizacji ***bitalg***

# Część użytkownika <a name="user"></a>
Wszystkie moduły opisane powyżej oprócz algorytmów znajdują się w pliku ***main.ipynb***, a algorytmy są importowane z pliku ***algorithms.py***.

Funkcje ***draw_tri*** oraz ***draw_voronoi*** służą do wizualizacji odpowiednio triangulacji Delaunaya oraz diagramu Voronoi za pomocą listy obiektów klasy ***Triangle*** składających się na triangulację Delaunaya odpowiadającą diagramowi Voronoi.

Funkcja ***generate_uniform_points*** służy do losowego generowania chmury punktów na płaszczyźnie.

# Sprawozdanie <a name="report"></a>