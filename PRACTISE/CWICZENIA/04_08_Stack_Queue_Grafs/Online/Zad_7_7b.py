""" 
Znany  operator  telefonii  komórkowej  Pause  postanowił  zakonczyc  działalnosc  wPolsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (któretworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a ope-ratorowi dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegudziałajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytmpodający kolejność wyłączania stacji
 """

"""generujemy drzewo rozpinające dfsem, a następnie rekurencyjnie usuwamy wszystkie węzły bezdzietne """

""" Czyli usuwamy od największego do najmniejszego czasu w zgenerowanej DFSem wersji drzewa """
