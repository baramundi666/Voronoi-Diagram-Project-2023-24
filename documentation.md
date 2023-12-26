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
- zainstalowana biblioteka ***NumPy***
- zainstalowana biblioteka do wizualizacji ***bitalg***

# Część użytkownika <a name="user"></a>
Wszystkie moduły opisane powyżej oprócz algorytmów znajdują się w pliku ***main.ipynb***, a algorytmy są importowane z pliku ***algorithms.py***.

Funkcje ***draw_tri*** oraz ***draw_voronoi*** służą do wizualizacji odpowiednio triangulacji Delaunaya oraz diagramu Voronoi za pomocą listy obiektów klasy ***Triangle*** składających się na triangulację Delaunaya odpowiadającą diagramowi Voronoi.

Funkcja ***generate_uniform_points*** służy do losowego generowania chmury punktów na płaszczyźnie.

# Sprawozdanie <a name="report"></a>

W ramach projektu zaimplementowaliśmy dwa algorytmy wyznaczające dla chmury punktów w 2D wierzchołki diagramu Voronoi. 
Umożliwilismy również wizualizację samego diagramu oraz kolejnych kroków algorytmów.
#### 1. Algorytm Bowyera-Watsona
Algorytm iteracyjny konstruuje triangulację Delaunaya.

Dla każdego nowo-dodanego punktu znajduje trójkąty, których okręgi opisane zawierają ten punkt.
Następnie usuwa znalezione trójkąty z obecnej triangulacji i w powstałej w skutego tego "dziurze" tworzy nowe trójkąty poprzez połączenie krawędziami nowo-dodanego punktu z sąsiednimi wierzchołkami powstałego wielokąta.

Na podstawie triangulacji Delaunaya chmury punktów, jesteśmy w stanie wyznaczyć wierzchołki diagramu Voronoi - są to środki okręgów opisanych na każdym z trójkątów wyznaczonej triangulacji.

Graficzne przedstawienie diagramu Voroni polega na połączeniu ze sobą odcinkami środków okręgów sąsiadujących ze sobą trójkątów oraz poprowadzenie dla pozostałych krawędzi półprostych wychodzących z wierzchołka Voronoi i pokrywających symetralną obecnie rozważanej krawędzi.

![example1](example1.png)

