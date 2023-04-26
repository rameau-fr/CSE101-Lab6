
def BubbleSort(footballers):
    '''
    This function sort footballers given the number of goals they scorred during world cups
    Args:
        footballers: list of footballers [Name, number of Goals, Country]
    Note: this function returns nothing (void function) but directly swap elements in the list
    Note2: You will sort only according to nb of goals --> footballer[i][1]
    '''
    

def returnTopFive(footballers):
    """ This function return the top 5 players from the sorted list!
    Args:
        footballers (list): SORTED footballer list
    
    Returns:
        list: top5 footballers
    """
    top5 = []
    
    return top5


def main():
    # 0. List of 35 top scorers (shuffled!)
    footballers = [ ["Rivaldo", 8, "Brazil"],
    ["Jürgen Klinsmann", 11, "Germany"],
    ["Pelé", 12, "Brazil"],
    ["Gary Lineker", 10, "England"],
    ["Miroslav Klose", 16, "Germany"],
    ["Just Fontaine", 13, "France"],
    ["Thomas Müller", 10, "Germany"],
    ["David Villa", 9, "Spain"],
    ["Iván Zamorano", 7, "Chile"],
    ["Diego Maradona", 8, "Argentina"],
    ["Johan Neeskens", 7, "Netherlands"],
    ["Ronaldo", 15, "Brazil"],
    ["Karl-Heinz Rummenigge", 9, "West Germany"],
    ["Sándor Kocsis", 11, "Hungary"],
    ["Roberto Baggio", 9, "Italy"],
    ["Aldo Serena", 8, "Italy"],
    ["Eusébio", 9, "Portugal"],
    ["Jairzinho", 8, "Brazil"],
    ["Teófilo Cubillas", 10, "Peru"],
    ["Christian Vieri", 9, "Italy"],
    ["Paolo Rossi", 9, "Italy"],
    ["Hristo Stoichkov", 8, "Bulgaria"],
    ["Léonidas", 7, "Brazil"],
    ["Gerd Müller", 14, "West Germany"],
    ["Grzegorz Lato", 10, "Poland"],
    ["Helmut Rahn", 7, "West Germany"],
    ["Vavá", 9, "Brazil"],
    ["Gabriel Batistuta", 10, "Argentina"],
    ["Rudi Völler", 8, "West Germany"],
    ["Uwe Seeler", 8, "West Germany"],
    ["Ademir", 8, "Brazil"],
    ["Oscar Míguez", 8, "Uruguay"],
    ["Helmut Rahn", 10, "West Germany"],
    ["Pelé", 8, "Brazil"],
    ["Ronaldo", 7, "Brazil"]]

    sorted_footballer = sorted(footballers, key=lambda x: x[1], reverse=True)
    #print(sorted_footballer[:5])
    # 1. sort the list using bubble sort
    BubbleSort(footballers)
    #print(footballers)

    # 2. display the top 5 best scorers!!
    print(returnTopFive(footballers))
    
main()
        