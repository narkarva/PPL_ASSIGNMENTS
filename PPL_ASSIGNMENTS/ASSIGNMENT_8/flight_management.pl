airport(toronto, 50, 60).
airport(madrid, 75, 45).
airport(malaga, 50, 30).
airport(valencia, 40, 20).
airport(barcelona, 40, 30).
airport(paris, 50, 60).
airport(london, 75, 80).
airport(toulose, 40, 30).
flight(toronto, air_canada, madrid, 900, 480).
flight(toronto, united, madrid, 950, 540).
flight(toronto, iberia, madrid, 800, 480).
flight(madrid, air_canada, toronto, 900, 480).
flight(madrid, united, toronto, 950, 540).
flight(madrid, iberia, toronto, 800, 480).
flight(toronto, air_canada, london, 500, 360).
flight(toronto, united, london, 650, 420).
flight(london, air_canada, toronto, 500, 360).
flight(london, united, toronto, 650, 420).
flight(london, iberia, barcelona, 220, 240).
flight(barcelona, iberia, london, 220, 240).
flight(madrid, air_canada, barcelona, 100, 60).
flight(madrid, iberia, barcelona, 120, 65).
flight(barcelona, air_canada, madrid, 100, 60).
flight(barcelona, iberia, madrid, 120, 65).
flight(barcelona, iberia, valencia, 110, 75).
flight(valencia, iberia, barcelona, 110, 75).
flight(madrid, iberia, malaga, 50, 60).
flight(malaga, iberia, madrid, 50, 60).
flight(madrid, iberia, valencia, 40, 50).
flight(valencia, iberia, madrid, 40, 50).
flight(valencia, iberia, malaga, 80, 120).
flight(malaga, iberia, valencia, 80, 120).
flight(paris, united, toulose, 35, 120).
flight(toulose, united, paris, 35, 120).

isflight(X, Y) :- flight(X, _, Y, _, _).
isflight(X, Y) :- flight(Z, _, Y, _, _), isflight(X, Z).
is_two_filghts(X, Y) :- flight(X, _, Z, _, _), flight(Z, _, Y, _, _).
ischeap(A, C, B) :- flight(A, C, B, D, _), D < 400.
preferred_flight(A, C, B) :- ischeap(A, C, B); C == air_canada.
flight_list(From, Airline, To, Price, Duration) :- forall(flight(From, Airline, To, Price, Duration), (print(From), tab(4), print(Airline), tab(4), print(To), tab(4), print(Price), tab(4), print(Duration), nl)).
airport_list(City, Airporttax, Minsecuritydelay) :- forall(airport(City, Airporttax, Minsecuritydelay), (print(City), tab(4), print(Airporttax), tab(4), print(Minsecuritydelay), nl)).
is_air_canada(A, B) :- not(flight(A, united, B, _, _));flight(A, air_canada, B,_, _).
